def readConfFile(inputfilename):
	fd=open(inputfilename)
	confDict=dict()
	word=''
	line=fd.readline()
	while(line!=''):
		if(line[:1]!='#'):
			
		print(firstPart)
		print(secondPart)
		line=fd.readline()

def main():
	inputfilename=input("Enter file name")
	readConfFile(inputfilename)

if __name__=='__main__':
	main()
	

