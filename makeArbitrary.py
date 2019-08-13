from random import randint


# create temporary list of associated indices
def Create_Linking(data):
	linking = []
	for i in range(0, len(data)):
		linking.append([i, data[i][0], data[i][6], data[i][9]])
		# [index, CommonName, LocationName, Observer]
	return linking

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

def Create_Observers(linking):
	file1 = "data/names.txt"
	file2 = "data/organizations.txt"
	observers = []
	organizations = []

	# generate name list
	with open(file1) as names:
		for name in names:
			observers.append([name.split(' ')[0], name.split(' ')[1].split('\n')[0]])
	# generate org list
	with open(file2) as orgs:
		for org in orgs:
			organizations.append(org.split('\n')[0])
	# assign random org to each name
	for obs in observers:
		obs.append(organizations[randint(0,len(organizations)-1)])

	# create list of unique observer IDs
	idx = 0
	unique_observer = []
	for item in linking:
		if(item[3] not in unique_observer):
			unique_observer.append(item[3])
			idx += 1

	# assign fictitious observers to actual eBird observerIDs
	paired_observer_list = []
	for index, obs in enumerate(zip(observers, unique_observer)):
		paired_observer_list.append([index, obs[0][0], obs[0][1], obs[0][2], obs[1]])
	
	return paired_observer_list


