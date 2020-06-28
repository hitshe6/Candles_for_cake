
#Candles on cake using function

def find_candles(n):

	inputs = []
	for x in range(n):
 	   inputs.append(input("Height of candles {}:\n".format(x+1)))
	print ("The no of candle Richa blowed out \n",inputs.count(max(inputs)))

n = int(input("Numbers of candles: "))

find_candles(n)





