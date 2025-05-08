a = 10
b = 20
c = 30

sum = a + b + c
print(f"sum:{sum}")

product = a*b*c
print(f"product:{product}")

average = sum/3

print(f"Average : {average}")


# strings

name = "Nandhini"

print("Uppercase:", name.upper())
print("Length of name:", len(name))
print("First 3 letters:", name[0:3])


# List

numbers = list(range(4))


numbers.append(1)
print("Number:", numbers)

numbers.remove(0)

print("Removed the Number 0:", numbers)

numbers.sort()

print("sorted Number:", numbers)

# Dictionaries

student = {
    "name": "Nithilan",
    "age": 9,
    "grade": "4th"
}

student['passed'] = True

print("Student:", student)
for value in student.values():
    print(value)

print(list(student.values()))
print(list(student.keys()))


# sets

my_set = {1, 2, 3, 3, 4, 5, 3, 2, 6, 5, 7, 9, 8}

my_set.add(0)
print("mySet:", my_set)
my_set.pop()

print("current set:", my_set)

my_set.remove(6)

print("After Removed", my_set)


# Create a small program to swap two numbers.

a = 5
b = 9
print("Before Swapping a,b:", a, b)
a, b = b, a

print("After Swapping a,b:", a, b)
