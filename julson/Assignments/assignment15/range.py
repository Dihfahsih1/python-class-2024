def main(start, end, step):
    # Using range() with specified start, end, and step
    for i in range(start, end, step):
        print(i)

if __name__ == "__main__":
    # Calling main function with start, end, and step values
    start = int(input("Enter start value: "))
    end = int(input("Enter end value: "))
    step = int(input("Enter step value: "))

    main(start, end, step)