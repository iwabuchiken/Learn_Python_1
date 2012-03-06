import os
import sys

def get_path():
	### variables ###
	path_original		= os.getcwd()
	p1						= path_original.split("\\")
	p2						= r"C:\WORKS".split("\\")
	p3						= list()
	i						= 0	# index for p1
	j						= 0	# index for p2
	### processes ###
	# reverse
	p1.reverse()
	p2.reverse()
	print p1
	print p2
	# compare and generate
	for i in range(len(p1)):
		if (p2[0] == p1[i]):
			#p3.append(p2[i])
			p3.append(".")
			break
		else:
			p3.append(p1[i])	
	#//for
	
	# show
	print "p3=", p3
	p3.reverse()
	print "p3=", p3
	print "p3=", "/".join(p3)
	
#//get_path()

if __name__ == '__main__':
	get_path()