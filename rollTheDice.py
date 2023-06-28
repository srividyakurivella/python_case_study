import random
d=[1,2,3,4,5,6]
min_value=1
max_value=6
con="yes"
while(con[0]=='y' or con[0]=='Y'):
    d1=random.randint(min_value,max_value)
    d2=random.choice(d)
    print("The value on top of dice are:",d1,",",d2)
    con=input("Enter \"yes\" or \"y\" to continue rolling the dice or else enter no.....")
print("***Thank you***")