import os

if os.path.isfile('products.csv'):
	print('yes')
else:
	print('no')


products =[]

with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f: 
		if 'name, price' in line:
			continue
		s = line.strip().split(',')
		print(s)


while True:
	name= input('name of the product: ')
	if name =='q':
		break
	price= input ('price of the product: ')
	products.append([name, price])
print(products)

for p in products:  
	print(p[0], 'price is ', p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('name, price\n')
	for p in products:
		f.write(p[0] + ',' + (p[1]) + '\n')