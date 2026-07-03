# 1. String
name = input("Enter your name: ")
print("\nHello,", name)
print("Length of your name:", len(name))
print("Uppercase:", name.upper())

# 2. List
subjects = ["Python", "C", "SQL"]
subjects.append("HTML")
print("\nSubjects List:")
for subject in subjects:
    print(subject)

# 3. Tuple
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print("\nFirst Day:", days[0])
print("Last Day:", days[-1])

# 4. Dictionary
student = {
    "Name": name,
    "Age": 18,
    "Course": "B.E. CSE"
}

print("\nStudent Details:")
for key, value in student.items():
    print(key, ":", value)

# 5. Set
numbers = {10, 20, 30, 20, 40, 10}
print("\nUnique Numbers:")
print(numbers)

numbers.add(50)
print("After adding 50:")
print(numbers)