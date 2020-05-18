for a in range(1,101):
	if a % 7 == 0:
		continue
	if (a - 7) % 10 ==0:
		continue
	if  a >=70 and a <= 79:
		continue
	print(a) 
