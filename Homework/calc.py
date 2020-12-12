a=int(input('a= '))
b=int(input('b= '))
print('Enter action number: 1)+ 2)- 3)* 4)/')
c=int(input())
if c == 1:
	print(a+b)
elif c==2:
	print(a-b)
elif c==3:
	print(a*b)
elif c==4:
	print(a/b)
else:
	print('Error')