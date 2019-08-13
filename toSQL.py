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

	def __init__(self, fields, values):
		self.info = dict(zip(fields, values))
	def get_record(self):
		return self.info


class Table:

	def __init__(self, name):
		self.name = name
		self.records = {}
		self.fields = []
		# fields [field1, field2, ...]
		# records dict {id: {field: data, field: data, ...}, id2: {field: data, field: data}, {...}}
		# unique record as dict created in add_record(self, data)
	def print_name(self):
		print(self.name)

	def add_field(self, field_name):
		self.fields.append(field_name)

	def add_record(self, data):
		self.records[len(self.records)] = Record(self.fields, data)
			
	def print_records(self, idx='all'):
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


def Create_Records(table, data, indices):
	for row in data:
		table.add_record([row[i] for i in indices])


def Write_SQL(table):
	sql_str = 'SET AUTOCOMMIT=0;\nINSERT INTO {0} VALUES\n'.format(table.name)
	for i in range(0, len(table.records)):
		sql_str += '('
		sql_str += str(i)+', '
		
		for field in table.fields:
			sql_str += str(table.records[i].get_record()[field])+', '
		
		sql_str = sql_str[:-2] +'),\n'
	sql_str = sql_str[:-2]+ ';\nCOMMIT;\n'

	return sql_str


def Export_SQL(sql, filename):
	with open(filename+'.sql', 'w') as fout:
		fout.write(sql)