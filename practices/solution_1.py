import datetime

now = datetime.datetime.now()
year=now.year
def when_hundred():
	name = input('What\'s your name?: ')
	age = int(input('How old are you?: '))
	year_difference = str((100 - age)+year)

	print('In ' + year_difference + ' you will be 100 years old ' + name)

if __name__== '__main__':
	when_hundred()