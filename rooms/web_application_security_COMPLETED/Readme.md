# Web Application Security


> (\*) Learn about web applications and explore some of their common security issues.

---

---

## Task 1: Introduction

* Every one of us uses different programs on our computers. Generally speaking, programs run on our computers, using our computer’s processing power and storage. Moreover, to use a program, we need to install it first. What if we can use any program without installation?

![Online Shopping Web Application](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/8e17b0405e195e975d517f995b2bb068.png)

* A web application is like a “program” that we can use without installation as long as we have a modern standard web browser, such as Firefox, Safari, or Chrome. Consequently, instead of installing every program you need, you only need to browse the related page. The following are some examples of web applications:

	* Webmail such as Tutanota, Protonmail, Outlook, and Gmail
	
	* Online office suites such as Microsoft Office 365 (Word, Excel, and PowerPoint), Google Drive (Docs, Sheets, and Slides), and Zoho Office (Writer, Sheet, and Show)

	* Online shopping such as Amazon.com, AliExpress, and Etsy

* Thousands more examples provide a myriad of services. Other examples include online banking, money transfer, weather forecast, and social media.


![Online Banking Web Application](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/7506ada8e89f3ec9694182d34e3056cd.png)

* The idea of a web application is that it is a program running on a remote server. A server refers to a computer system running continuously to “serve” the clients. In this case, the server will run a specific type of program that can be accessed by web browsers.

* Consider an online shopping application. The web application will read the data about the products and their details from a database server. A database is used to store information in an organized way. Examples include information about products, customers, and invoices. A database server is responsible for many functions, including reading, searching, and writing to the database. The online shopping web application might need more than one database to access, for example:

	* Products database: This database contains details about the products, such as name, images, specifications, and price.

	* Customers database: It contains all details related to customers, such as name, address, email, and phone number.

	* Sales database: We expect to see what each customer has purchased and how they paid in this database.

* We can already see the amount of information stored in any online shopping system. Suppose an attacker manages to exploit (hack) the web application and steal the customers’ database. In that case, this will lead to a significant loss for the company and its customers.

* The image below shows searching for an item on an online shopping site. In the simplest version, the search will take four steps:

	1. The user enters an item name or related keywords in the search field. The web browser sends the search keyword(s) to the online shopping web application.

	2. The web application queries (searches) the products database for the submitted keywords.

	3. The product database returns the search results matching the provided keywords to the web application.

	4. The web application formats the results as a friendly web page and returns them to the user.

![Network diagram showing example database systems in a web application](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/9efb37af45d16b776ec3d6c6b9235c15.png)

* From the user’s perspective, they will only access an elegant online shop where all the technical infrastructure is hidden.

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/7cd9405026eca43ed73206e6e10e6b4c.png)

* Many companies offer bug bounty programs. A bug bounty program allows the company to offer a reward for anyone who discovers a security vulnerability (weakness) in the company’s systems. The main condition is that the found vulnerability is within the bug bounty scope and rules. Among many others, Google, Microsoft, and Facebook have bug bounty programs. Discovering a bug can earn you from a few hundred USD to tens of thousands of USD, depending on the severity of the vulnerability, i.e., the weakness you discovered.

---

* Answer the questions below
* What do you need to access a web application?

```
Browser
```


## Task 2: Web Application Security Risks

* Let’s say that you want to buy an item from an online shop. There are certain functions that you would expect to be able to do on this web application. Most straightforwardly, the online order might go as follows:

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/352114ac8da5f156f42aa551701323a2.png)

* There are a few main categories of common attacks against web applications. Consider the following steps and related attacks.

	* Log in at the website: The attacker can try to discover the password by trying many words. The attacker would use a long list of passwords with an automated tool to test them against the login page.

	* Search for the product: The attacker can attempt to breach the system by adding specific characters and codes to the search term. The attacker’s objective is for the target system to return data it should not or execute a program it should not.

	* Provide payment details: The attacker would check if the payment details are sent in cleartext or using weak encryption. Encryption refers to making the data unreadable without knowing the secret key or password.

* We cannot cover everything, but we will present a few formal categories from OWASP Top Ten. Don’t worry if these techniques sound alien to you; TryHackMe walks you through each vulnerability.

### Identification and Authentication Failure

* Identification refers to the ability to identify a user uniquely. In contrast, authentication refers to the ability to prove that the user is whom they claims to be. The online shop must confirm the user’s identity and authenticate them before they can use the system. However, this step is prone to different types of weaknesses. Example weaknesses include:

	* Allowing the attacker to use brute force, i.e., try many passwords, usually using automated tools, to find valid login credentials.

	* Allowing the user to choose a weak password. A weak password is usually easy to guess.

	* Storing the users’ passwords in plain text. If the attacker manages to read the file containing the passwords, we don’t want them to be able to learn the stored password.
	

![Database table with usernames and passwords in cleartext](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/0ac52c1bafa532db2a23e4a9efc6663d.png)



