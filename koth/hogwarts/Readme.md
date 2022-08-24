# Hogwarts

```bash
export IP=10.10.186.78
```

* Nmap scan results:

```
22/tcp   open     http       Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Site doesn't have a title (text/html).
|_ssh-hostkey: ERROR: Script execution failed (use -d to debug)
5989/tcp filtered wbem-https
9999/tcp open     abyss?
| fingerprint-strings: 
|   FourOhFourRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Date: Tue, 23 Aug 2022 16:46:17 GMT
|     Content-Length: 0
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Date: Tue, 23 Aug 2022 16:46:16 GMT
|_    Content-Length: 0
```

* found in /style.cloudflare.css

```
/* Resurrection stone: bdc!32mogonld75lbsi3apluc  */
```

1svc8@vik1r5q3sdxkt5lqtts
