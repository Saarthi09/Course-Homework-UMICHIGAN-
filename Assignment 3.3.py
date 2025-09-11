score = input("Enter score: ")
try:
    s = float(score)
    try:
        if s<=1:
            try:
                if s>=0.9:
                    print("A")
                elif s>= 0.8:
                    print("B")
                elif s>= 0.7:
                    print("C")
                elif s>= 0.6:
                    print("D")
                elif s<0.6:
                    print("F")
            except:
                exit()
        else:
            print("out of range")
    except:
        print("The range if from 0 to 1")
except:
    print("Enter a valid number")
k = input("press bs to close")