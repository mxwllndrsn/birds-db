filename = "ebird_dataset.txt"

k = 0
with open(filename) as ebird:
	for line in ebird.readlines():
		r = line.strip().split("\t")
		print(r[4], r[5], r[8], r[10], r[12], r[14], r[18])

# Common name [4]
# Scientific [5]
# Count [8]
# Age/Sex [10]
# Country [11]
# State [13]
# Obs Date [18]
