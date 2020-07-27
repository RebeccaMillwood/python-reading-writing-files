# Question 2: output column headings and values for columns 2, 3 & 5

# import csv

# colours = []

# with open("colours_213.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colours.append(line)

# # print(colours)


# for data in colours:
#     print(f"{data[1].strip():<15} {data[2].strip():<10} {data[4].strip():<10}")


# Question 3: output the number of times 'red', 'green' and 'blue' appear in english name

import csv

colours = []

with open("colours_213.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line)

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