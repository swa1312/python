def recStringLenth(inputString):
	if(inputString==''):
		return 0
	else:
		return 1+recStringLenth(inputString[1:])

def main():
	inputString=input("Enter String")
	print(recStringLenth(inputString))
if __name__=='__main__':
	main()
