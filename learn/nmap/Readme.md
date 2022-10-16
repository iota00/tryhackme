# NMAP

## Nmap Switches

1. What is the first switch listed in the help menu for a 'Syn Scan'?

```
-sS
```

2. Which switch would you use for a "UDP scan"?

```
-sU
```

3.If you wanted to detect which operating system the target is running on, which switch would you use?

```
-O
```

4. Nmap provides a switch to detect the version of the services running on the target. What is this switch?

```
-sV
```
5. The default output provided by nmap often does not provide enough information for a pentester. How would you increase the verbosity?

```
-v
```

6. How would you set the verbosity level to two?

```
-vv
```

7. What switch would you use to save the nmap results in three major formats?

```
-oA
```

8. What switch would you use to save the nmap results in a "normal" format?

```
-oN
```

9. A very useful output format: how would you save results in a "grepable" format?

```
-oG
```

10. How would you activate this setting?

```
-A
```

11. How would you set the timing template to level 5?

```
-t5
```

12. How would you tell nmap to only scan port 80?

```
-p 80
```

13. How would you tell nmap to scan ports 1000-1500?

```
-p 1000-1500
```

14. How would you tell nmap to scan all ports?

```
-p-
```

15. How would you activate a script from the nmap scripting library ?

```
--script
```

16. How would you activate all of the scripts in the "vuln" category?

```
--script=vuln
```

## Scan Types

* When port scanning with Nmap, there are three basic scan types. These are:

1. TCP Connect Scans ```(-sT)```
2. SYN "Half-open" Scans ```(-sS)```
3. UDP Scans ```(-sU)```

* Additionally there are several less common port scan types. These are:

1. TCP Null Scans ```(-sN)```
2. TCP FIN Scans ```(-sF)```
3. TCP Xmas Scans ```(-sX)```

## TCP Connect Scans 

`-sT`

1. Which RFC defines the appropriate behaviour for the TCP protocol?

```
RFC 793
```

2. If a port is closed, which flag should the server send back to indicate this?

```
RST
```

## SYN Scans 

`-sS`

1. There are two other names for a SYN scan, what are they?

```
Half-open, stealth
```

2. Can Nmap use a SYN scan without Sudo permissions (Y/N)?

```
N
```

## UDP Scans 

`-sU`

1. If a UDP port doesn't respond to an Nmap scan, what will it be marked as?

```
open|filtered
```

2. When a UDP port is closed, by convention the target should send back a "port unreachable" message. Which protocol would it use to do so?

```
ICMP
```

## NULL, FIN and Xmas

All three are interlinked and are used primarily as they tend to be even stealthier, relatively speaking, than a SYN "stealth" scan.

* NULL (`-sN`): when the TCP request is sent with no flags set at all. (the target host should response with RST if the port is closed)
* FIN (`-sF`): almost identical, a request with the FIN flag is sent (usually used to close an active connection. Again Nmap expects a RST if the port is closed)
* Xmas (`-sX`): send a malformed TCP packet and expects a RST response if the port is closed. Set (PSH, URG, and FIN) flags (give it the appearance of blinking chrismats tree when viewed as a packet)
* The expected response for open ports with these scans is also identical, and is very similar to that of a UDP scan.
* If the port is open then there's no response to the malformed packet.
* **Note**: `Microsoft Windows (and a lot of Cisco network devices) are known to respond with a RST to any malformed TCP packet -- regardless of whether the port is actually open or not.`
* `By sending requests which do not contain the SYN flag, we effectively bypass this kind of firewall.` (this is good in theory, most IDS solutions are savvy to these scan types)

1. Which of the three shown scan types uses the URG flag? 

```
Xmas
```

2. Why are NULL, FIN and Xmas scans generally used?

```
firewall evasion
```

3. Which common OS may respond to a NULL, FIN or Xmas scan with a RST for every port?

```
Microsoft Windows
```

## ICMP Network Scanning

* **Ping sweep**: Nmap sends an ICMP packet to each possible IP for the specified network, when it receives a response, it marks the IP that responded as being alive.
* To perform a ping sweep, we use `-sn` switch with IP ranges (can be either a `-` hypen or CIDR notation)

```bash
# Example: scan 192.168.0.X network

nmap -sn 192.168.0.1-254

# or

nmap -sn 192.168.0.1/24

```

* The `-sn` switch tells Nmap not to scan any ports -- forcing it to rely primarily on ICMP echo packets (or ARP requests on a local network) to identify targets.
* Also cause nmap to send a TCP SYN packet to port 443 of the target, as well as a TCP ACK (or SYN if not run as sudo) packet to port 80 of the target.

1. How would you perform a ping sweep on the 172.16.x.x network (Netmask: 255.255.0.0) using Nmap? (CIDR notation)?

```bash
nmap 172.16.0.0/16
```

## NSE Scripts

