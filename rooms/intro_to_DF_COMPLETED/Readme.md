# Introduction to Digital Forensics:

## Task 1: Introduction

* Forensics: the application of science to investigate crimes and establish fact.
* Using digital systems (computersm smartphones,...) new branch of forensics was bron to investigate related crimes(computer forenics => Digital Forensics).
* Digital Forensics: the application of computer science to investigate digital evidence for legal purpose. DF is used in two types of investigations:
	* Public-sector inverstigation: investigations carried out by government and law enforcement agencies (would be part of crime or civil investigation).
	* Private-sector inverstigation: investigations carried out by corporate bodies vy assigning a private investigator. they are triggered by corporate policy violations.
---
![Question Image](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/4d5f3c52ca103102881305ce3bcd13e8.jpg)

* 
Consider the desk in the photo above. In addition to the smartphone, camera, and SD cards, what would be interesting for digital forensics?

```
laptop
```

## Task 2: Digital Forensics Process

* After getting the proper legal auth, the basic plan goes as follows:

1. **Acquire the evidence**: Collect the digital devices (laptops, storage, digital cameras).
2. **Establish a chain of custody**: (Fill out the related form) The purpose is that only auth investigators had access to the evidence and no one could tampered with it.
3. **Place the evidence in a secure container**: You want to ensure that the evidence does not get damaged. In the case of smartphones, you want to ensure that they cannot access the network, so they don’t get wiped remotely.
4. **Transport the evidence to your digital forensics lab**.

* At the lab, the process goes as follows:

1. **Retrieve** the digital evidence from the secure container.
2. **Create a forensic copy of the evidence**: The forensic copy requires advanced software to avoid modifying the original data.
3. **Return the digital evidence to the secure container**: You will be working on the copy. If you damage the copy, you can always create a new one.
4. **Start processing** the copy on your forensics workstation.

* More generally, according to the former director of the Defense Computer Forensics Laboratory, Ken Zatyko, digital forensics includes:

* **Proper search authority**: Investigators cannot commence without the proper legal authority.
* **Chain of custody**: This is necessary to keep track of who was holding the evidence at any time.
* **Validation with mathematics**: Using a special kind of mathematical function, called a hash function, we can confirm that a file has not been modified.
* **Use of validated tools**: The tools used in digital forensics should be validated to ensure that they work correctly. For example, if you are creating an image of a disk, you want to ensure that the forensic image is identical to the data on the disk.
* **Repeatability**: The findings of digital forensics can be reproduced as long as the proper skills and tools are available.
* __Reporting__: The digital forensics investigation is concluded with a report that shows the evidence related to the case that was discovered.

---

* 
It is essential to keep track of who is handling it at any point in time to ensure that evidence is admissible in the court of law. What is the name of the documentation that would help establish that?

```
Chain of custody
```

## Task 3: Practice Example 

* Using *pdfinfo*, find out the author of the attached PDF file. 

```
Ann Gree Shepherd
```

* Using *exiftool* or any similar tool, try to find where the kidnappers took the image they attached to their document. What is the name of the street?

```
Milk street
```

* What is the model name of the camera used to take this photo?

```
Canon EOS R6
```









