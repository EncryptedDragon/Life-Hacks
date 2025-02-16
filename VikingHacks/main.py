import random
import time
import streamlit as st
import pandas as pd

st.title("Life Hacks ᕙ(  •̀ ᗜ •́  )ᕗ")
mode = st.sidebar.radio("Choose an option:", ["Random Exercise Generator", "Daily Log", "Meditation"])

if mode == "Random Exercise Generator":
    st.subheader("Random Exercise Generator")

    workout_area = st.selectbox("Choose a workout area:", ["Arms", "Legs", "Core"])

    exercise_list = {
        "Arms": [
            {"exercise": "Pushups", "min_reps": 10, "max_reps": 30},
            {"exercise": "Pullups", "min_reps": 5, "max_reps": 15},
            {"exercise": "Tricep Dips", "min_reps": 10, "max_reps": 20},
            {"exercise": "Arm Circles", "min_reps": 30, "max_reps": 60},
            {"exercise": "Bicep Curls", "min_reps": 10, "max_reps": 25},
            {"exercise": "Tricep Pushdowns", "min_reps": 10, "max_reps": 25},
        ],
        "Legs": [
            {"exercise": "Squats", "min_reps": 15, "max_reps": 50},
            {"exercise": "Lunges", "min_reps": 10, "max_reps": 30},
            {"exercise": "Leg Press", "min_reps": 10, "max_reps": 20},
            {"exercise": "Leg Extensions", "min_reps": 10, "max_reps": 20},
            {"exercise": "Leg Curls", "min_reps": 10, "max_reps": 20},
            {"exercise": "Leg Raises", "min_reps": 10, "max_reps": 30},
        ],
        "Core": [
            {"exercise": "Situps", "min_reps": 20, "max_reps": 50},
            {"exercise": "Plank", "min_reps": 30, "max_reps": 90},  # Plank time in seconds
            {"exercise": "Burpees", "min_reps": 10, "max_reps": 30},
            {"exercise": "Crunches", "min_reps": 20, "max_reps": 50},
            {"exercise": "Bicycle Crunches", "min_reps": 20, "max_reps": 50},
        ]
    }

    if st.button("Generate Random Exercise"):
        # Pick a random exercise from the chosen workout area
        selected_exercise = random.choice(exercise_list[workout_area])
        exercise_name = selected_exercise["exercise"]
        min_reps = selected_exercise["min_reps"]
        max_reps = selected_exercise["max_reps"]

        # Generate a random number of reps within the range
        reps = random.randint(min_reps, max_reps)

        st.success(f"Your random exercise is: {exercise_name} - {reps} reps")

elif mode == "Daily Log":
    st.subheader("Daily Exercise Log")

    date = st.text_input("Enter the date (dd/mm/yyyy):")
    exercise_time = st.number_input("How long did you exercise? (minutes)", min_value=0, step=5)
    explanation = st.text_area("What did you do during that time?")

    if st.button("Save Entry"):
        with open("myFile.txt", "a") as file:
            if exercise_time >= 60:
                time_display = f"{exercise_time / 60:.2f} hours"
            else:
                time_display = f"{exercise_time} minutes"
            file.write(f"Date: {date}, Time Spent: {time_display}, Activity: {explanation}\n")
        st.success("Your journal entry has been saved!")

    if st.button("View Journal Entries"):
        try:
            with open("myFile.txt", "r") as file:
                entries = file.readlines()
                if entries:
                    st.subheader("Previous Journal Entries")
                    data = []
                    for entry in entries:
                        entry_parts = entry.strip().split(", ")
                        date = entry_parts[0].split(": ")[1]
                        time_spent = entry_parts[1].split(": ")[1]
                        activity = entry_parts[2].split(": ")[1]
                        data.append([date, time_spent, activity])

                    df = pd.DataFrame(data, columns=["Date", "Time Spent", "Activity"])
                    st.dataframe(df)
                else:
                    st.warning("No journal entries found.")
        except FileNotFoundError:
            st.error("No entry info available.")

    if st.button("Remove Last Entry"):
        try:
            with open("myFile.txt", "r") as file:
                entries = file.readlines()

            if entries:
                entries.pop()

                with open("myFile.txt", "w") as file:
                    file.writelines(entries)

                st.success("The last journal entry has been removed.")
            else:
                st.warning("No entries to remove.")
        except FileNotFoundError:
            st.error("No entry info available.")

    if st.button("Clear All Entries"):
        try:
            with open("myFile.txt", "w") as file:
                file.truncate(0)
            st.success("All journal entries have been cleared.")
        except FileNotFoundError:
            st.error("No entry info available.")

elif mode == "Meditation":
    st.subheader("Meditation Session")

    h = st.number_input("How many hours would you like to meditate for?", min_value=0)
    m = st.number_input("How many minutes would you like to meditate for?", min_value=0)
    s = st.number_input("How many seconds would you like to meditate for?", min_value=0)

    total_seconds = int(h) * 3600 + int(m) * 60 + int(s)

    start_button = st.button("Start Meditation")
    stop_button = st.button("Stop Meditation")

    if start_button:
        with st.empty():  # Update the UI dynamically
            while total_seconds > 0:
                minutes_left = total_seconds // 60
                seconds_left = total_seconds % 60
                st.write(f"Meditation in progress: {minutes_left} minutes and {seconds_left} seconds remaining...")
                time.sleep(1)
                total_seconds -= 1
                if stop_button:  # Stop meditation if button is pressed
                    break
            st.success("Your meditation has ended.")

    if stop_button:
        st.success("Your meditation has been stopped.")
