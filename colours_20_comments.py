# Question 2: output column headings and values for columns 2, 3 & 5

# import csv

# colours = []

# with open("colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colours.append(line)

# # print(colours)


# for data in colours:
#     print(f"{data[1].strip():<15} {data[2].strip():<10} {data[4].strip():<10}")


# below code is trying to output to new file but not working:

# my code:
# with open("colours_20_output.csv", mode="w") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=",")
#     for data in colours:
#         csv_writer.writerows([data[1].strip()], [data[2].strip()], [data[4].strip()])

# error message:
# Traceback (most recent call last):
#   File "colours_20.py", line 20, in <module>
#     csv_writer.writerows([data[1].strip()], [data[2].strip()], [data[4].strip()])
# TypeError: writerows() takes exactly one argument (3 given)


# Question 3: output the number of times 'red', 'green' and 'blue' appear in english name


# import csv

# colours = []
# english_name = []

# with open("colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colours.append(line)


# for english in colours:
#     print(f"{english[4].strip()}")

# for english in colours:
#     english_name.append(english[4])

# print(english_name)    



# Check if the phrase "ain" is present in the following text:

# txt = "The rain in Spain stays mainly in the plain"
# x = "ain" in txt
# print(x)


# txt = english_name

# x = "yellow" in txt

# print(x)


# item = "red"

# if item in english_name:
#     print(true)


# for name in english_name:
#     print(name) 




# name = "red"

# if name == "yellow":
#     print("cool")

# else:
#     print("unlucky")

# list1 = ["tomato red", "green", "lobster red", "yellow"]

# colour_count = list1.count("red")
# print(colour_count)

# colours2 = []

# for colour in english_name:
#     colours2.append(str.split(colour))
    
# print(colours2)


# for name in colours2:
#     colour_count = colours2.count("yellow")
#     print(name)
#     # print(colour_count)


# print(english_name)
# substring = " English"

# count = english_name.count(substring)

# print(substring)
# print(count)


# trying again with original Q2 code:

import csv

colours = []

with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line)

print(colours)


# for data in colours:
#     print(f"{data[1].strip():<15} {data[2].strip():<10} {data[4].strip():<10}")


colour = "yellow"
count = colours.count("yellow")

for colour in colours:
    if colour[4] == colour:
        print(name)