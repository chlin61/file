products=[]
while True:
	name = input('請輸入name')
	if name == 'q':
		break
	price = input('price')
	products.append([name,price])
print(products)

with open('products.csv','w',encoding='utf-8') as f:
	for p in products:
		f.write(p[0] + ':' + p[1] + '\n')