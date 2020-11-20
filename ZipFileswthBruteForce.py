import zipfile

keyList = "abc123."
keys = []
tries = 0

for current in range(4):
	a = [i for i in keyList]
	for x in range(current):
		a = [y + i for i in keyList for y in a]

	keys = keys + a

z = zipfile.ZipFile("zipfile.zip")

for key in keys:
	try:
		tries += 1
		z.setpassword(key.encode("ascii"))
		z.extract("zipfile.txt")
		print(f"Key was found after {tries} tries! it was {key}")
		break
	except:
		pass	
