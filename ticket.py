import random
print("***Railway Ticket booking Website***")
print("1.Ticket Booking\n2. Check PNR Status\n3.Exit from the Website")
restart="Y"
name = []
age = []
sex = []
t1 = []
while 1:


    ch=int(input("Enter ur choice"))
    if ch==1:
        print("Enter no.of Persons:")
        p = int(input())
        for i in range(p):
            name1 = input("Enter Name:")
            name.append(name1)
            age1 = int(input("Enter Age:"))
            age.append(age1)
            sex1 = input("Enter Sex:")
            sex.append(sex1)
            u = random.randint(1000, 30000)
            t1.append(u)
            print()


        x = 0
        print("Ticket Details")
        print("\nTotal No.of Tickets : ", p)
        for i in range(1,p + 1):

            print("\nTicket Number:", t1[x])
            print("Name : ", name[x])
            print("Age  : ", age[x])
            print("Sex : ", sex[x])
            print()
            x = +1
        print("***Happy Journey***")
    elif ch==2:

        print("Enter ticket number:")
        t = int(input())
        y = 0
        if t in t1:
            print("Successfully Registered")
        else:
            print("Not Found")

    elif ch==3:
        exit()



