# Question 1
print('Hello World')
n = int(input('Enter a number : '))
print(n)
print(type(n))



# Question 2
n = int(input('Enter the number of students : '))
l = []
for i in range(0, n):
    ele = int(input())
    l.append(ele)
print(l)
print('Maximum : ',max(l))
print('Minimum : ',min(l))
avg = sum(l)/len(l)
print('Average : ',avg)


# Question 3
n = int(input('Enter the number of students : '))
s = int(input('Enter the number of subjects : '))
l=[]
for i in range(0, n):
    temp = []
    print('Enter the marks of student ',i+1)
    for j in range(0,s):
        nu = int(input())
        temp.append(nu)
    l.append(temp)
print(l)
for i in range(0, n):
    print('Sum of marks of student ',i+1,': ', sum(l[i]))
    print('Average marks : ',sum(l[i])/len(l[i]))



# Question 4
n = int(input('Enter the number of employees : '))
print('Enter their basic salary : ')
sal = []
tot =[]
for i in range(0, n):
    t = int(input())
    sal.append(t)
    if(t<=10000):
        to = t + 0.2*t + 0.8*t
        tot.append(to)
    elif(t<=20000):
        to = t + 0.25*t + 0.85*t
        tot.append(to)
    else:
        to = t + 0.3*t + 0.9*t
        tot.append(to)
print(sal)
print(tot)


# Question 5
import re as r
while(True):
    pswd = input('Enter a valid password : ')
    flag = True
    if(len(pswd)<8):
        flag = False
    elif(len(pswd) > 16):
        flag = False
    elif not r.search("[a-z]",pswd):
        flag = False
    elif not r.search("[A-Z]",pswd):
        flag = False
    elif not r.search("[0-9]",pswd):
        flag = False
    elif not r.search("[$@#]",pswd):
        flag = False
    if(flag):
        print('Valid Password')
        break
    else :
        print('Invalid Password')


# Question 6
import random as ran
import sympy
l = []
for i in range (100):
    n = ran.randint(100, 900)
    l.append(n)
print(l)
odd = []
even = []
prime = []
for i in range(0, len(l)):
    if(l[i]%2 == 0):
        even.append(l[i])
    else:
        odd.append(l[i])
    if(sympy.isprime(l[i])):
        prime.append(l[i])
print(odd)
print(even)
print(prime)