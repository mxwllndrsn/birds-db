'''
5 data tables, 1 linking table 

LINK:Sighting
	Id 				INT
	Date 			DATE
	Time			TIME
	BirdId			INT
	LocationId		INT
	ObserverId		INT

Location
	Id				INT
	LocationName	VARCHAR
	City			VARCHAR
	County			VARCHAR
	State			CHAR(2)

Observer
	Id				INT
	ObserverFName	VARCHAR
	ObserverLName	VARCHAR
	Organization	VARCHAR

Birds
	Id				INT
	CommonName		VARCHAR
	Genus			VARCHAR
	Species			VARCHAR
	ConservationId	TINYINT
	SeasonalityId	TINYINT

Conservation
	Id 					INT
	ConservationStatus	VARCHAR

Seasonality
	Id 					INT
	SeasonalityType		VARCHAR
'''

class Table:
	name = ""
	fields = []
		# fields [field1, field2, ...]
	records = {}
		# records dict {id: {field: data, field: data, ...}, id2: {field: data, field: data}, {...}}
		# unique record dict created in add_record(self, data)

	def __init__(self, name):
		self.name = name

	def print_name(self):
		print(self.name)

	def add_field(self, field_name):
		self.fields[field_name] = ''

	def add_record(self, data):
		# data[] supplied in appropriate order
		for key, item in zip(self.fields, data):
			self.fields[key] = data
			self.records[len(self.records)+1] = self.fields

	def print_items(self, idx='all'):
		if(idx!='all'):
			print(self.records.get(idx))
		else:
			for key, val in self.records.iteritems():
				print(key, val)

			 
location = Table('Location')
location.print_name()

location.add_field('City')
location.add_record('Seattle')
location.print_items(1)

location.add_field('County')
location.add_record('King')
location.print_items(2)

print
print('all:')
location.print_items()