def swapDiffBits(x,y,x_position,y_position,bits):
	mask=(1<<bits)-1
	x_mask=mask<<(x_position-bits)
	y_mask=mask<<(y_position-bits)
	x_part=x & mask
	y_part=y & mask
	if x_position > y_position:
		x_part=x_part>>(x_position-y_position)
		y_part=y_part<<(x_position-y_position)
	else:
		x_part=x_part<<(y_position-x_position)
		y_part=y_part>>(y_position-x_position)
	x=x & ~ x_mask
	y=y & ~ y_mask
	x=x | y_part
	y=y | x_part	
	return x,y

def main():
	x,y,x_position,y_position,bits=input("Enter x,y,x_position,y_position,bits")
	print(swapDiffBits(x,y,x_position,y_position,bits))

if __name__=='__main__':
	main()
