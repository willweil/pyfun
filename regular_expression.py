##########################################
# regular expressions
##########################################

'''
Identifiers:

\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
. any character except for a newline
\. a period
\b the whitespace around words

Modifiers:
{1,3} we're expecting 1-3 \{1,3}
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ Match the end of a string
^ Match the beginning of a string
| either or
[] range or 'variance' [1-5A-Za-z]
{x} expecting "x" amount

White space characters:
\n new line
\s space
\t tab
\e escape
\f from feed
\r return

Don't forget!:
. + * ? [ ] $ ^ ( ) { } | \
if you want to use them, you have to escape them with \

'''

import re

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
