CREATE OR REPLACE VIEW birdTime AS
SELECT CommonName, LocationName, `Time`
FROM
	Sighting
		JOIN Birds USING (BirdId)
        JOIN Location USING (LocationId)
WHERE `Time` BETWEEN '06:00:00' AND '12:00:00'
ORDER BY `Time`, CommonName;
        
SELECT * FROM birdTime;