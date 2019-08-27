"""
This program generates dataset for the machine learning model used in this project.

:author: Hitesh Vaidya
"""

import numpy as np
import math
import csv

def generatePrintBinary(n): 
      
    # Create an empty queue 
    from Queue import Queue 
    q = Queue() 
    numbers = []
      
    # Enqueu the first binary number 
    q.put("1") 
  
    # This loop is like BFS of a tree with 1 as root 
    # 0 as left child and 1 as right child and so on 
    while(n>0): 
        n-= 1 
        # Print the front of queue 
        s1 = q.get()  
        # print s1
        numbers.append(s1)
      
        s2 = s1 # Store s1 before changing it 
      
        # Append "0" to s1 and enqueue it 
        q.put(s1+"0") 
  
        # Append "1" to s2 and enqueue it. Note that s2 
        # contains the previous front 
        q.put(s2+"1")
    return numbers

def main():
	numbers = generatePrintBinary(math.pow(2,10)-1)
	vectors = []
	# print "main function"
	for index in numbers:
		# temp = index.split()
		num = ''
		while len(index) < 10:
			index = '0' + index
		num = [int(x) for x in index]
		vectors.append(num)
		# if len(vectors)%500:
		# 	print vectors[-1]
	vectors.insert(0, [0 for x in range(10)])
	print "number of vectors = " + str(len(vectors))
	print '\nfinal data\n'
	data = []
	for index in range(1, 29):
		count = 0
		for combo in vectors:
			temp = [x for x in combo]
			temp.append(index)
			data.append(temp)
			count += 1
		print "data size = " + str(len(data)) + ";	rise = " + str(count)
			# print 'after -> ' + str(data[np.random.randint(0, len(data))])
	print '\nfinal'
	print 'len = ' + str(len(data))
	for index in range(10):
		print str(-1*index) + '. ' + str(data[-index])

	with open('random.csv', 'w') as csvfile:
		fp = csv.writer(csvfile)
		for index in data:
			fp.writerow(index)

if __name__ == '__main__':
	main()