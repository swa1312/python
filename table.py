#! /usr/bin/python
print("This is at start point")
def main():
	inputNumber=input("Enter integer number");
	print("Using pass")
	for x in range(11):
		if(x==0):
			pass
		else:	
			print(inputNumber*x)
	print("Using two arguments in range()")
	for x in range(1,11):
		print(inputNumber*x)

if __name__=='__main__':
	main()
print("This is at end point")
