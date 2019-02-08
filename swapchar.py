#WAP to swap first two char of two strings.
firstString=input("Enter first String")
secondString=input("Enter seconda String")
firsttwo=firstString[:2]
remainfirst=firstString[2:]
secondtwo=secondString[:2]
remainsecond=secondString[2:]
newFirst=secondtwo+remainfirst
newSecond=firsttwo+remainsecond
print("Swapped char string : "+newFirst+" & "+newSecond)
