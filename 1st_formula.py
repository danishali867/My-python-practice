# string1=input("enter one chracter=")
# string2=input("enter 2nd number=")

# string1

# test=string1==string2
# print("test the number are equal=",test)



a=int(input("enter the value of a= "))
b=int(input("enter the value of b= "))
print("-------------------Now finding the LHS-----------------")
#LHS= (a+b)*2
lhs=(a+b)*(a+b)
print("The LHS = ", lhs)
print("-------------------Now finding the RHS-----------------")
#RHS= (a*a)+(b*b)+2(a)(b)
rhs=(a*a)+(b*b)+2*(a)*(b)
print("The RHS=",rhs)
equal= lhs==rhs
print(equal)
