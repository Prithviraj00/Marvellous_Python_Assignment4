from functools import reduce

Even = lambda A : A %2 == 0

square = lambda A : A**2

Add = lambda A,B : A + B


def main() :
    data = []
    print("Enter your numbers :")
    value1 = int(input())
    
    print("Please enter in numeric values :")
    for i in range (value1):
        no = int(input())
        data.append(no)
    print("Input Data :",data)

    FData = list(filter(Even,data))
    print("Filter output :",FData)

    MData = list(map(square,FData))
    print("Map output :",MData)

    RData = reduce(Add,MData)
    print("Reduce output :",RData)
        


if __name__ == "__main__":
    main()