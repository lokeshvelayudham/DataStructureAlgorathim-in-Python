#code is contributed by Lokesh Poluru Velayudham


while True:
    choice = int(input())

    if choice == 1:
        n1 = float(input())
        n2 = float(input())
        sum = n1 + n2
        print(int(sum))

    elif choice == 2:
        n1 = float(input())
        n2 = float(input())
        diff = n1 - n2
        print(int(diff))

    elif choice == 3:
        n1 = float(input())
        n2 = float(input())
        prod = n1 * n2
        print(int(prod))

    elif choice == 4:
        n1 = float(input())
        n2 = float(input())
        div = n1 / n2
        print(int(div))

    elif choice == 5:
        n1 = float(input())
        n2 = float(input())
        mod = n1 % n2
        print(int(mod))

    elif choice == 6:
        break

    else:
        print("Invalid Operation")
