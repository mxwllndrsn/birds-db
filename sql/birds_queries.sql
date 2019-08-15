USE bird;

/*This view is a convenient fact sheet about the various bird species*/
CREATE OR REPLACE VIEW bird_info AS
SELECT birds.CommonName, CONCAT(birds.Genus, ' ',birds.Species) AS 'Scientific Name', seasonality.Seasonality, conservation.ConservationStatus
FROM birds JOIN seasonality USING (SeasonalityId)
		   JOIN conservation USING (ConservationId);
           
/*This view returns all sightings in Montgomerey, AL*/
CREATE OR REPLACE VIEW Montgomerey_Sightings AS
SELECT sighting.Date, Location.LocationName, birds.CommonName, conservation.ConservationStatus
FROM sighting JOIN Location USING (LocationId)
			  JOIN birds USING (BirdId)
              JOIN conservation USING (ConservationId)
WHERE Location.City='Montgomerey' AND Location.State='AL'
ORDER BY ConservationStatus, CommonName, `Date`;

/*This is a query of all endangered bird sightings in Montgomerey, AL*/
SELECT *
FROM Montgomerey_Sightings
WHERE ConservationStatus='Endangered' OR ConservationStatus='Critically Endangered'
ORDER BY CommonName, Date;


/*This is a query that returns the 10 observers who have contributed the most sightings */
SELECT ObserverId, ObserverFName, ObserverLName ,COUNT(ObserverId) AS Total
FROM sighting JOIN observer USING (ObserverId)
GROUP BY ObserverId
ORDER BY Total DESC
LIMIT 10;


/*This is a query that returns the dates of the 10 most recent sightings in Montgomerey*/
SELECT `Date`, `Time`
FROM Sighting
ORDER BY `Date` DESC, `Time`
LIMIT 10;

/*This returns all the species sighted in Montgomerey*/
SELECT DISTINCT CommonName
FROM Montgomerey_Sightings;

/*This is a query that tells us which observers have seen endangered species*/
SELECT DISTINCT observer.ObserverFName, observer.ObserverLName,  birds.CommonName, conservation.ConservationStatus
FROM observer JOIN sighting USING (ObserverId)
			  JOIN birds USING (BirdId)
              JOIN conservation USING (ConservationId)
WHERE ConservationStatus='Endangered';
