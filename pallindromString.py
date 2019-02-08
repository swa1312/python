#!usr/bin/python
inputString=input("Enter any String to check pallindrom or not :")
def pallindrom(inputString):
	if(inputString==inputString[::-1]):
		print("String is pallindrom")
	else:
		print("String is not pallindrom")

if __name__=='__main__':
	pallindrom(inputString)
