
while True:
    # Program make a simple calculator

    # This function adds two numbers
    def add(x, y):
        return (x+y)

    # This function subtracts two numbers
    def subtract(x, y):
        return (x-y)

    # This function multiplies two numbers
    def multiply(x, y):
        return (x*y)
    # This function divides two numbers

    def divide(x, y):
        return (x/y)


    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    # take input from the user
    choice=int(input("Enter choice(1/2/3/4): "))
    x=int(input("enter value 1"))
    y=int(input("enter value 2"))
    if choice==1:
        print(add(x,y))
    elif choice==2:
        print(subtract(x,y))
    elif choice==3:
        print(multiply(x,y))
    elif choice==4:
        print(divide(x,y))
    else:
        print("kk")
