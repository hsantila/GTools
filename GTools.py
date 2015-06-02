import numpy
def readframe(objectgro):

	line=objectgro.readline()
	
	if line == '':
		print "found an end of line"
		return None,None,None,None

	line=objectgro.readline()
	
	Natoms=int(line)
	i=0;
	
	xyz=numpy.zeros((Natoms,3))
	box=[0]*3
	types=[]
	
	while i<Natoms:
		line=objectgro.readline()
	
		parts=line.split()
		
		types.append(parts[1])
		xyz[i][0]=float(parts[3])
		xyz[i][1]=float(parts[4])
		xyz[i][2]=float(parts[5])
		
		i=i+1
	line=objectgro.readline()
	
	parts=line.split()
	box[0]=float(parts[0])
	box[1]=float(parts[1])
	box[2]=float(parts[2])
	return xyz,types,Natoms,box
