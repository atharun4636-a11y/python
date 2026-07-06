#a=int(input("enter a number: "))
#print(a)
'''a=int(input("num1:"))
b=int(input("num2:"))
c=a+b
print("result=",c)'''
#age=int(input("enter a age:"))
#print("my age is",age)
'''l=int(input("enter a lenght: "))
b=int(input("enter a berdth: "))
area=l*b
print("area of rectangle is",area)'''
'''a,b,c=map(int,input().split())
sum=a+b+c
average=sum//3
print("average of theree numbers",average)'''
'''r=int(input("enter a radius of circle:"))
area=3.14*r*r
print("area of circle is",area)'''
"""temp=int(input("enter a temperture in celisius:"))
F=(temp*9/5) + 32
print("farenheit vaule is",F)"""
'''centimeter=int(input("centimeter vaule:"))
meter=centimeter/100
print("meter vaule",meter)'''
'''p,r,t=map(int,input().split())
si=(p*r*t)//100
print("simple interst=",si)'''
'''num=int(input("enter a number:"))
square=num*num
print("square of number",square)'''
#num=int(input("enter a number;"))
'''if num%2==0:
    print("even number:")
else:
    print("odd number")'''
'''num=int(input("enter a number:"))
if num>0:
    print("positive number")
elif num<0:
    print("negative number")
else:
    print("number is zero")'''
'''age=int(input("enter a age:"))
if age>=18:
    print("vote is eligible")
else:
    print("vote is not eligible")'''
'''marks=int(input("enter a marks:"))
if marks>=35:
    print("pass")
else:
    print("fail")'''
#num1,num2=map(int,input().split())
'''if num1>num2:
    print("num1 is big number")
else:
    print("num2 is big number")'''
#marks=int(input("enter a marks:"))
'''if marks>=90:
    print("grade A")
elif marks>=75:
    print("grade B")
elif marks>=50:
    print("grader C")
else:
    print("fail")'''

'''num1,num2,num3=map(int,input().split())
if num1>num2 and num1>num3:
    print("num1 is greater number")
elif num2>num1 and num2>num3:
    print("num2 is greater number")
else:
    print("num3 is grater number")'''
'''num=int(input())
if num%5==0:
    print("number is divisible by 5")
else:
    print("the number is not divisible by 5")'''
'''num=int(input("enter a number:"))
if num % 5==0 and num % 11==0:
    print("the num is divisible by both 5 amd 11")
else:
    print("not divisible")'''
#year=int(input("enter a year:"))
'''if year % 4==0:
    print("leap year")
else:
    print("not a leap year")'''
'''L=input("enter a letter:")
vowels="aeiouAEIOU"
if L in vowels:
    print("the letter is vowel letter")
else:
    print("consonant")'''
'''num=input("enter a number:")
b=len(num)
if b==3:
    print("yes")
else:
    print("no")'''
'''temp=int(input())
if temp>30:
    print("hot")
else:
    print("normal")'''
'''n=int(input())
for i in range(5,0,-1):
    print(i)'''
'''n=int(input("enter a number:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)'''
'''count=0
for i  in range(1,101):
    if i % 2 !=0:
        count+=1
print(count)'''
'''n=int(input("enter a number"))
for i in range(1,n+1):
    if i>n:
        print(i)
        break
    else:
        print(n)
        break'''
'''for i in range(1,100):
        print(i*i)'''
'''n=int(input())
for i in range(1,n+1):
    print(i*i)'''
'''for i in range(1,100):
    if i>10 and i<20:
        print(i)'''
product=1
'''n=int(input("enter a number:"))
for i in range(1,n+1):
    product*=i
print(product)'''
'''even_count=0
odd_count=0
for i in range(1,101):
    if i % 2==0:
        even_count+=1
    else:
        odd_count+=1

count=even_count+odd_count
print(count)'''
even_sum=0
odd_sum=0
'''n=int(input())
for i in range(1,n+1):
    if i % 2==0:
        even_sum+=i
    else:
        odd_sum+=i
print(even_sum,odd_sum)'''
'''n=int(input())
a=1
for i in range(1,n+1):
    if i % 2 !=0:
        if i<a:
            a=i
print("smallest odd number is", a)'''

#i=10
#while i>=0:
        #print(i)
        #i-=1
count=0
i=1
while i<=100:
    if i % 2 ==0:
        count+=1
print(count)








