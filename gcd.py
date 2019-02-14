def gcd(number1,number2):
	while(number1!=number2):
		if(number1>number2):
			number1=number1-number2
		else:
			number2=number2-number1
	return number1
def main():
	number1,number2=input("Enter number1, number2 : ")
	print(gcd(number1,number2))
if __name__=='__main__':
	main()
