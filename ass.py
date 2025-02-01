#import dis
#def add(a,b):
 #   sum=a+b
  #  return sum
#res=add(10,20) 
#print(res)          
        

#l=5
#b=6
#rectangle=l*b
#print(f'Area of a rectangle: {rectangle}')
l=int(input("enter length"))
b=int(input("enter breadth"))
print("Area of rectangle is :",l*b)

#*****2****#

username="manju"
psswrd=1011
u=input("enter username:")
p=input("enter passowrd:")
if u == username and p == str(psswrd):
    print("login success")
else:
    print("invalid")

 #*****3****#

Num = int(input("Enter the number: ")) 
if Num > 1:
    for i in range(2, int(Num ** 0.5) + 1): 
        if Num % i == 0:
            print("Not a prime number")
            break
    else: 
        print("Prime number")
else:
    print("Not a prime number")
     

     #********4********#
username="manju"
psswrd=1011
attempt=0

while attempt <3 :
    u=input("enter username:")
    p=int(input("enter password:"))
    if u==username and p==psswrd:
        print("Login succes!")
        break
    else:
        print("ivalid")
        attempt +=1
if attempt == 3:
    print("try later again")    



    #**************5************#


tc = int(input("Enter the total number of classes : "))
ac = int(input("Enter the number of classes you attended: "))
attendance_percentage = (ac / tc) * 100

if attendance_percentage >= 75:
    print(f"Eligible for exam .")
else:
    print(f"Not eligible for exam")







    

