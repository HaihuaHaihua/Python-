import io
import numpy as np

def boomSort(source):
	length = len(source)
	for i in range(length):
		j = i+1
		for j in range(length):
			temp = 0
			if(source[i]<source[j]):
				temp = source[i]
				source[i] = source[j]
				source[j] = temp
     
def selectSort(source):
	length = len(source)
	for i in range(length):
		minvalue = source[i]
		for j in range(i,length):
			if(source[j]<minvalue):
				minvalue = source[j]
				temp = source[j]
				source[j] = source[i]
				source[i] = temp

# def yuesefu(n):
# 	# people = np.array((1,n+1),dtype=int)
# 	people = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
# 	index = 0
# 	for i in range(n):
# 		count = 0
# 		while count < 3:
# 			if people[index] != 0:
# 				count += 1
# 			if count == 3:
# 				print(people[index],"dead")
# 				people[index] = 0
# 			index = (index+1) % n
# 	print(people)


def yuesefu():
	n = 17
	survive = list(range(1,n+1))
	count = 3
	temp = 1
	roun = 0
	kill = []
	while(roun < 10):
		for i in survive:
			print(i,end=' ')
			if temp == count:
				kill.append(i)
				survive.remove(i)
				temp = 1
				print("kill person ",i)
			temp +=1
		roun +=1
	print(kill)
	print(survive)

def main():
	source = [8,4,1,6,3,2,1]
	source2 = [3,7,8,4,1,6,3,2,1]
	print(source)
	boomSort(source)
	print(source)
	print(source2)
	selectSort(source2)
	print(source2)
	# yuesefu(17)
	yuesefu()


if __name__ == "__main__":
	main()			