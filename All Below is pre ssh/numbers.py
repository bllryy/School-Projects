"""
Name: ---------- (cause its on github ( ͡° ͜ʖ ͡°))
Section: 275-02
Desc: Lab2
"""



def main():
    vars = []
    vars.append(int(input("Enter 1 number: ")))
    vars.append(int(input("Enter 2 number: ")))
    vars.append(int(input("Enter 3 number: ")))
    vars.append(int(input("Enter 4 number: ")))
    vars.append(int(input("Enter 5 number: ")))
    vars.append(int(input("Enter 6 number: ")))
    vars.append(int(input("Enter 7 number: ")))
    vars.append(int(input("Enter 8 number: ")))

    sum1 = vars[0] + vars[1] 
    sum2 = vars[2] - vars[3]
    sum3 = vars[4] * vars[5]
    sum4 = vars[6] / vars[7]

    print("your sum is: "  + str(sum1))
    print("your sum is: "  + str(sum2))
    print("your sum is: "  + str(sum3))
    print("your sum is: "  + str(sum4))




# need for full credit
if __name__ == "__main__":
    main()



# type: ignore #var1 = 
    #var2 = int(input("please input ur number "))
    #var3 = int(input("please input ur number "))
    #var4 = int(input("please input ur number "))