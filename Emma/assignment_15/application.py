def main():
    start = int(input("Enter start of the range : "))
    end = int(input("Enter end of the range : "))
    step = int(input("Enter number of steps to skip : "))
    for i in range(start,end,step):
        print(i)

main()