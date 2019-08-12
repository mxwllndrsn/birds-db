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

class Record:
	info = {}

	def __init__(self, fields, values):
		self.info = dict(zip(fields, values))
	def get_record(self):
		return self.info

class Table:
	name = ''
	fields = []
		# fields [field1, field2, ...]
	records = {}
		# records dict {id: {field: data, field: data, ...}, id2: {field: data, field: data}, {...}}
		# unique record as dict created in add_record(self, data)

	def __init__(self, name):
		self.name = name

	def print_name(self):
		print(self.name)

	def add_field(self, field_name):
		self.fields.append(field_name)

	def add_record(self, data):
		# data[] supplied in appropriate order
		self.records[len(self.records)] = Record(self.fields, data)
			
	def print_items(self, idx='all'):
		if(idx!='all'):
			print(self.records.get(idx).get_record())
		else:
			for key, val in self.records.items():
				print(key, val.get_record())


def Create_Table(name, fields):
	table = Table(name)
	for field in fields:
		table.add_field(field)
	return table