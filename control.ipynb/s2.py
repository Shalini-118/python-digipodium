str='digipodium'
print('str[0]=',str[0])
print('str[1]=',str[1])
print('str[2]=',str[-2])
print('str[3]=',str[3])
print('str[4]=',str[4])
#getting a SLICE
slice1= str[4:7] #starting from 4 indexing and stopping point is 7
print(slice1)
slice2=str[0:4]
print(slice2)
slice3=str[:3]
print(slice3)
slice4=str[:-3]
print(slice4)
slice5=str[4:len(str)]
print(slice5)
slice6=str[4:]
print(slice5)
slice7=str[:-4]
print(slice7)

#builtin function for string
str=chr(65)
print(str)
str=chr(2365)
print(str)
str=chr(12365)
print(str)
