wh = int(input("enter the wave height:"))
str = input("enter the string")
rep = wh-1
rem=0
f = wh*2-2+1
for x in range(0,wh):
	for y in range(0,len(str)):
		if(y%(rep*2)==rem or y%(rep*2)==f):
			print(str[y],end="")
	f-=1
	rem+=1
