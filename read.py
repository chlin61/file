import os

#讀取檔案
products =[]
if os.path.isfile('products.txt'):
	print('已讀取到檔案')
	with open('products.txt','r',encoding='utf-8') as f:
		for line in f:
			if '產品,價格' in line:
				continue
			products.append([line.strip().split(',')])
	print(products)
else:
	print('找不到檔案')

#寫入檔案
while True:
	name = input('請輸入欲輸入的產品名稱 :(q離開)')
	if name =='q':
		break
	price = input('請輸入' + name + '的產品價格:')
	products.append([name, price])

with open('products.txt','w',encoding='utf-8') as f:
	f.write('產品,價格\n')
	for p in products:
		f.write(str(p[0]) + ',' + str(p[1]) + '\n')
