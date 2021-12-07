# XOR Encryption / Decryption 
<p align="right">(<a href="#-part-2">Jump to Part 2</a>)</p>  

# 🚀 Part 1
## About the Project
Implemented two python scripts: 
- <a href="cracker1.py">**encrypt.py**</a>   
           &nbsp;  - encrypts the 'input.txt' file, using xor and a specific password, and writes the result in the 'output' file.  
           &nbsp;  - time complexity: _O(n)_ </br>
           &nbsp; - memory complexity: _O(n)_, where n is the length of the input text
            </br>
            </br>
- <a href="cracker1.py">**decrypt.py**</a>  
            &nbsp; - decrypts the aforementioned encrypted 'output' file and writes the result in the 'input_recuperat.txt' file.  
            &nbsp; - time complexity: _O(n)_ </br>
            &nbsp; - memory complexity: _O(n)_, where n is the length of the input text

## Usage

Choose a password and run the python script as shown below    
  *&nbsp;&nbsp;&nbsp;&nbsp; // your password must contain between 10 and 15 characters which can be digits or english letters (both uppercase and lowercase)*  
  *&nbsp;&nbsp;&nbsp;&nbsp; // instead of 'password', write your own chosen password*

## Encryption
```bash
python encrypt.py password input.txt output
```

## Decryption
```bash
python decrypt.py password output input_recuperat.txt
```
***

# 🚀 Part 2
## Match
* Our Team: ```Asyncoders```
* Enemy Team: ```Riga Crypto```
* Enemy Team Password: ```CampinaBrasov1```

## About the Project
Implemented two python scripts:
- <a href="cracker1.py">**cracker1.py**</a>  
           &nbsp; - gets the password of another team using xor between their 'input.txt' and 'output' files.  
           </br>
- <a href="cracker2.py">**cracker2.py**</a>      
           &nbsp; - gets the password of another team while using only their 'output' file and xor operation.

## Password Cracking 1

Deriving from the fact that the password has at least 10 and at most 15 characters, we have 6 possible lengths (e.g. with n-characters).  For each of these 6 cases we are xor-ing character by character the first 2n characters of the text (we're not xor-ing all the characters, inasmuch as we are assured that the first n-characters and the second n-characters of the text are different), so that we can verify if the first half of the xored result string is equal to the second half. If so, we've found our correct password.

## Password Cracking 2

The main idea consists of using xor operation between every character from the 'output' file and all the possible characters that can appear in the 'input.txt' (i.e. digits, punctuation marks, space character, newline character, letters of the english alphabet both lowercase and uppercase, since the 'input.txt' file is written in romanian language without diacritics). 

If the result of this operation is a valid character (i.e. an ascii character), then it is added to a list which contains all the possible characters at a certain position in the password string. Afterwards, the list is appended to a bigger list of lists, which has a number of lists equal to the number of characters from the 'output' file.

After that, for a fixed length of the unknown password, we implemented the following algorithm:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;1. We search for the character at a certain position x in the password. We find the frequency of each character in the lists at     position x + k * lg, where 0 <= k <= cnt_ap, lg = fixed length, cnt_ap = required number of occurrences of a character from the password.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;2. If there is a character whose number of occurrences is equal to cnt_ap, then we add it to the password. If for a certain position in password we do not find any valid character, then the fixed length is not the right one, therefore we continue the search with the next possible length.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_//For more explanation, you can see the code comments_

### [Improved Algorithm]:  

If the length of the password is not between 10-15 characters and is comparable with the length of the output text, then there is the possibility that our previous algorithm might return more passwords. Thus, we create a dictionary that will contain the most frequent words of the romanian language in order to get the corrrect password (which by xor-ing with the output text returns a text written in romanian language without diacritics.

## Copyright © 2021

<p><a href="https://github.com/vl4dio4n">@vl4dio4n</a><a> &nbsp;</a><a href="https://github.com/cristina-timbur">@cristina-timbur</a></p>

***
*<p align="center"><a>FMI UniBuc 2021</a></p>*

<p align="right">(<a href="#top">Back to Top</a>)</p>
