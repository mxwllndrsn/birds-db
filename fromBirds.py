from toSQL import *

''' eBird dataset description

date
time
bird
	commonname
	genus
	species
	conservation
	seasonality
observer
	fname
	lname
	organization
location
	name
	city
	county
	state

INDICES (after acquisition)

  0 COMMON NAME
  1 SCIENTIFIC NAME .split(' ') species
  2 SCIENTIFIC NAME .split(' ') genus
  3 STATE
  4 STATE CODE [:-2]
  5 COUNTY
  6 LOCALITY
  7 OBSERVATION DATE
  8 TIME OBSERVATIONS STARTED
  9 OBSERVER ID

'''

# table specific lists (not included in dataset)
seasonality_types = [['Year-round'], ['Breeding'], ['Winter'], ['Migration']]
conservation_types = [['Least Concern'], ['Near Threatened'], ['Vulnerable'], ['Endangered'], ['Critically Endangered']]

# input data
filename = "data/ebird_dataset.txt"
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


location = Create_Table('Location', ['LocationName','City','County','State'])
birds = Create_Table('Birds', ['CommonName','Genus','Species','ConservationId', 'SeasonalityId'])
observer = Create_Table('Observer', ['ObserverFName', 'ObserverLName', 'Organization'])
conservation = Create_Table('Conservation', ['ConservationStatus'])
seasonality = Create_Table('Seasonality', ['Seasonality'])
sighting = Create_Table('Sighting', ['Date', 'Time', 'BirdId', 'LocationId', 'ObserverId'])


Create_Records(location, data, [5, 4, 4, 3])

# remove duplicate entries and assign ID
bird_filter = []
for i in range(0, len(data)):
	if(data[i-1][0] != data[i][0]):
		bird_filter.append(data[i])

Create_Records(birds, bird_filter, [0, 1, 2])

Create_Records(observer, observer_filter, [9])
Create_Records(seasonality, seasonality_types, [0])
Create_Records(conservation, conservation_types, [0])

birds.print_records()
observer.print_records()