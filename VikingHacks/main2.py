import random
import time

while True: 
  mode = input("Would you like to access the random exercise generator, the daily log, meditation, or exit the program? (1 for random excercise generator, 2 for daily log, 3 for meditation, 4 for exit): ")
  if mode == "1":
    print("Welcome to the random exercise generator!")
    while True: 
      workout_area = input("What area of the body would you like to workout? (arms(1), legs(2), core(3))?")

      exercise_list_arms = ["pushups", "pullups", "tricep dips", "arm circles", "bicep curls", "tricep pushdowns"] 
      exercise_list_legs = ["squats", "lunges", "leg press", "leg extensions", "leg curls", "leg raises"]
      exercise_list_core = ["situps", "squats", "plank", "burpees", "crunches", "bicycle crunches"]
      if workout_area == "1" or workout_area.lower() == "arms":
        print("Your random excercise is: " + random.choice(exercise_list_arms))
      elif workout_area == "2" or workout_area.lower() == "legs":
        print("Your random excercise is: " + random.choice(exercise_list_legs))
      else:
        print("Your random excercise is: " + random.choice(exercise_list_core))
  elif mode == "2":
    print("Welcome to the daily log!")
    while True:
      YesNo = input("Would you like to add a new journal entry? (y/n)")
      if YesNo.lower() == "yes" or YesNo.lower() == "y":
        file = open("myFile.txt", "a")
        exerciseTime = input("How long did you exercise (min)?")
        explanation = input("What did you do in that time?")
        date = input("What is the date? (dd/mm/yyyy)")
        timeMins = int(exerciseTime)
        if timeMins >= 60:
          timeHours = timeMins/60
          print(f'You exercised for {timeHours} hours')
          file.write(f'Day {date}, How much time spent: {timeHours} hours, {explanation}\n')
        else:
          file.write(f'Day {date}, How much time spent: {timeMins} minutes, {explanation}\n')
        file.close()

      elif YesNo.lower() == "no" or YesNo.lower() == "n":
        entries = input("Would you like to read your previous journal entries? (y/n)")
        if entries.lower() == "yes" or entries.lower() == "y":
          print("Here are your previous journal entries:")
          file = open("myFile.txt", "r")
          for line in file:
            print(line.strip())
          file.close()
        if entries.lower() == "no" or entries.lower() == "n":
          print("Thank you and have a nice day!")
          break
        else: 
          continue
      else: 
        continue
  elif mode == "3":
    print("Welcome to the meditation!")
    meditatiion_start = input("Would you like to start your meditation (y/n)? ")
    if meditatiion_start.lower() == "yes" or meditatiion_start.lower() == "y":
      print("You will now begin your meditation.")
      h = input("How many hours would you like to meditate for? ")
      m = input("How many minutes would you like to meditate for? ")
      s = input("How many seconds would you like to meditate for? ")
      total_seconds = int(h) * 3600 + int(m) * 60 + int(s)
      while total_seconds > 0:
        total_seconds = total_seconds - 1
        time.sleep(1)
      print("Your meditation has ended.")

    if meditatiion_start.lower() == "no" or meditatiion_start.lower() == "n":
      print("Thank you and have a nice day!")
      break

  elif mode == "4": 
    break
  else: 
    continue