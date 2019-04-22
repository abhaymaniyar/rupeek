def hasDigits(A, B):
    listA = list(str(A))
    listB = list(str(B))
    yeah = True
    for digit in listB:
        if digit in listA:
            listA.remove(digit)

    if len(listA) == 1:
        return True
    else:
        return False


def hasArrayTwoCandidates(Arr,arr_size,sum): 
    l = 0
    r = arr_size-1
    A = sum - Arr[l]
    B = Arr[l]

    # traverse the array for the two elements 
    while len(str(A)) >= 2: 
        lenA = len(str(A))
        lenB = len(str(B))
        if (lenA >= 2 and lenA - lenB == 1):
            if (A + B == sum): 
                if(hasDigits(A, B)):
                    print(str(A) + "   " + str(B))
        
        l += 1
        A = sum - Arr[l]
        B = Arr[l]
    print("\n")


# hasArrayTwoCandidates(A, 1002, 1002)

if __name__ == "__main__":
    input_file = open("testdata.in.txt")
    t = input_file.readline()
    for i in range(int(t)):
        sum = int(input_file.readline())
        Arr = []
        for i in range(sum):
            Arr.append(i + 1)
        print("TEST #", i + 1)
        hasArrayTwoCandidates(Arr, sum, sum)
    