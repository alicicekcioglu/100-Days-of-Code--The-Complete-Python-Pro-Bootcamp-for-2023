import random
# For creating dict comprehension:
#   new_dict = {new_key: new_value for item in list}
#   new_dict = {new_key: new_value for (key, value) in dict.items()}
#   new_dict = {new_key: new_value for (key, value) in dict.items() if test}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (degree * 9/5) + 32 for (day,degree) in weather_c.items()}
print(weather_f)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)
