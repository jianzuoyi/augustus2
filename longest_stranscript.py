#! /usr/bin/env python

import sys, re

def readall(lines):
	q = {}
	for line in lines:
		line = line.strip()
		if line:
			each = line.split()
			if each[2] == 'gene':
				id = re.search(r'^ID=(.*?);', each[8]).group(1)
				q[id] = [line]
			elif each[2] == 'CDS' or each[2] == 'mRNA':
				q[id].append(line)
	return q

def longest_transcript(lines):
	q = {}
	t = {}
	for line in lines[1:]:
		each = line.split()
		if each[2] == 'mRNA':
			id = re.search(r'ID=(.*?);', each[8]).group(1)
			q[id] = [line]
		elif re.search(r'Parent=(.*)', each[8]).group(1) == id:
			q[id].append(line)
	for k, v in q.iteritems():
		long = length(v)
		t[long] = k
	Max = max(t.keys())
	return q[t[Max]]

def output(dictionary):
	for k, v in dictionary.iteritems():
		type = [i.split()[2] for i in v]
		if type.count('mRNA') >= 2:
			lst = longest_transcript(v)
			lst.insert(0, v[0])
			dictionary[k] = lst
	with open('longest_transcript.gff', 'w') as out:
		for k in sorted(dictionary.keys(), key = lambda x : int(re.search(r'\d+', x).group())):
			out.write('\n'.join(dictionary[k]) + '\n\n')

def length(lines):
	n = 0
	for line in lines:
		each = line.split()
		if each[2] == 'CDS':
			n += int(each[4]) - int(each[3])
	return n 

def main():
	with open(sys.argv[1], 'r') as input:
		output(readall(input))

if __name__ == '__main__':
	main()
