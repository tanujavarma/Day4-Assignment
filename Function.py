def fact(num):
    if num<0:
        print("factorial don't exist") 
    elif num==0:
        return 1
    else:
        return num*fact(num-1)
num=int(input("enter number"))
print(fact(num))
