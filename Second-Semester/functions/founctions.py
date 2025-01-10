# Functions
# organized code blocks that allow for modularity and resue in our programs
# function signiture 


def happy(name):
    print("Happy brithday to " + name + "!")

def add(x,y):
    print(x)
    return x + y

def printadd(x,y):
    print(x+y)

def check_num(x):
    if x % 2 == 0:
        return True
    if x % 5 == 0:
        return False


def main():
    print("Happy birthday to John!")
    print("Happy Birthday to Paul!")
    print("Happy brithday to ...")
    happy("Jonas")
    print(add(4, 5))
    printadd(4,5)
    sum = printadd(4,5)
    print(sum)
    sum = add(4,5)
    print(sum)



    print(check_num(2))
    print(check_num(5))
    print(check_num(10))


    x = add(4,5)
    print(x)


if __name__ == "__main__":
    main()
