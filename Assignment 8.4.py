filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        words_list = []

        for line in file:
            words = line.split()
            for word in words:
                if word not in words_list:
                    words_list.append(word)

        words_list.sort()
        print(words_list)

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
