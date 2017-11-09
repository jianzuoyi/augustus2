#!/usr/bin/env python

import re, sys

def mergeall(gff, lst, all):
	all = re.split(r',|\n', all)[:-1]
	q = {}
	for line in gff:
		each = line.strip().split()
		if each[2] == 'mRNA':
			geneid = re.search(r'ID=(.*?);', each[8]).group(1)
			q[geneid] = int(each[4]) - int(each[3])
			if not geneid in all:
				lst.append(geneid)
	finalset = longset(lst, q)
	return finalset

def longset(lst,longdic):
	geneset = []
	q = {}
	for line in lst:
		ids = line.strip().split(',')
		if len(ids) > 1:
			for id in ids:
				length = longdic[id]
				q[length] = id
			long = max(q.keys())
			geneset.append(q[long])
		else:
			geneset.append(ids[0])
	return geneset

def mkdb(gff):
	db = {}
	for line in gff:
		line = line.strip()
		if line:
			each = line.split()
			if each[2] == 'gene':
				id = 'evm.model.' + re.search(r'ID=evm.TU.(.*?);', each[8]).group(1)
				db[id] = [line]
			else:
				db[id].append(line)
	return db

def extract_longff(lst, db):
	with open('final_longest.gff', 'w') as out:
		for k in sorted(lst, key = lambda x : (int(re.search(r'(\d+)\.(\d+)', x).group(1)), int(re.search(r'(\d+)\.(\d+)', x).group(2)))):
			out.write('\n'.join(db[k]) + '\n')

def extract_longpep(lst, all):
	p = {}
	for line in all:
		line = line.strip()
		if line.startswith('>'):
			id = line[1:]
		else:
			p[id] = line
	with open('final_longest.pep', 'w') as out:
		for k in lst:
			out.write('>' + k + '\n' + p[k] + '\n')

def main():
	with open(sys.argv[1], 'r') as file1:
		lst = file1.readlines()
	with open(sys.argv[1], 'r') as file1:
		All = file1.read()
	with open(sys.argv[2], 'r') as file2:
		gff = file2.readlines()
	db = mkdb(gff)
	finalset = mergeall(gff, lst, All)
	extract_longff(finalset, db)
	with open(sys.argv[3], 'r') as file3:
		extract_longpep(finalset, file3)
		
if __name__ == '__main__':
	main()
