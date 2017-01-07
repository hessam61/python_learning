import bz2, sys

opener = bz2.opener

if __name__ == '__main__':
	f = bz2.open(sys.argv[1], mode='wt')
	f.write(' '.join(sys.argv[2:]))
	f.close()