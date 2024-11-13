import fileinput

def main():
    file1 = open("accounts", "a")
    file2 = open("balances","a")
    check = True
    while check == True:
        newaccount = input("input your account ")
        newbalance = input("input your balance ")
        file1.write("\n" + newaccount)
        file2.write("\n" + newbalance)
        option = int(input("exit? "))
        if option == 1:
            check == False

    accounts = []
    balances = []

    file1.close()
    file2.close()


    for line in fileinput.input("accounts"):
        accounts.append(line.strip())

    for line in fileinput.input("balances"):
        blaances.append(line.strip())

    print(accounts)
    print(blaances)



if __name__ == "__main__":
     main()