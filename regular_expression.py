##########################################
# regular expressions
##########################################


"""
* Match 0 or more
+ Match 1 or more
? Match 0 or 1
$ Match the end of a string
^ Match the beginning of a string
\A string starting point
\Z string ending point
| either or
{m, n} repeat from m to n times
[] range; e.g. [A-Z] any one from A-Z; [1-5A-Za-z]
{x} expecting "x" amount
() group

\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
. any character except for a newline
\. a period
\b the whitespace around words; e.g. \b(cat)\b contain the word 'cat'

White space characters:
\n new line
\s space
\t tab
\e escape
\f from feed
\r return

Escape special characters with \ if you want to use them:
. + * ? [ ] $ ^ ( ) { } | \


"""

import re

re.match()
re.search()
re.findall()

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''

ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)

print(ages)
print(names)

ageDict = {}
x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1

print(ageDict)
