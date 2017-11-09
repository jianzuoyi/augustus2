#!/usr/bin/env python

import sys, re, os

def identity(db, solar, pepdb):
	q = []
	for line in solar:
		each = line.strip().split()
		match = 0
		total = 0
		for position in each[11].split(';')[:-1]:
			start = position.split(',')[0]
			end = position.split(',')[1]
			id = '-'.join([each[0], each[5], start, end])
			match += db[id]*(int(end) - int(start) + 1)
			total += int(end) - int(start) + 1
		Identity = 1.0*match/total
		Coverage = coverage(pepdb, each[11], each[0])
		if Identity >= 45 and each[10] >= 25 and Coverage > 0.5:
			q.append(each[0])
	return q

def merge(nrset, uniset):
	final = list(set(nrset) | set(uniset))
	with open('with_hits_ID.out', 'w') as out:
		out.write('\n'.join(final))
	return final

def withouthist(pepid, pepdb, matchid):
	q = []
	with open('without_hits_ID.out', 'w') as out1:
		final = list(set(pepid) - set(matchid))
		out1.write('\n'.join(final))
	with open('without_hits_ID_gl50.out', 'w') as out2:
		for each in final:
			if pepdb[each] > 50:
				q.append(each)
		out2.write('\n'.join(q))

def coverage(pepdb, region, id):
	regions = sorted(region.split(';')[:-1], key = lambda x : int(x.split(',')[0]))
	new_region = []
	fs = int(regions[0].split(',')[0])
	fe = int(regions[0].split(',')[1])
	for n in range(1, len(regions)):
		rs = int(regions[n].split(',')[0])
		re = int(regions[n].split(',')[1])
		if rs <= fe < re:
			fe = re
		elif fe >= re:
			continue
		else:
			new_region.append((fs, fe))
			fs = rs
			fe = re
	new_region.append((fs, fe))
	length = 0
	for i in new_region:
		length += i[1] - i[0] + 1
	coverage = 1.0*length/pepdb[id]
	return coverage
	
def pepdb(all):
	fasta = {}
	blocks = all.strip().split('>')
	for block in blocks[1:]:
		lines = block.strip().split('\n')
		id = lines[0].strip().split()[0]
		seq = ''.join(lines[1:])
		num = len(seq)
		fasta[id] = num
	ID = fasta.keys()
	return fasta, ID

def mkdb(blast):
	q = {}
	for line in blast:
		each = line.strip().split()
		id = '-'.join([each[0], each[1], each[6], each[7]])
		q[id] = float(each[2])
	return q

def main():
	with open(sys.argv[1], 'r') as file1:
		pdb, pepid = pepdb(file1.read())
	with open(sys.argv[2], 'r') as blast_nr, open(sys.argv[3], 'r') as blast_uni: #blast
		dbnr = mkdb(blast_nr); dbuni = mkdb(blast_uni)
	with open(sys.argv[4], 'r') as solar_nr, open(sys.argv[5]) as solar_uni: #solar
		hist_nr = identity(dbnr, solar_nr, pdb)
		hist_uni = identity(dbuni, solar_uni, pdb)
		hist = merge(hist_nr, hist_uni)
		withouthist(pepid, pdb, hist)

if __name__ == '__main__':
	main()