* The Nmap Scripting Engine (NSE) is an incredibly powerful addition to Nmap, extending its functionality quite considerably.
* NSE Scripts are written in the Lua programming language, and can be used to do a variety of things: from scanning for vulnerabilities, to automating exploits for them.
* The NSE is particularly useful for reconnaisance, however, it is well worth bearing in mind how extensive the script library is.
* There are many categories available. Some useful categories include:
    * `safe`: Won't affect the target
    * `intrusive`: Not safe, likely to affect the target
    * `vuln`: Scan for vulnerabilities
    * `exploit`: Attempt to exploit a vulnerability
    * `auth`: Attempt to bypass authentification for running services (e.g: log into an FTP server anonymously)
    * `brute`: Attempt to bruteforce credentials for running services
    * `brute`: Attempt to query running services for further information about the network (e.g: query an SNMP server)

> More [here](https://nmap.org/book/nse-usage.html)

1. What language are NSE scripts written in?

```

```

2. Which category of scripts would be a very bad idea to run in a production environment?

```
intrusive
```

## Working with NSE

* To run a specific script, we would use `--script=<script-name>`
* Multiple scripts can be run simultaneously in this fashion by separating them by a comma `--script=smb-enum-users,smb-enum-shares`
* Some scripts require arguments, these can be given with the `--script-agrs` Nmap switch.

```bash
# Example: http-put to upload a filen takes 2 agrs(URL to upload the file to, file's location on the disk)

nmap -p 80 --script http-put --script-agrs http-put.url='/dav/shell.php',http-put.file="./shell.php"

```

> Full list of scripts and their corresponding arguments can be found [here](https://nmap.org/nsedoc/)

1. What optional argument can the ftp-anon.nse script take?

```
maxlist
```

## Searching for Scripts

* We have two options for this :
    * The first is the page on the Nmap website.
    * The second is the local storage on your attacking machine.

* Nmap stores its scripts on Linux at `/usr/share/nmap/scripts`
* There are two ways to search for installed scripts:
    * One is by using the `/usr/share/nmap/scripts/script.db` file. (*scripts.db* isn't a database: formatted text file)
    * The second way to search for scripts is quite simply to use the `ls` command. 
    ```bash 
    ls -l /usr/share/nmap/scripts/*ftp*
    ```
* **Installing New Scripts**

```bash
# if one of these is missing in the scripts directory locally
# A standard 
sudo apt update && sudo apt install nmap 
# should fix this; however, it's also possible to install the scripts manually by downloading the script from Nmap 
sudo wget -O /usr/share/nmap/scripts/<script-name>.nse https://svn.nmap.org/nmap/scripts/<script-name>.nse
# This must then be followed up with 
nmap --script-updatedb 
# which updates the script.db file to contain the newly downloaded script
```

Search for "smb" scripts in the `/usr/share/nmap/scripts/` directory using either of the demonstrated methods.
1. What is the filename of the script which determines the underlying OS of the SMB server?

```
smb-os-discovery.nse
```

2. Read through this script. What does it depend on?

> look for dependecies in the smb-os-discovery.nse file

```
smb-brute
```

## Firewall Evasion

* Nmap provides an option for this: `-Pn`, which tells Nmap to not bother pinging the host before scanning it. (treat the host as being alive, effectivly bypassing the ICMP block)
* There are a variety of other switches which Nmap considers useful for firewall evasion:
    * `-f`:- Used to fragment the packets making it less likely that the packets will be detected by a firewall or IDS.
    * `--mtu <number>`, alternative to `-f`, but providing more control over the size of the packets, accepts a maximum transmission unit size to use for the packets sent. This must be a multiple of 8.
    * `--scan-delay <time>ms`:- used to add a delay between packets sent. This is very useful if the network is unstable, but also for evading any time-based firewall/IDS triggers which may be in place.
    * `--badsum`:- this is used to generate in invalid checksum for packets. Any real TCP/IP stack would drop this packet, however, firewalls may potentially respond automatically, without bothering to check the checksum of the packet. As such, this switch can be used to determine the presence of a firewall/IDS.

1. Which simple (and frequently relied upon) protocol is often blocked, requiring the use of the `-Pn` switch?

```
ICMP
```

2. [Research] Which Nmap switch allows you to append an arbitrary length of random data to the end of packets?

```
--data-length
```

## Practical

1. Does the target (10.10.166.147)respond to ICMP (ping) requests (Y/N)?

```
N
```

2. Perform an Xmas scan on the first 999 ports of the target -- how many ports are shown to be open or filtered?

```
999
```

3. There is a reason given for this -- what is it?

```
no responses
```

4. Perform a TCP SYN scan on the first 5000 ports of the target -- how many ports are shown to be open?

```
5
```

5. Deploy the ftp-anon script against the box. Can Nmap login successfully to the FTP server on port 21? (Y/N)

```
Y
```
