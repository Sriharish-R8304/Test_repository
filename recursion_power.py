def pwr(x, y):
	if y == 1:
		return x
	else:
		return x * pwr(x, y - 1) 
x = int(input('Enter a number:'))
y = int(input('Enter the power of the number:'))

print(pwr(x, y))