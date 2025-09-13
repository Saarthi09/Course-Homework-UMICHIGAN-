filename = input("Enter file name: ")
try:
    file = open(filename, "r")
except FileNotFoundError:
    print("File cannot be opened:", filename)
    quit()

count = 0
accumulator = 0.0

for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        col_pos = line.find(":")
        value = float(line[col_pos+1:].strip())
        accumulator += value

file.close()

if count > 0:
    average = accumulator / count
    print("Average spam confidence:", average)
else:
    print("No matching lines found.")