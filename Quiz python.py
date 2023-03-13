# write a program that asks the user to enter his or her name
def hello():
    name=str(input("enter the name : "))
    print("hello " + str(name))
    return
hello()

#write a progarm that asks the user to enter the width and length of room

width =float(input("please enter the width"))
length =float(input("please enter the length"))
area= width*length
print("the area is {}".format(area))

#create a program that reads the length and width of a farmer's field from the user
#in feel

length_width = 43.460
your= f"There are {length_width} square in an acre."
print(your)

#write a program that reads positive int
n=int(input("please enter the n: "))
sum=(n/2)*(n+1)
print (" the sum is ",sum)
