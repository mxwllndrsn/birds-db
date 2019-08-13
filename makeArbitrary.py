from random import randint


def Create_Seasonality():
	return [['Year-round'], ['Breeding'], ['Winter'], ['Migration']]


def Create_Conservation():
	return [['Least Concern'], ['Near Threatened'], ['Vulnerable'], ['Endangered'], ['Critically Endangered']]


# remove duplicate entries and append rand conservation and seasonality IDs
# access by index 9, 10
'''def Bird_Filter_Append(data):
	bird_filter = []
	for i in range(0, len(data)):
		if(data[i-1][0] != data[i][0]):
			bird_filter.append(data[i])
	for bird in bird_filter:
		bird.append(randint(0, 5))
		bird.append(randint(0, 4))
	return bird_filter
'''

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

