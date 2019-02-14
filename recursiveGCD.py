def recursiveGCD(number1,number2):
	if(number1==number2):
		return number1
	if(number1>number2):
		return recursiveGCD(number1-number2,number2)		
	return recursiveGCD(number1,number2-number1)

def main():
	number1,number2=input("Enter two numbers:")
	print(recursiveGCD(number1,number2))

if __name__=='__main__':
	main()
