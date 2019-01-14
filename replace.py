inputstring=(input("Enter String : "))
tobereplace=inputstring[:1]
substring=inputstring[1::]
endstring=substring.replace(tobereplace,'*',)
result=tobereplace+endstring
print("Result is : "+str(result))
