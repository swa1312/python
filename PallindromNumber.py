#!/usr/bin/python
#WAP to accept number from user and check if it is pallindrom or not
inputNumber=input("Enter integer : ")
def pallindromNumber(inputNumber):
        reverseNumber=0;
	tmp=inputNumber;
        while(tmp>0):
                reverseNumber=(reverseNumber*10)+(tmp%10)
                tmp=(tmp/10)
        if(inputNumber==reverseNumber):
		print("Number is pallindrom")
	else:
		print("Number is not pallindrom")

if __name__=='__main__':
        pallindromNumber(inputNumber)

