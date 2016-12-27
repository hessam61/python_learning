def fibonacci():
	trail, lead = 0, 1
	while True:
		yield lead
		trail, lead = lead, trail + lead

if __name__ == '__main()__':
	fibonacci()