#!/usr/bin/env python3
infile = open('CAP.txt')
outfile = open('CAP.cvt','w')

testo=infile.readlines()

def replicate(c,a):
	s=""
	for i in range(0,a):
		s=s+c
	return s

k=0
for s in range (len(testo)):
	if (len(testo[s]) > 1):
		k=k+1
		m=0
		linea=""
		if (len(str(k))==1):
			nr=4
		if (len(str(k))==2):
			nr=3
		if (len(str(k))==3):
			nr=4
		if (len(str(k))==4):
			nr=1
		linea=linea + replicate(' ',nr) + str(k) +' '
		linea=linea + testo[s][0:5]+' '
		linea=linea + testo[s][6:9]+' '
		linea=linea + testo[s][10:12]+' '
		if (testo[s][13:17]=='    '):
			linea=linea + replicate('X',4)+' '
			m=1
		if (testo[s][13:15]=='  ' and m==0):
			linea=linea + replicate('X',2)+testo[s][15:17]+' '
			m=1
		if (testo[s][13:14]==' ' and m==0):
			linea=linea + replicate('X',1)+testo[s][14:17]+' '
			m=1
		if (m==0): 
			linea=linea + testo[s][13:17]+' '
		linea=linea + testo[s][18:]
		outfile.write(linea)

infile.close()
outfile.close()
print(k)
