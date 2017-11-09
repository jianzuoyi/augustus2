#!/usr/bin/env python

import sys

def tandem(lines, out):
	other_lst = iteration(lines, out)
	while len(other_lst) != 0:
		other_lst = iteration(other_lst, out)

def iteration(lst, out):
	seed = lst[0].strip()
	final = seed.split(',')
	while True:
		raw_nlst = len(lst)
		final,lst = delete(lst, final)
		after_nlst = len(lst)
		if raw_nlst == after_nlst:
			break
	out.write(','.join(list(set(final))) + '\n')
	lst.remove(lst[0])
	return lst

def delete(lst, final):
	for each in lst[1:]:
		e = each.strip().split(',')
		if e[0] in final:
			final.append(e[1])
			lst.remove(each)
		elif e[1] in final:
			final.append(e[0])
			lst.remove(each)
	return final, lst

def main():
	with open(sys.argv[1], 'r') as files, open('tandem_gene', 'w') as out:
		lines = files.readlines()
		tandem(lines, out)

if __name__ == '__main__':
	main()
