import json

config = {}
config['Hostname'] = 'ipp'
config['Migrate'] = 'sec'


config = json.dumps(config).encode() + b"\x00"
#padding = b"\x00" * (2000 - len(config))
#config = config + padding



# Find {"Hostname"
with open("c2", "rb") as binFile:
	byteData = bytearray(binFile.read())
binFile.close()
offset = byteData.find(b'{"Hostname"')
print(offset)
with open("c2", "r+b") as binFile:
	binFile.seek(offset)
	binFile.write(config)

binFile.close()
