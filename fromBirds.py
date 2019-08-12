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

INDICES

  4 COMMON NAME
  5 SCIENTIFIC NAME .split(' ') species/genus
 14 STATE
 15 STATE CODE [:-2]
 16 COUNTY
 22 LOCALITY
 27 OBSERVATION DATE
 28 TIME OBSERVATIONS STARTED
 29 OBSERVER ID

'''

filename = "data/ebird_dataset.txt"
have = []
with open(filename) as data:
	next(data) #skip header
	for line in data:
		try:
			row = next(data).split('\t')
		except:
			pass
		want = [row[4], row[5], row[14], row[15], row[16], row[22], row[27], row[28], row[29]]
		have.append(want)

for item, num in enumerate(have, 0):
	print(item, num)


location = Create_Table('Location', ['LocationName','City','County','State'])
bird = Create_Table('Birds', ['CommonName','Genus','Species','ConservationId', 'SeasonalityId'])
observer = Create_Table('Observer', ['ObserverFName', 'ObserverLName', 'Organization'])
conservation = Create_Table('Conservation', ['ConservationStatus'])
seasonality = Create_Table('Seasonality', ['Seasonality'])
sighting = Create_Table('Sighting', ['Date', 'Time', 'BirdId', 'LocationId', 'ObserverId'])




