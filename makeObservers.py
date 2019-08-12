from random import randint

def Create_Observers():
	file1 = "data/names.txt"
	file2 = "data/organizations.txt"
	observers = []
	with open(file1) as names:
		for name in names:
			observers.append([name.split(' ')[0], name.split(' ')[1].split('\n')[0]])

	organizations = []
	with open(file2) as orgs:
		for org in orgs:
			organizations.append(org.split('\n')[0])

	for obs in observers:
		obs.append(organizations[randint(0,len(organizations)-1)])

	return observers