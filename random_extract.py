#! /usr/bin/env python

import sys, random

def random_extraction(all):
	blacks = all.read().strip().split('\n\n')
	if len(blacks) <= 2000:
		os.system('ln -s ../../03.Isoseq/06.Transdecoder/longest_transcript.gff trainning.gff')
	else:
		with open('trainning.gff', 'w') as out:
			sample = random.sample(blacks, 2000)
			out.write('\n\n'.join(sample))

def main():
	with open(sys.argv[1], 'r') as inputfile:
		random_extraction(inputfile)

if __name__ == '__main__':
	main()
