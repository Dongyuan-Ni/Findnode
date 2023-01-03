import os
import numpy as np

gap_tol = float(input('Input the gap tolerance:'))
Ef = float(os.popen('grep E-fermi OUTCAR').read().split()[2])

with open('IBZKPT', 'r') as f:
	f.readline()
	nkpts_scf = int(f.readline())

data = []

with open('EIGENVAL', 'r') as f:
	for i in range(5):
		f.readline()
	number = [int(i) for i in f.readline().split()]
	nelectrons = number[0]
	noccupancy = int(nelectrons)
	nkpts = number[1]
	nbnds = number[2]
	f.readline()
	for i in range(nkpts_scf):
		for j in range(nbnds+2):
			f.readline()

	for i in range(nkpts - nkpts_scf):
		kpoint_coord = '    '.join(f.readline().split()[:3])
		for j in range(noccupancy - 1):
			f.readline()
		Evb1 = float(f.readline().split()[1]) - Ef
		Ecb1 = float(f.readline().split()[1]) - Ef
		gap = Ecb1 - Evb1
		#if gap < gap_tol:
		#	data.append(kpoint_coord + ' ' + str(gap) + '\n')	

		for j in range(nbnds - noccupancy - 1):
			f.readline()
		if i != nkpts - nkpts_scf - 1:
			f.readline()
		else:
			pass

with open('k-positions.dat', 'w') as f:
	f.writelines(data)
