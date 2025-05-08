# List unpacking

from array import array
number = list(range(5, 20))
print(number[4])
print(number[::3])
first, second, *other = number

print(other)

# packing the list


def Number(*even):
    print(even)


Number(2, 4, 6, 8, 12)


# insert, delete

primary_numbers = [1, 2, 3, 4, 5]
primary_numbers.append(6)
primary_numbers.insert(3, 8)

primary_numbers.remove(2)
del primary_numbers[1: 3]
print(primary_numbers)

tuple_repeated_Num = (3,) * 10
print(tuple_repeated_Num)

List_repeated_num = [7] * 20
print(List_repeated_num)

primary_numbers += [3] * 10
print(primary_numbers)

print(primary_numbers.count(3))

print(primary_numbers.index(3))

sample_Num = [4, 1, 48, 21, 2]

sample_Num.sort(reverse="true")

print(sample_Num)

family = [
    ("Suresh", 39),
    ("Niranjan", 5),
    ("Nandhini", 33),
    ("Nithilan", 9)
]


def sort_items(item):
    return item[1]


family.sort(key=sort_items, reverse=True)
print(family)


# Lambda

family = [
    ("Suresh", 39),
    ("Niranjan", 5),
    ("Nandhini", 33),
    ("Nithilan", 9)
]

family.sort(key=lambda item: item[0])

print(family)


# Map function

x = list(map(lambda item: item[1], family))
print("list", x)


# List of comprehensive

y = [item[1] for item in family if item[1] > 10]

print(y)


# stacks LIFO

# Example as Browser history

browser_history = [1, 2, 3, 4]

browser_history.append(5)

browser_history.pop()
print(browser_history)


# Queue FIFO

# Tuples

sample_tuple = 1, 5, 6
print(list(sample_tuple))


# Swapping variables

a = 10

b = 50

a, b = b, a

print(a)

# Arrays => from array import array


x = array("i", [1, 2, 4, 8, 0])

# It allows only int("i")

num_value = [1, 2, 2, 2, 3, 44, 5, 55, 7, 7, 9, 3]
num_without_sort = [1, 4, 2, 6, 5]
set_num = set(num_value)
print(set_num)
print(num_without_sort)

another_set = {1, 3, 10}

print(set_num | another_set)
print(set_num & another_set)
print(set_num - another_set)
print(set_num ^ another_set)


# Dict
fav_sport = dict(Volleyball=95, Badmidton=85)


fav_sport['cricket'] = 70
print(fav_sport)

if 'cricket' in fav_sport:
    print("its there cricket")

print(fav_sport.get("Volleyball"))

# dict comprehension

value = {x: x*2 for x in range(5)}
print(value)

tuple_value = [x*2 for x in range(5)]

print(tuple_value)


sentence = "This is common interview question"

Highest_char = {}

for letters in sentence:
    if letters in Highest_char:
        Highest_char[letters] += 1
    else:
        Highest_char[letters] = 1

print(Highest_char)

sorted_value = sorted(Highest_char.items(),
                      key=lambda char: char[1], reverse=True)

print(sorted_value)
