# Question 2: output column headings and values for columns 2, 3 & 5

# import csv

# colours = []

# with open("colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colours.append(line)

# print(colours)


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

import csv

colours = []

with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line)

# print(colours)
 

# count_yellow = 0
# count_beige = 0
# count_ivory = 0
# for data in colours:
#     count1 = data[4].lower().count("yellow")
#     count_yellow += count1
#     count2 = data[4].lower().count("beige")
#     count_beige += count2
#     count3 = data[4].lower().count("ivory")
#     count_ivory += count3
# print(count_yellow, count_beige, count_ivory)
# print(f"Yellow: {count_yellow}")
# print(f"Beige: {count_beige}")
# print(f"Ivory: {count_ivory}")

count_red = 0
count_green = 0
count_blue = 0
for data in colours:
    count1 = data[4].lower().count("red")
    count_red += count1
    count2 = data[4].lower().count("green")
    count_green += count2
    count3 = data[4].lower().count("blue")
    count_blue+= count3
# print(count_red, count_green, count_blue)
print(f"Red: {count_red}")
print(f"Green: {count_green}")
print(f"Blue: {count_blue}")




    