# a=int(input("Enter 1 no."))
# b=int(input("Enter 2 no."))
# c=a+b
# addition=c
# print("On addition answer is=",c)
# d=a-b
# subtraction=d
# if d>=0:
#     print("On subtraction answer will be positive A is greater than B=",d)
# else:
#     print("On subtraction Answer will be negative as B is greater than A=",d)
# e=a*b
# if e==0:
#  print("Either A or B one is zero")
# else:
#    print("On multiplication Answer is=",e)
# f=a/b
# print("On dividing A by B answer is=",f)



while True:
    a=input("Enter symbol for cal.")
    b=int(input("enter 1 no"))
    c=int(input("enter 2 no"))
    if a=="+":
     print(b+c)
    elif a=="-":
     print(b-c)
    elif a=="*":
     print(b*c)
    elif a=="/":
     print(b/c)
    else:
     print("invalid")