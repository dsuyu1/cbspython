# passgen
A simple password generator that I built to help me ease myself into learning Python while making something relevant to cybersecurity.
## Introduction
Often, in cybersecurity, we hear that humans are the weakest link in the security chain. As awesome as we may think we are, we are very susceptible to losing, forgetting,
or even worse, making weak passwords. A password generator that makes us strong passwords will help us to avert the trouble of making strong passwords ourselves.
<br>
## Objective
For my first Python/cybersecurity project, I decided to make a password generator. I will walk through step-by-step what each piece of code does. I aim to:
- Deepen my understanding of Python and cybersecurity topics
- Become more comfortable writing in Python

## Walkthrough
```python
import random
import string
```
As always, we import the neccessary libraries. ```random``` gives us the ability to generate random numbers. While Python supports strings, the ```string``` library extends our string
capabilities. In other words, we can mess with strings more.  The ```string``` library lets us give more complexity to our passwords we otherwise couldn't have without it.
<br>
```python
def generate_password(min_length: int = 8, max_length: int = 16): # password will always have a different length
```
Here, we define our first function, generate_password(). It accepts two parameters: ```min_length``` and  ```max_length```. These parameters allow you to specify the minimum and maximum lengths of the password.
If no values are provided when calling the function, it defaults to creating a password between 8 and 16 characters long. We call this <b>optional type hinting</b>.
<br>
```python
length = random.randint(min_length, max_length)
```
```length``` stores a random integer between ```min_length``` and ```max_length```(inclusive) using the ```random.randint()``` function. This ensures that each generated password will have a different length
within the given range.
<br>
```python
alphabet = string.ascii_letters + string.digits + string.punctuation
```


