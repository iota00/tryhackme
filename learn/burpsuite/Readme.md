# Burp Suite: The Basics

## Task 1: `Introduction` Outline

* Specifically, we will be looking at:

    * What Burp Suite is
    * An overview of the available tools in the framework
    * Installing Burp Suite for yourself
    * Navigating and configuring Burp Suite. 

## Task 2: `Getting Started` What is Burp Suite?

* **Burp Suite** is a framework written in Java that aims to provide a one-stop-shop for web application penetration testing.
* Burp Suite is also very commonly used when assessing mobile applications, as the same features which make it so attractive for web app testing translate almost perfectly into testing the APIs powering most mobile apps.

* At the simplest level, Burp can capture and manipulate all of the traffic between an attacker and a webserver: this is the core of the framework. After capturing requests, we can choose to send them to various other parts of the Burp Suite framework.

```
This ability to intercept, view, and modify web requests prior to them being sent to the target server (or, in some cases, the responses before they are received by our browser), makes Burp Suite perfect for any kind of manual web app testing.
```

* There are various different editions of Burp Suite available:
	* Burp Suite Community (free)
	* Burp Suite Professional
	* Burp Suite Enterprise

---

1. Which edition of Burp Suite will we be using in this module?

```
Burp Suite Community
```

2. Which edition of Burp Suite runs on a server and provides constant scanning for target web apps?

```
Burp Suite Enterprise
```

3. Burp Suite is frequently used when attacking web applications and ______ applications.

```
Mobile
```

## Task 3: `Getting Started` Features of Burp Community 

Whilst Burp Community has a relatively limited feature-set compared to the Professional edition, it still has many superb tools available. These include:

1. **Proxy**: The most well-known aspect of Burp Suite, the Burp Proxy allows us to intercept and modify requests/responses when interacting with web applications.
2. **Repeater**: The second most well-known Burp feature -- Repeater -- allows us to capture, modify, then resend the same request numerous times. This feature can be absolutely invaluable, especially when we need to craft a payload through trial and error (e.g. in an SQLi -- Structured Query Language Injection) or when testing the functionality of an endpoint for flaws.
3. **Intruder**: Although harshly rate-limited in Burp Community, Intruder allows us to spray an endpoint with requests. This is often used for bruteforce attacks or to fuzz endpoints.
4. **Decoder**: Though less-used than the previously mentioned features, Decoder still provides a valuable service when transforming data -- either in terms of decoding captured information, or encoding a payload prior to sending it to the target. Whilst there are other services available to do the same job, doing this directly within Burp Suite can be very efficient.
5. **Comparer**: As the name suggests, Comparer allows us to compare two pieces of data at either word or byte level. Again, this is not something that is unique to Burp Suite, but being able to send (potentially very large) pieces of data directly into a comparison tool with a single keyboard shortcut can speed things up considerably.
6. **Sequencer**: We usually use Sequencer when assessing the randomness of tokens such as session cookie values or other supposedly random generated data. If the algorithm is not generating secure random values, then this could open up some devastating avenues for attack.






















