# n=open("text.txt",'r')
# print(n.read())

# y=open("text.txt",'w')

# print(y.write("my name is Dipta"))

#x=open("tt.txt",'x')

# import os
# os.remove("tt.txt")
# os.rmdir("new1")

# try:
#     print(n)

# except:
#     print("n is don't here")


# try:
#     number=int(input('enter your number:'))
#     print("number:",number)
# except ValueError:
#     print("wrong input please valid input")

# finally:
#     print("thank you")
   

# def countdown(n):  # recursive function
#     if n==0:
#         print("time up")
#     else:
#         print(n)
#         countdown(n-1)
# countdown(5)

# def num(n):
#     if n==0:
#         return
#     num(n-1)
#     print(n)  # print the number

# num(5)
    
## fibonnaci
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
for i in range(10):
    print(fibo(i),end=" ")


