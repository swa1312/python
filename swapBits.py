def swapBits(x,y,position,bits):
	mask=( 1<<bits)-1
	mask=mask<<(position-bits)
	x_part=x&mask
	y_part=y&mask
	x=x&~mask
	y=y&~mask
	x=x|y_part
	y=y|x_part
	return x,y

def main():
	x=input("Enter first number")
	y=input("Enter second number")
	position=input("Enter positions")
	bits=input("Enter number of bits")
	print(swapBits(x,y,position,bits))

if __name__=='__main__':
	main()
