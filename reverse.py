a=int(input("enter the number a"))
while(a>0):
    rev=0
    digit=a%10
    rev=rev*10+digit
    a=a//10
    print(rev)