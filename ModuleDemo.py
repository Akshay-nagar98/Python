import UDF

while True:
    print("*"*50)
    print("1.OddEven")
    print("2.Maxoftwo")
    print("3.Exit")

    choice=int(input("Enter Your Choice : "))


    if choice==1:
        n1=int(input("Enter Number : "))
        UDF.oddeven(n1)
        print("*"*50)
    elif choice==2:
        n1=int(input("Enter Number : "))
        n2=int(input("Enter Number : "))
        UDF.maxoftwo(n1,n2)
        print("*"*50)
    elif choice==3:
        print("Thank you")
        print("*"*50)
        break
    else:
        print("Invalid Choice. Please Try Again.")
        print("*"*50)
        
