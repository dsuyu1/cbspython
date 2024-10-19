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
### 1. generate_password()
```python
def generate_password(min_length: int = 8, max_length: int = 16): # password will always have a different length
```
Here, we define our first function, ```generate_password()```. It accepts two parameters: ```min_length``` and  ```max_length```. These parameters allow you to specify the minimum and maximum lengths of the password.
If no values are provided when calling the function, it defaults to creating a password between 8 and 16 characters long. We call this <b>optional type hinting</b>.
<br>
```python
  length = random.randint(min_length, max_length)
```
`length` stores a random integer between `min_length` and `max_length`(inclusive) using the `random.randint()` function. This ensures that each generated password will have a different length
within the given range.
<br>
```python
  # alphabet is a huge list of all ascii letters, digits, and punctuation
  alphabet = string.ascii_letters + string.digits + string.punctuation 
```
Using the `string` library we imported earlier we can create a huge list of all the ASCII letters, all the digits, and all the different kinds of punctuation. We store them in the variable `alphabet`.
<br>
```python
  # picks 10 random letters, digits, and punctuation for our password
  password = ''.join(random.choice(alphabet) for i in range(length))
  return password
```
We use the `random` library to choose random characters from the huge list we made earlier (`alphabet`) for however long `length` is. In our example, `length` will default between 8 and 16 characters long. `password` stores the password as a `string`.
<br>
### 2. password_strength()
```python
def password_strength(password: str): # function accepts one parameter, password
```
Our second function, `password_strength`, accepts one parameter, `password` with the data type `string`.
<br>
```python
    if len(password) < 8:
        return "Weak"
    # no lower/uppercase letters
    if not any(c.islower() for c in password) or not any (c.isupper() for c in password):
        return "Moderate"
    # no digits or special characters
    if not any(c.isdigit() for c in password) or not any(c in string.punctuation for c in password):
        return "Moderate"
    return "Strong"
```
We use a series of `if` statements to determine the strength of `password`. If `password` is fewer than 8 characters, it is `Weak`. If `password` contains no uppercase or lowercase letters but it is 8 characters or longer, it is `Moderate`. Furthermore, if `password` contains no special characters or digits but satisfies the previous two conditions, then `password` is `Moderate`. Otherwise, if `password` fulfills all the conditions, it is `Strong`.

## Conclusion
```python
password = generate_password()
strength = password_strength(password)

print(f"Generated password: {password}")
print(f"Length of password: {len(password)}")
print(f"Password strength: {strength}")
```
<i>Test statements</i>
<br>

By writing this program, I learned about function syntax in Python and manipulating strings. 
