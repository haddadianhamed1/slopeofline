import itertools
from itertools import combinations
def slope(x1,x2,y1,y2):
	a = [[y1-x1, y2-x2]]
#	print a
	m= []
	for x, y in a:
#		print x,y
		m.append(x/y)
#	print m
	return m
def main():


	points= [[1,3],[4,7],[3,12]]

	for (x1,x2),(y1,y2) in combinations(points,2):
		x = slope(x1,x2,y1,y2)
		print x



if __name__ == "__main__":
        main()
