# AES-Encryption-And-Decryption
##### This project is an Advanced Encryption Standard (AES) with 128 bit or 16 byte key values.
***
#### Advanced Encryption Standard (AES)
AES is a symmetric block cipher algorithm and it uses key to encrypt the message. It has three different key sizes like 128, 192, or 256 bit. In this project, AES 128-bit key was developed. It means that 128-bit or 16-byte messages can be encrypted and decrypted.<br/>
Some useful links are shown below.
* [Tutorial of AES](https://www.tutorialspoint.com/cryptography/advanced_encryption_standard.htm)
* [Article](https://www.researchgate.net/publication/338853730_A_Review_on_Advanced_Encryption_Standards_AES)
* [Example Encryption](https://kavaliro.com/wp-content/uploads/2014/03/AES.pdf)
***
#### Cipher block chaining (CBC)
CBC is a version of the AES. CBS uses the AES in itself and it can encrypt and decrypt all messages which have more byte than 16.<br/>
The schematic explanation link is shown below.
* [Tutorial of CBC](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC))
***
#### Output Feedback (OFB)
OFB is a version of the AES. OFB uses the AES in itself and it can encrypt and decrypt all messages which have more byte than 16.<br/>
The schematic explanation link is shown below.
* [Tutorial of OFB](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Output_feedback_(OFB))
***
#### Pay Attention
[AES.py](https://github.com/alihaydarkurban/AES-Encryption-And-Decryption/blob/main/AES.py) is the main program of the project. [CBC.py](https://github.com/alihaydarkurban/AES-Encryption-And-Decryption/blob/main/CBC.py) and [OFB.py](https://github.com/alihaydarkurban/AES-Encryption-And-Decryption/blob/main/OFB.py) have to use [AES.py](https://github.com/alihaydarkurban/AES-Encryption-And-Decryption/blob/main/AES.py) to encrypt and decrypt the messages. The runnable files are [AES_test.py](https://github.com/alihaydarkurban/AES-Encryption-And-Decryption/blob/main/AES_test.py), [CBC_test.py](https://github.com/alihaydarkurban/AES-Encryption-And-Decryption/blob/main/CBC_test.py) and [OFB_test.py](https://github.com/alihaydarkurban/AES-Encryption-And-Decryption/blob/main/OFB_test.py) to test the programs.
***

#### Requirements 
* The version of the python interpreter is Python 3.7.5 and you can find it [here](https://www.python.org/downloads/).
***
#### Running 
