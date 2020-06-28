'''
# DIVISIBLE BY 7 not BY 5

l=[]
for i in range(1,50):
	if (i%7==0) and (i%5!=0):
	  l.append(i)
print(l)

OUTPUT:
	[7, 14, 21, 28, 42, 49]

--------------------------------------------------------
#FACTORIAL

def fact(x):
	if x == 0:
		return 1
	else:
		return x*fact(x-1)

x = int(input("Enter no:"))
print (fact(x))


OUTPUT:
	Enter no:5
	120   
----------------------------------------------------------


#DICTIONARY

x = int(input("Enter the no:"))

d=dict()

for i in range(1,x+1):
	d[i]=i**3

print (d)

OUTPUT:
	Enter the no:6
	{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216}
-------------------------------------------------------

#LIST and TUPLES

values = input("Input some comma seprated numbers : ")
l = values.split(",")
t = tuple(l)
print('List : ',l)
print('Tuple : ',t)

OUTPUT:
	Input some comma seprated numbers:0,111,1212,123

List :  ['0', '111', '1212', '123']
Tuple :  ('0', '111', '1212', '123')

---------------------------------------------------------------


#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the #class methods.

class InputOutString():
	def __init__(self):
		self.s= ""
	
	def getString(self):
		self.s= input("Enter string:")
	
	def printString(self):
		print (self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()

#OUTPUT:
	#hitesh prajapati                            
	#HITESH PRAJAPATI

-----------------------------------------------------------------

#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.


import math

C=50
H=30
values=[]
numb= input("Enter numbers:").split(',')

for D in numb:
	values.append(str(int(round(math.sqrt((2*C*float(D)/H))))))
print(values)

OUTPUT:
	Enter numbers:100,150,180
	['18', '22', '24']

--------------------------------------------------------------


Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.



input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]

multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print (multilist)


# 2nd Method for Above problem

a=input('Enter the dimension:')
row,column=a.split(',')
row=int(row)
column=int(column)
print("Rows:",row,"Columns:",column)
c=[]
for i in range(row):
	t=[0]*column
	c.append(t)


for i in range(row):
	for j in range(column):
		c[i][j]=i*j
print(c)

#OUTPUT:
	#Rows: 3 Columns: 5
       # [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

------------------------------------------------------------------

#ARRANGE THE STRING IN ASCENDING ORDER
words=[]
sttr = input('Enter the string:').split(',')
for i in sttr:
		words.append(i)

words.sort()
print(words)


OUTPUT:
	Enter the string:hitesh,shubham,ketan,sanya,ajay
	['ajay', 'hitesh', 'ketan', 'sanya', 'shubham']


y=input("Enter strings:").split(',')
for items in y:
	items.sort()
	print (','.join(items))


#3RD Program

x=input('Enter strings:').split(',')
x.sort()
print(x)

--------------------------------------------------------------------

st=[]

x= input('Enter the string:')
for i in x:
	st.append(i.upper())

for sent in st:
	print (sent,end='')  #end='' horizantal output
print('\n')

#OUTPUT:
	#Enter the string:hi how are you
	#HI HOW ARE YOU


-------------------------------------------------------------------



#SORT THE STRING AND REMOVE BRACKETS OF THE LIST

words=[]
sttr = input('Enter the string:').split(',')
for i in sttr:
		words.append(i)

words.sort()
print(*words, sep=',' )


#OUTPUT:
	#Enter the string:hitesh,aman,you,tut
	#aman,hitesh,tut,you

--------------------------------------------------------------------------------

#SORT THE STRING WITHOUT REPETATION ON WORd


x = input("Enter the string:").split(" ")
y=[]
for i in x:
	y.append(i)

sortt= sorted(list(set(y)))	
print (*sortt)


#OUTPUT: 
	#Enter the string:
	#hello world and practise makes perfect and hello world again
	#again and hello makes perfect practise world


n = input('Enter the numbers of candles:')


l = map(int,input("Height of candles:").strip().split(' '))
print l.count(max(l))

-------------------------------------------------------------------------------


def find_candles(n):

	inputs = []
	for x in range(n):
 	   inputs.append(input("Height of candles {}:\n".format(x+1)))
	print ("The no of candle Richa blowed out \n",inputs.count(max(inputs)))

n = int(input("Numbers of candles: "))

find_candles(n)



'''


