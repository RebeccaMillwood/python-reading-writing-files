# Question 1:

names = []

with open("names_file.txt") as txt_file:
    for line in txt_file:
        line = line.strip()
        names.append(line)

print(names)

for index, name in enumerate(names):
    print(f"{index+1}. {name}")

with open("names_file_output.txt", "w") as txt_file:
    for index, name in enumerate(names):
        txt_file.write(f"{index+1}. {name}" + "\n")