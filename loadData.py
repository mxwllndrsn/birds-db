import os
from toSQL import *
from dataHandles import *

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

# io data
infile = os.path.join('data', 'ebird_dataset.txt')
outfile = os.path.join('sql', 'birds_data')

data = Get_Data(infile)

# create tables
sighting = Create_Table('Sighting', ['Date', 'Time', 'BirdId', 'LocationId', 'ObserverId'])
location = Create_Table('Location', ['LocationName','City','County','State'])
birds = Create_Table('Birds', ['CommonName','Genus','Species','ConservationId', 'SeasonalityId'])
observer = Create_Table('Observer', ['ObserverFName', 'ObserverLName', 'Organization'])
conservation = Create_Table('Conservation', ['ConservationStatus'])
seasonality = Create_Table('Seasonality', ['Seasonality'])
sighting = Create_Table('Sighting', ['Date', 'Time', 'BirdId', 'LocationId', 'ObserverId'])

# lists for records
linking = Create_Linking(data)
u_birds = Unique_Birds(data)
u_locations = Unique_Locations(linking, data)
u_observers = Unique_Observers(linking)
seasonality_types = Create_Seasonality()
conservation_types = Create_Conservation()

# sort links 
linking = Corroborate_Links(linking, stripped(u_birds, 0), stripped(u_locations, 0), stripped(u_observers, 3))

# create records
Create_Records(location, u_locations, [0, 1, 2, 3])
Create_Records(birds, u_birds, [0, 1, 2, 3, 4])
Create_Records(observer, u_observers, [0, 1, 2])
Create_Records(seasonality, seasonality_types, [0])
Create_Records(conservation, conservation_types, [0])
Create_Records(sighting, linking, [1, 2, 3, 4, 5])

# write sql 
sql_out = Write_SQL(conservation)
sql_out += Write_SQL(seasonality)
sql_out += Write_SQL(location)
sql_out += Write_SQL(birds)
sql_out += Write_SQL(observer)
sql_out += Write_SQL(sighting)

Export_SQL(sql_out, outfile)