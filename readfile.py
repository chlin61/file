#read file
data =[]
count = 0
with open('reviews.txt','r') as f:   #  with  只要離開with架構  將會自動關閉open
	for line in f:
		##print(line.strip()) ##.strip() 去調換行符號
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(count)
print(len(data))

print(data[0])