### Broken Access Control

* Access control ensures that each user can only access files (documents, images, etc.) related to their role or work. For example, you don’t want someone in the marketing department to access (read) the finance department’s documents. Example vulnerabilities related to access control include:

	* Failing to apply the principle of the least privilege and giving users more access permissions than they need. For example, an online customer should be able to view the prices of the items, but they should not be able to change them.

	* Being able to view or modify someone else’s account by using its unique identifier. For example, you don’t want one bank client to be able to view the transactions of another client.

	* Being able to browse pages that require authentication (logging in) as an unauthenticated user. For example, we cannot let anyone view the webmail before logging in.

### Injection

* An injection attack refers to a vulnerability in the web application where the user can insert malicious code as part of their input. One cause of this vulnerability is the lack of proper validation and sanitization of the user’s input.

### Cryptographic Failures

* This category refers to the failures related to cryptography. Cryptography focuses on the processes of encryption and decryption of data. Encryption scrambles cleartext into ciphertext, which should be gibberish to anyone who does not have the secret key to decrypt it. In other words, encryption ensures that no one can read the data without knowing the secret key. Decryption converts the ciphertext back into the original cleartext using the secret key. Examples of cryptographic failures include:

	* Sending sensitive data in clear text, for example, using HTTP instead of HTTPS. HTTP is the protocol used to access the web, while HTTPS is the secure version of HTTP. Others can read everything you send over HTTP, but not HTTPS.

	* Relying on a weak cryptographic algorithm. One old cryptographic algorithm is to shift each letter by one. For instance, “TRY HACK ME” becomes “USZ IBDL NF.” This cryptographic algorithm is trivial to break.
	
	* Using default or weak keys for cryptographic functions. It won’t be challenging to break the encryption that used 1234 as the secret key.

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/a4aa058f7f07ee91dfcae39e9075bae4.png)

* Don’t worry if these techniques look challenging or sophisticated at first. TryHackMe has dedicated in-depth rooms to help you understand and experiment with the various attacks against web applications.

---

* Answer the questions below
* You discovered that the login page allows an unlimited number of login attempts without trying to slow down the user or lock the account. What is the category of this security risk?

```
Identification and Authentication Failure
```

* You noticed that the username and password are sent in cleartext without encryption. What is the category of this security risk?

```
Cryptographic Failures
```


## Task 3: Practical Example of Web Application Security

* This task will investigate a vulnerable website that uses __Insecure Direct Object References (IDOR)__. __IDOR__ falls under the category of Broken Access Control. Broken access control means that an attacker can access information or perform actions not intended for them. Consider the case where a web server receives user-supplied input to retrieve objects (files, data, documents) and that they are numbered sequentially. Let’s say that the user has permission to access a photo named ```IMG_1003.JPG```. We might guess that there are also ```IMG_1002.JPG``` and ```IMG_1004.JPG```; however, the web application should not provide us with that image even if we figured out its name. In general, an IDOR vulnerability can occur if too much trust has been placed on that input data. In other words, the web application does not validate whether the user has permission to access the requested object.

* Just providing the correct URL for a user or a product does not necessarily mean the user should be able to access that URL. For instance, consider the product page ```https://store.tryhackme.thm/products/product?id=52```. We can expect this URL to provide details about product number 52. In the database, items would be assigned numbers sequentially. The attacker would try other numbers such as 51 or 53 instead of 52; this might reveal other retired or unreleased products if the web application is vulnerable.

* Let’s consider a more critical example; the URL ```https://store.tryhackme.thm/customers/user?id=16``` would return the user with ```id=16```. Again, we expect the users to have sequential ID numbers. The attacker would try other numbers and possibly access other user accounts. This vulnerability might work with sequential files; for instance, if the attacker sees 007.txt, the attacker might try other numbers such as ```001.txt```, ```006.txt```, and ```008.txt```. Similarly, if you were ID number 16 and ID number 17 was another user, by changing the ID to 17, you could see sensitive data that belongs to another user. Likewise, they can change the ID to 16 and see sensitive data that belongs to you. (Of course, we assume here that the system is vulnerable to IDOR.)

* Click on “View Site,” and let’s see this in action. You will see a page showing an Inventory Management System. If you click on the “Planned Shipments” tab, you will discover that an attacker has managed to mix things up as part of sabotage plans. Notice how they send the wrong tires to each assembly line; for instance, they assign scooter tires and motorcycle tires to bike assembly! If left unfixed, all tires will go to the wrong assembly.

* We will hack the system back and undo the attacker’s steps. On “Your Activity,” you can see the activity of one of the users. We have reason to believe that this website has an IDOR vulnerability.

---

* Answer the questions below
* Check the other users to discover which user account was used to make the malicious changes and revert them. After reverting the changes, what is the flag that you have received?

```
THM{IDOR_EXPLORED}
```