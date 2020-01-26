wh = int(input("enter the wave height:"))
wl = int(input("enter the wave length:"))
string=input("enter the string:")
rep = rem = wh-1
for x in range(0,wh):
	cp = 0
	for y in range(0,len(string)):
		if(y%(rep*2)==rem or y%(rep*2)==rep+x):
			print(string[cp],end="")
		cp+=1
	rem-=1
print(ord('A'))
print(ord('a'))

