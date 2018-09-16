print('hello, this is a stastical calculator that is capable of carrying out complex and intrisic calculations, it is text based for now and requires you to input your answers to various questions asked')
#first ask if the user wants to continue with the program after he has read the agreement policy
choice_1 = str(input('would you like to continue?(yes/no):'))
#for the addition calculation
def addition():
    b = 0
    c = 0
    #this collects how many numbers will be added together
    amount = eval(input('how many numbers would you like to add?:'))
    #this is used to ensure the numbers dont exceed the amount you want to put in
    while b < amount:
        c += eval(input('enter a number:'))
        b += 1
    print('the sum of your',amount,'numbers is',c)
#for the subtraction calculation
def subtraction():
    b = 0
    amount = eval(input('how many numbers would you like to subtract?:'))
    c = eval(input('enter a number:'))
    while b < (amount-1):
        c -= eval(input('enter the next number:'))
        b += 1
    print('the final number is',c)
#for the multiplication calculation
def multiplication():
    b = 0
    amount = eval(input('how many numbers would you like to multiply?:'))
    c = eval(input('enter a number'))
    while b < (amount-1):
        c *= eval(input('enter the next number:'))
        b += 1
    print('the final answer is',c)
#for the division calculation
def division():
    num_1 = eval(input('enter the numerator:'))
    num_2 = eval(input('enter the denominator:'))
    a = num_1/num_2
    print('the final answer is',a)
#for the calculation of squareroot
def squareroot():
    import math
    a = eval(input('enter the number whose square root you want to find:'))
    b = math.sqrt(a)
    print('the square root of',a,'is',b)

def sine():
    import math
    a = eval(input('enter the number whose sine you want to find:'))
    b = math.sin(a)
    print('the sine of',a,'is',b,'degrees')
def cosine():
    import math
    a = eval(input('enter the number whose cosine you want to find:'))
    b = math.cos(a)
    print('the cosine of',a,'is',b,'degrees')
def tangent():
    import math
    a = eval(input('enter the number whose tangent you want to find:'))
    b = math.tan(a)
    print('the tangent of',a,'is',b,'degrees')    
def mean():
    b = 0
    c = 0
    amount = eval(input('how many numbers would you like to find their mean?:'))
    while b < amount:
        c += eval(input('enter a number:'))
        b += 1
    d = c/amount
    print('the mean of your',amount,'numbers is',d)
def mode():
    a=[]
    b=0
    amount = eval(input('how many numbers would you like to find their mode?:'))
    while b < amount:
        c = eval(input('enter a number:'))
        d =  a.append(c)
        b += 1
        a.sort()
    print(a[len(a)-1])
def median():
    import statistics
    a=[]
    b=0
    amount = int(input('how many numbers would you like to find their median?:'))
    while b < amount:
        c = int(input('enter a number:'))
        d =  a.append(c)
        b += 1
    e=statistics.median(a)
    print('the median is',e)
def variance():
    import statistics
    a=[]
    b=0
    amount = eval(input('how many numbers would you like to find their mode?:'))
    while b < amount:
        c = eval(input('enter a number:'))
        d =  a.append(c)
        b += 1
    e=statistics.variance(a)
    print('the variance is',e)
def standarddeviation():
    import statistics
    a=[]
    b=0
    amount = eval(input('how many numbers would you like to find their mode?:'))
    while b < amount:
        c = eval(input('enter a number:'))
        d =  a.append(c)
        b += 1
    e=statistics.pstdev(a)
    print('the standard deviation is',e)
def trapezium():
        a=eval(input('please enter the length of the top of the trapezium:'))
        b=eval(input('please enter the length of the bottom of the trapezium:'))
        c=eval(input('please enter the height of the trapezium:'))
        d=a+b
        e=c*d
        f=e/2
        print('the area of your trapezium is:',f)
def square():
        g=eval(input('enter the length of the squares side:'))
        h=g**2
        print('the area of your square is:',h)
        print('thats all for the square')
def cylinder():
        from math import pi
        i=eval(input('enter the height of your prefered cylinder:'))
        j=eval(input('enter the radius of the cylinder:'))
        k=j**2
        l=pi*k*i
        print('the area of your chosen cylinder is:',l)
def triangle():
        m=eval(input('enter the height of our preferred triangle:'))
        n=eval(input('enter the length of the base of the triangle:'))
        o=(m*n)/2
        print('the area of your triangle is:',o)






while choice_1=='yes':
    print('this is the code you are to use for this calculator: \n addition = a \n subtraction = b \n multiplication = c \n division = d \n squareroot = e \n sine = f \n cosine = g \n tangent = h \n mean = i \n mode = j \n median = k \n variance = l \n standard deviation = m \n area of trapezium = n \n area of square = o \n area of cylinder = p \n area of triangle = q')
    agn='yes'
    while agn=='yes':
        choice_2 = input('what equation would you like to carry out?:')
        if choice_2=='a':
                   print(\n addition())
                   agn=input('would you like to solve some other equation?(yes/no):')
        elif choice_2=='b':
                   subtraction()
                   agn=input('would you like to solve some other equation?(yes/no):')
        elif choice_2=='c':
                   multiplication()
                   agn=input('would you like to solve some other equation?(yes/no):')
        elif choice_2=='d':
                   division()
                   agn=input('would you like to solve some other equation?(yes/no):')
        elif choice_2=='e':
                   squareroot()
                   agn=input('would you like to solve some other equation?(yes/no):')
        elif choice_2=='f':
                   sine()
                   agn=input('would you like to solve some other equation?(yes/no):')
        elif choice_2=='g':
                   cosine()
                   agn=input('would you like to solve some other equation?(yes/no):')
        elif choice_2=='h':
                   tangent()
                   agn=input('would you like to solve some other equation?(yes/no):')
        elif choice_2=='i':
                   mean()
                   agn=input('would you like to solve some other equation?(yes/no):')
        elif choice_2=='j':
                   mode()
                   agn=input('would you like to solve some other equation?(yes/no):')
        elif choice_2=='k':
                   median()
                   agn=input('would you like to solve some other equation?(yes/no):')
        elif choice_2=='l':
                   variance()
                   agn=input('would you like to solve some other equation?(yes/no):')
        elif choice_2=='m':
                   standarddeviation()
                   agn=input('would you like to solve some other equation?(yes/no):')
        elif choice_2=='n':
                   trapezium()
                   agn=input('would you like to solve some other equation?(yes/no):')
        elif choice_2=='o':
                   square()
                   agn=input('would you like to solve some other equation?(yes/no):')
        elif choice_2=='p':
                   cylinder()
                   agn=input('would you like to solve some other equation?(yes/no):')
        elif choice_2=='q':
                   triangle()
                   agn=input('would you like to solve some other equation?(yes/no):')
        else:
            print('that is not a valid input')
            agn=input('would you like to solve some other equation?(yes/no):')
    

    
