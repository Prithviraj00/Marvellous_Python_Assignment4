from functools import reduce

def prime(no1):
    is_prime = True
    for i in range(2,no1):
        if no1 % i == 0:
            is_prime = False
            return False
            
    if is_prime :
        return True

def multiplication(value1):
    ans = value1*2;
    return ans

def maximum (no1,no2):
    if no1 > no2:
        return no1
    else:
        return no2


def main() :
    data = []
    print("Enter your numbers :")
    value1 = int(input())
    
    print("Please enter in numeric values :")
    for i in range (value1):
        no = int(input())
        data.append(no)
    print("Input Data :",data)

    FData = list(filter(prime,data))
    print("Filter output :",FData)

    MData = list(map(multiplication,FData))
    print("Map output :",MData)

    RData = reduce(maximum,MData)
    print("Reduce output :",RData)
        


if __name__ == "__main__":
    main()