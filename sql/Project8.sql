

DROP DATABASE IF EXISTS Bird;
CREATE DATABASE Bird;
USE Bird;

CREATE TABLE Bird.Location		(
	LocationId		INT				PRIMARY KEY		AUTO_INCREMENT,
    LocationName	VARCHAR(64)		NOT NULL,
    City			VARCHAR(32)		NOT NULL,
    County			VARCHAR(32)		NOT NULL,
    State			CHAR(2)			NOT NULL
);

CREATE TABLE Bird.Observer	(
	ObserverId		INT 			PRIMARY KEY		AUTO_INCREMENT,
    ObserverFName	VARCHAR(32)		NULL,
    ObserverLName	VARCHAR(32)		NULL,
    `Organization`	VARCHAR(64)		NULL
    );

CREATE TABLE Bird.Seasonality	(
	SeasonalityId	TINYINT			PRIMARY KEY		AUTO_INCREMENT,	
    Seasonality		VARCHAR(10)		NOT NULL
    );

CREATE TABLE Bird.Conservation	(
	ConservationId		TINYINT 	PRIMARY KEY		AUTO_INCREMENT,
    ConservationStatus	VARCHAR(25)	NULL
    );
    
CREATE TABLE Bird.Birds		(
	BirdId			INT 			NOT NULL,
    CommonName		VARCHAR(45)		NOT NULL,
	Species			VARCHAR(30)		NOT NULL,
    Genus			VARCHAR(30)		NOT NULL,
    ConservationId	TINYINT			NOT NULL,
    SeasonalityId	TINYINT			NOT NULL,
		CONSTRAINT		Bird_BirdId_pk			PRIMARY KEY (BirdId),
        CONSTRAINT 		Bird_ConservationId_fk	FOREIGN KEY (ConservationId)
			REFERENCES 	Conservation (ConservationId)
            ON DELETE RESTRICT,
		CONSTRAINT		Bird_SeasonalityId_fk	FOREIGN KEY (Seasonalityid)
			REFERENCES	seasonality (Seasonalityid)
            ON DELETE RESTRICT
            );

CREATE TABLE Bird.Sighting	(
	SightingId		INT 			NOT NULL,
    `Date`			DATE 			NOT NULL,
    `Time`			TIME 			NOT NULL,
    BirdId			INT 			NOT NULL,
    LocationId		INT				NOT NULL,
    ObserverId		INT				NOT NULL,
		CONSTRAINT	Sight_SightingId_pk		PRIMARY KEY (SightingId),
        CONSTRAINT	Sight_BirdId_fk			FOREIGN KEY (BirdId)
			REFERENCES Birds (BirdId)
            ON DELETE RESTRICT,
		CONSTRAINT	Sight_LocationId_fk		FOREIGN KEY (LocationId)
			REFERENCES Location (LocationId)
            ON DELETE RESTRICT,
		CONSTRAINT	Sight_ObserverId_fk		FOREIGN KEY (ObserverId)
			REFERENCES Observer (ObserverId)
            ON DELETE RESTRICT
		);
    