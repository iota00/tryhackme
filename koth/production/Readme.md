# Production

```bash

export IP=10.10.106.100

```

* Rustscan: found 2 ports

```

9002: Overly Limited Shell
9999: THM port for checking the king

```

* Using port 9002: found 2 users 

```
ashu
skidy
```

* FTP: flag.txt using ftp server

* **Flag 1**

```
cde6951cf12ff485d6d33ad7a2e6ac49
```

* ssh as **ashu** user:

1. flag inside *mail-server-backup* :

* **Flag 2**

```
06380baf84b7f9a8161e1642d4771251
```

* flag in **/home/skidy**:

1. flag.txt

* **Flag 3**

```
04461ad0759944a4d743deec6bbd8d54
```

* flag in **/home/ashu**

1. flag.txt

```
eabe4da21f519b8d6726427df7e683c5
```

* Getting root permissions:

1. change user from *ashu* to  *skidy* :

- by runnig **sudo -l** we can see that 
```

```

