import json


def xor(data):
    return bytearray((data[i] ^ ord("Q") for i in range(0, len(data))))

config = {}
config['Hostname'] = 'Die welt ist eine bloede'
config['Migrate'] = 'Die Zinsen verpesten die Menschheit'


config = json.dumps(config).encode()
padding = b"\x00" * (2000 - len(config) - 1) 
config = xor(config) + b"\xff" + padding


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
