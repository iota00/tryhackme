# Introduction to Cryptography

## Task 1

* "Xjnvw lc sluxjmw jsqm wjpmcqbg jg wqcxqmnvw; xjzjmmjd lc wjpm sluxjmw jsqm bqccqm zqy." Zlwvzjxj Zpcvcol

* You can guess that it is a quote. Who said it?

```
Miyamoto Musashi
```

## Task 2

* Let’s review some terminology:

    * __Cryptographic Algorithm__ or __Cipher__: This algorithm defines the encryption and decryption processes.
    * __Key__: The cryptographic algorithm needs a key to convert the plaintext into ciphertext and vice versa.
    * __plaintext__ is the original message that we want to encrypt
    * __ciphertext__ is the message in its encrypted form

* AES (Advanced Encryption Standard) repeats the following four transformations multiple times:

    * __SubBytes(state)__: This transformation looks up each byte in a given substitution table (S-box) and substitutes it with the respective value. The state is 16 bytes, i.e., 128 bits, saved in a 4 by 4 array.
    * __ShiftRows(state)__: The second row is shifted by one place, the third row is shifted by two places, and the fourth row is shifted by three places. This is shown in the figure below.
    * __MixColumns(state)__: Each column is multiplied by a fixed matrix (4 by 4 array).
    * __AddRoundKey(state)__: A round key is added to the state using the XOR operation.


* In addition to AES, many other symmetric encryption algorithms are considered secure. Here is a list of symmetric encryption algorithms supported by GPG (GnuPG) 2.37.7, for example:

|Encryption Algorithm| 	Notes|
|---|---|
|AES, AES192, and AES256| 	AES with a key size of 126, 192, and 256 bits|
|IDEA| 	International Data Encryption Algorithm (IDEA)|
|3DES|	Triple DES (Data Encryption Standard) and is based on DES. We should note that 3DES will be deprecated in 2023 and disallowed in 2024.|
|CAST5| 	Also known as CAST-128. Some sources state that CASE stands for the names of its authors: Carlisle Adams and Stafford Tavares.|
|BLOWFISH| 	Designed by Bruce Schneier|
|TWOFISH |	Designed by Bruce Schneier and derived from Blowfish|
|CAMELLIA128, CAMELLIA192, and CAMELLIA256| 	Designed by Mitsubishi Electric and NTT in Japan. Its name is derived from the flower camellia japonica.|


### __GNU Privacy Guard__

* The GNU Privacy Guard, also known as GnuPG or GPG, implements the OpenPGP standard.

* We can encrypt a file using GnuPG (GPG) using the following command:

```bash
gpg --symmetric --cipher-algo CIPHER message.txt
```
* where CIPHER is the name of the encryption algorithm. You can check supported ciphers using the command `gpg --version`. The encrypted file will be saved as `message.txt.gpg`.

* The default output is in the binary OpenPGP format; however, if you prefer to create an ASCII armoured output, which can be opened in any text editor, you should add the option --armor. For example, 

```bash
gpg --armor --symmetric --cipher-algo CIPHER message.txt
```

* You can decrypt using the following command:

```bash
gpg --output original_message.txt --decrypt message.gpg
```

### __OpenSSL Project__

* The OpenSSL Project maintains the OpenSSL software.

* We can encrypt a file using OpenSSL using the following command:

```bash
openssl aes-256-cbc -e -in message.txt -out encrypted_message
```

* We can decrypt the resulting file using the following command:

```bash
openssl aes-256-cbc -d -in encrypted_message -out original_message.txt
```

* To make the encryption more secure and resilient against brute-force attacks, we can add `-pbkdf2` to use the Password-Based Key Derivation Function 2 (PBKDF2); moreover, we can specify the number of iterations on the password to derive the encryption key using `-iter NUMBER`. To iterate 10,000 times, the previous command would become:

```bash
openssl aes-256-cbc -pbkdf2 -iter 10000 -e -in message.txt -out encrypted_message
```

* Consequently, the decryption command becomes:

```bash
openssl aes-256-cbc -pbkdf2 -iter 10000 -d -in encrypted_message -out original_message.txt
```

---

* Decrypt the file quote01 encrypted (using AES256) with the key s!kR3T55 using gpg. What is the third word in the file?

```
waste
```

* Decrypt the file quote02 encrypted (using AES256-CBC) with the key s!kR3T55 using openssl. What is the third word in the file?

```
science
```

* Decrypt the file quote03 encrypted (using CAMELLIA256) with the key s!kR3T55 using gpg. What is the third word in the file?

```
understand
```

## Task 3

* Bob has received the file `ciphertext_message` sent to him from Alice. You can find the key you need in the same folder. What is the first word of the original plaintext?

```
Perception
```

* Take a look at Bob’s private RSA key. What is the last byte of p?

```
e7
```

* Take a look at Bob’s private RSA key. What is the last byte of q?

```
27
```

## Task 4

* A set of Diffie-Hellman parameters can be found in the file dhparam.pem. What is the size of the prime number in bits?

```
4096
```

* What is the prime number’s last byte (least significant byte)

```
4f
```

## Task 5

* What is the SHA256 checksum of the file `order.json`?

```
2c34b68669427d15f76a1c06ab941e3e6038dacdfb9209455c87519a3ef2c660
```

* Open the file `order.json` and change the amount from `1000` to `9000`. What is the new SHA256 checksum?

```
11faeec5edc2a2bad82ab116bbe4df0f4bc6edd96adac7150bb4e6364a238466
```

* Using SHA256 and the key `3RfDFz82`, what is the HMAC of `order.txt`?

```
c7e4de386a09ef970300243a70a444ee2a4ca62413aeaeb7097d43d2c5fac89f
```

## Task 6

* What is the size of the public key in bits?

```
4096
```

* Till which year is this certificate valid?

```
2039
```

## Task 7

* You were auditing a system when you discovered that the MD5 hash of the admin password is 3fc0a7acf087f549ac2b266baf94b8b1. What is the original password?

```
qwerty123
```

## Task 8

```
No Answer Needed
```

## Task 9

```
No Answer Needed
```
