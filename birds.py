filename = "ebird_dataset.txt"

k = 0
with open(filename) as ebird:
	for line in ebird.readlines():
		r = line.strip().split("\t")
		print(r[4], r[5], r[8], r[10], r[12], r[14], r[18])


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