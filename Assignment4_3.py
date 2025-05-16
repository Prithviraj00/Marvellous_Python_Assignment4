from functools import reduce

Compare = lambda A : A >= 70 and A <= 90

Increase = lambda A : A+10

Mul = lambda A,B : A * B


def main() :
    data = []
    print("Enter your numbers :")
    value1 = int(input())
    
    print("Please enter in numeric values :")
    for i in range (value1):
        no = int(input())
        data.append(no)
    print("Input Data :",data)

    FData = list(filter(Compare,data))
    print("Filter output :",FData)

    MData = list(map(Increase,FData))
    print("Map output :",MData)

    RData = reduce(Mul,MData)
    print("Reduce output :",RData)
        


if __name__ == "__main__":
    main()