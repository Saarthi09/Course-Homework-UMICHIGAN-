largest = None
smallest = None

while True:
    num = input("Enter or number (type 'done' to end the process): ")
    if num == 'done':
        break
    try:
        n = int(num)
        if largest is None or n>largest:
            largest = n
        if smallest is None or n<smallest:
            smallest = n
    except:
        print("Invalid Input")
if largest is not None and smallest is not None:
    print("Maximum: "+ str(largest))
    print("Minimum: "+ str(smallest))