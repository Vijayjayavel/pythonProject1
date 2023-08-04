# not yet completed

# itsssssssssssssss a practice desk

x=int(input('Enter a number: '))
y=int(input('Enter a second input: '))

if x>y:
    z=divmod(x,y)
    if z[1] == 0:
        print(f'Lcm of {x} and {y} is ' + str(x))
    else:
        for i in range(1,y+1):
            if (i*x)%(y/2)==0:
                a=i*x
                print(f'(Lcm of {x} and {y} is ')
                print(a)
else:
    z=divmod(y,x)
    if z[1] == 0:
        print(f'Lcm of {x} and {y} is ' + str(y))
    else:
        for i in range(1,x+1):
            if (i*y)%(x/2)==0:
                a=i*y
                print(f'(Lcm of {x} and {y} is ')
                print(a)


