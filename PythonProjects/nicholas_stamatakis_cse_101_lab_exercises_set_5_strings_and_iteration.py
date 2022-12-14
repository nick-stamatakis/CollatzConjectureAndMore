# -*- coding: utf-8 -*-
"""Nicholas Stamatakis CSE 101 Lab Exercises Set #5: Strings and Iteration

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jpaiZCZKLCWn2fOxB8WYCTfNnxJIPGp5

#CSE 101: Computer Science Principles

####Stony Brook University, Summer 2021, Session I Extended

### Lab Exercises Set #5

#### Due: Sunday, June 13, 2021 at 11:59 pm EDT

### Learning Outcomes
By the end of these exercises you should be able to:
* Write for-loops to perform simple computations.
* Use loops to perform basic repetitive operations on strings using for-loops.

### for-loops Fundamentals

E1. Write a for-loop that iterates exactly 10 times, printing the word `'Hello'` once per iteration.
"""

for i in range(10):
    print("Hello")

"""E2. Write a for-loop that counts from 0 to 9 inclusive and prints double each of those numbers (i.e., it will print 0, 2, 4, ..., 18, each on a separate line)."""

for i in range(10):
    print(i * 2)

"""E3. Write a for-loop that counts from 5 to 19 (inclusive) and prints every other value, starting with 5 (i.e., 5, 7, 9, ..., 19)."""

for i in range(5,20,2):
    print(i)

"""E4. Execute the code provided below. How many times is `'SBU'` printed? Ask yourself why you think this is the case."""

for i in range(-3):
    print('SBU')

#SBU is not printed in the code above.  This is because the range function assumes you to start at 
# an index of 0 and then increment positively by 1.  There is no way to reach -3 in such a case.

"""### The `ord` and `chr` Functions

E5. Display the Unicode value for the capital letter `'P'`.
"""

ord('P')

"""E6. Display the character that has the Unicode value `9992`."""

chr(9992)

"""E7. Use the `ord` and `chr` functions to display the character that has the code that is 5 greater than the code for the character `'&'`. Hint: use a mathematical operator."""

chr(ord('&') + 5)

"""### String Processing with Iteration

E8. Use a for-loop and `range` to print out each letter of a word stored in a variable named `word`, with each letter on a separate line. To make your code as general as possible, use the syntax `range(len(word))` so that your code works with words of any length.
"""

word="Computer"
for i in range(len(word)):
    print(word[i])

"""E9. Repeat the above process, but this time use the "for-each" syntax of a for-loop to print each letter of `word` on a separate line. That is, your code will need to contain the syntax `for w in word` somewhere (or a variable with a name other than `w`, your choice)."""

word="Computer"
for ch in word:
    print(ch)

"""E10. Write a for-loop that computes and displays the sum of the Unicode values of the characters in a string variable named `name`. Provide your own string to store in `name`."""

name="Nicholas"
sum=0
for ch in name:
    sum += ord(ch)
print(sum)

"""E11. Create a string called `movie` and store the title of a movie in it. Pick a movie whose title contains at least 15 characters. Using a for-loop and an if-statement, count and display the number of lowercase vowels in the movie title. (Hint: suppose `ch` stores a particular character from a string. The Boolean condition `ch in 'aeiou'` evaluates to `True` when `ch` stores a vowel.)"""

movie="Spiderman: No Way Home"
count=0
for ch in movie:
    if ch in 'aeiou':
        count += 1
print(count)

"""E12. Use the `enumerate` function and a for-loop to print each uppercase letter, along with its position in the alphabet, each on a separate line. Your output should resemble the following:

```
A 1
B 2
C 3
.
.
.
Z 26
```
"""

my_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i,j in enumerate(my_str,1):
  print(j,i)

"""### How to Submit Your Work

1. Go to the [course website](https://sites.google.com/stonybrook.edu/cse101sum/schedule-session-i).

1. Click the **Submit** link for this assignment.

1. Type your Net ID (Blackboard login) on the line provided.

1. Press the button marked **Add file**.

1. Click the **My Drive** tab.

1. Click on the file you wish to submit.

1. Hit **Select**.

1. Hit **Submit** to submit your file grading.
"""