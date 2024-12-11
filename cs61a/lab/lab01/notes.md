# Collected Mistakes
## Q1: WWPD: Control

### how_big
>>> def how_big(x):
...     if x > 10:
...         print('huge')
...     elif x > 5:
...         return 'big'
...     elif x > 0:
...         print('small')
...     else:
...         print("nothing")

Q: What should the function display with how_big(7) ?
A: Actually nothing should be displayed, since 7 > 5 and the function should return 'big' as a whole string.

### Condition judges
What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> positive = 28
>>> while positive: # If this loops forever, just type Infinite Loop
...    print("positive?")
...    positive -= 3

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> positive = -9
>>> negative = -12
>>> while negative: # If this loops forever, just type Infinite Loop
...    if positive:
...        print(negative)
...    positive += 3
...    negative += 3

A: In python, a condition will return turn if the value is 'int', no matter it is positive or negtive. But 0 is an exception since python will treat 0 as False.

## short-circuit
1. False values in python: False, 0, '', None, True values in python: anything else.
2. Evaluation rules has been stated in composingprograms - 1.5.4 in below link:
https://www.composingprograms.com/pages/15-control.html#conditional-statements

PS: If int values are the member of logic evaluations, it will become the output of that evaluation. And the output of such evaluation obey the rules(short-circuiting) stated in composingprograms - 1.5.4. For 'and', if first operand is False, then there is no need to evaluate the next operands. For 'or', if the first operand is True, then there is no need to evaluate the next operands neither.
Examples:
>>> 5 and 0
0
>>> 5 and 10
10
>>> 5 or 10
5
>>> 1 and 5
5
>>> 1 or 5
1
>>> True or 1
True
>>> True and 1
1
>>> 1 and True
True
>>> False and 1
False