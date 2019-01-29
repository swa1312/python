#WAP which contains add, substract, multiply and divide operation with two argumets each.
#! /usr/bin/python

a=input("Enter number 1")
b=input("Enter number 2")
def add(a,b):
	return(a+b)
def substract(a,b):
	return(a-b)
def multiply(a,b):
	return(a*b)
def divide(a,b):
	return(a/b)

if __name__=='__main__':
	print(add(a,b))
	print(substract(a,b))
	print(multiply(a,b))
	print(divide(a,b))

