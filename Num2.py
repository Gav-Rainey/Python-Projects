def fib(num):
    x, y = 0, 1

    for x in (range(0, num)):
        x, y = y, x + y
    print("Number: " + str(x))


def main():
    runs = int(input("Select what stage of the fibonacci sequence you would like to see\n"))
    fib(runs)


main()
