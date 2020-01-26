n = int(input("enter the number:"))
e=n
r=0
while(n!=0):
	a=n%10
	r=r+a*a*a
	n=n//10
if(e==r):
	print("sucess")
else:
	print("no problem")
