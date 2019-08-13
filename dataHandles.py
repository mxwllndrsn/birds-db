from random import randint


# import eBird Data
def Get_Data(filename):
	data = []
	with open(filename) as ebird:
		next(ebird) #skip header
		for line in ebird:
			try:
				row = next(ebird).split('\t')
			except:
				pass
			want = [row[4], row[5], row[14], row[15], row[16], row[22], row[27], row[28], row[29]]

			#[-2:] slice state abbrev from "US-WA"
			want.insert(3, want.pop(3)[-2:])
			#.split(' ') species / genus from SCIENTIFIC NAME
			sci_name = want.pop(1)
			want.insert(1, sci_name.split(' ')[1])
			want.insert(2, sci_name.split(' ')[0])
			data.append(want)
	return data


# create temporary list of associated indices
def Create_Linking(data):
	linking = []
	for i in range(0, len(data)):
		linking.append([i, data[i][7], data[i][8], data[i][0], data[i][6], data[i][9]])
		# [index, Date, Time, CommonName, LocationName, Observer]
	return linking

def Create_Seasonality():
	return [['Year-round'], ['Breeding'], ['Winter'], ['Migration']]


def Create_Conservation():
	return [['Least Concern'], ['Near Threatened'], ['Vulnerable'], ['Endangered'], ['Critically Endangered']]


#113 unique birds
def Unique_Birds(data):
	unique_birds = []
	# create list of unique birds and append conservation/seasonality IDs
	for i in range(0, len(data)):
		if(data[i-1][0] != data[i][0]):
			unique_birds.append([data[i][0], data[i][1], data[i][2], randint(0, 5), randint(0, 4)])
	return unique_birds

#88 unique locations
def Unique_Locations(linking, data):
	idx = 0
	unique_location = []
	# create list of unique locations
	for item in linking:
		if(item[4] not in unique_location):
			unique_location.append(item[4])
			idx += 1
	# just add the county and state
	for i in range(0, len(unique_location)):
		unique_location[i] = [unique_location[i], 'Montgomerey', 'Montgomerey', 'AL']
	return unique_location


# 20 unique observers
def Unique_Observers(linking):
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
		if(item[5] not in unique_observer):
			unique_observer.append(item[5])
			idx += 1

	# assign fictitious observers to actual eBird observerIDs
	paired_observer_list = []
	for o, u in zip(observers, unique_observer):
		paired_observer_list.append([o[0], o[1], o[2], u])
	
	return paired_observer_list

# return list of desired index
def stripped(og, idx):
	stripped = []
	for i in range(0, len(og)):
		stripped.append(og[i][idx])
	return stripped

# linking: [index, Date, Time, CommonName, LocationName, Observer]
def Corroborate_Links(linking, birds, locations, observers):
	for i in range(0, len(linking)):
		linking[i] = [i, linking[i][1], linking[i][2], birds.index(linking[i][3]),
		 locations.index(linking[i][4]), observers.index(linking[i][5])]
	
	return linking