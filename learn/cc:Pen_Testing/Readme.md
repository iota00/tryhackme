# CC: Pen Testing

## Task 1

```
No answer needed
```

1. __Section 1 - Network Utilities__

## Task 2

### __nmap__

* nmap is one of the most important tools in a pen testers arsenal. It allows a pen tester to see which ports are open, and information about which services are running on those ports.

1. What does nmap stand for?

```
Network Mapper
```

2. How do you specify which port(s) to scan?

```
-p
```

3. How do you do a "ping scan"(just tests if the host(s) is up)?

```
-sn
```

4. What is the flag for a UDP scan? 

```
-sU
```

5. How do you run default scripts?

```
-sC
```

6. How do you enable "aggressive mode"(Enables OS detection, version detection, script scanning, and traceroute)

```
-A
```

7. What flag enables OS detection

```
-O
```

8. How do you get the versions of services running on the target machine 

```
-sV
```

9. Deploy the machine

```
No answer needed
```

10. How many ports are open on the machine?    

```
1
```

11. What service is running on the machine?           

```
Apache
```

12. What is the version of the service?

```
2.4.18
```

13. What is the output of the http-title script(included in default scripts)


```
Apache2 Ubuntu Default Page: It works
```

## Task 3

### NetCat

* Netcat aka nc is an extremely versatile tool. It allows users to connect to specific ports and send and receive data. It also allows machines to receive data and connections on specific ports, which makes nc a very popular tool to gain a [Reverse Shell](https://resources.infosecinstitute.com/icmp-reverse-shell/#gref).

1. How do you listen for connections?

```
-l
```

2. How do you enable verbose mode(allows you to see who connected to you)?

```
-v
```

3. How do you specify a port to listen on

```
-p
```

4. How do you specify which program to execute after you connect to a host(One of the most infamous)?

```
-e
```

5. How do you connect to udp ports

```
-u
```

2. __Section 2 - Web Enumeration__

## Task 4

### Gobuster

* One of the main problems of web penetration testing is not knowing where anything is. Basic reconnaissance can tell you where some files and directories are; however, some of the more hidden stuff is often hidden away from the eyes of users. This is where gobuster comes in, the idea behind gobuster is that it tries to find valid directories from a wordlist of possible directories. gobuster can also be used to valid subdomains using the same method.

1. How do you specify directory/file brute forcing mode?

```
dir
```

2. How do you specify dns bruteforcing mode?    

```
dns
```

3. What flag sets extensions to be used?

```
-x
```

4. What flag sets a wordlist to be used?

```
-w
```

5. How do you set the Username for basic authentication(If the directory requires a username/password)?

```
-U
```

6. How do you set the password for basic authentication?

```
-P
```

7. How do you set which status codes gobuster will interpret as valid?

Example: 200,400,404,204

```
-s
```

8. How do you skip ssl certificate verification?

```
-k
```

9. How do you specify a User-Agent?

```
-a
```

10. How do you specify a HTTP header?

```
-H
```

11. What flag sets the URL to bruteforce?

```
-u
```

12. Deploy the machine

```
No answer needed
```

13. What is the name of the hidden directory

```
secret
```

14. What is the name of the hidden file with the extension xxa

```
password
```

## Task 5

### Nikto

* nikto is a popular web scanning tool that allows users to find common web vulnerabilities. It is commonly used to check for common CVE's such as shellshock, and to get general information about the web server that you're enumerating.

1. How do you specify which host to use?   

```
-h
```

2. What flag disables ssl?

```
-nossl
```

3. How do you force ssl?

```
-ssl
```

4. How do you specify authentication(username + pass)?

```
-id
```

5. How do you select which plugin to use?

```
-plugins
```

6. Which plugin checks if you can enumerate apache users?   
```
apacheusers
``` 

5. How do you update the plugin list    

```
-update
```

6. How do you list all possible plugins to use

```
-list-plugins
```
