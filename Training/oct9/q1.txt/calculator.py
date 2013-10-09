def calculator():
    choice=0
    while (choice!=5):
        print "1.Addition"
        print "2.Subtraction"
        print "3.Multiplication"
        print "4.Division"
        print "5.Exit"
        choice = raw_input("enter your choice:")
        if choice == "1":
            add()

        elif choice == "2":
            sub()

        elif choice == "3":
            mult()

        elif choice == "4":
            div()

        elif choice == "5":
            exit(0)

def add():
    print "enter two no"
    a = int(raw_input("enter a:"))
    b = int(raw_input("enter b:"))
    c = a + b
    print c

def sub():
    print "enter two no"
    a = int(raw_input("enter a:"))
    b = int(raw_input("enter b:"))
    c = a - b
    print c

def mult():
    print "enter two no"
    a = int(raw_input("enter a:"))
    b = int(raw_input("enter b:"))
    c = a * b
    print c

def div():
    print "enter two no"
    a = float(raw_input("enter a:"))
    b = float(raw_input("enter b:"))
    c = a / b
    print c
if __name__ == '__main__':
    calculator()


    

