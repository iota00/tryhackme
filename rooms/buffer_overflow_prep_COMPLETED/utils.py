import binascii

def generate_bytearray():
	for x in range(1, 256):
		print("\\x" + "{:02x}".format(x), end='')
	print()

def hex2bytes(h):
	x = bytes.fromhex(h)
	print(x)
	print(h[::-1])

	# Print in reverse order
	print(x[::-1])