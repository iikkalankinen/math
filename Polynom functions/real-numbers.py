# Pitkä matematiikka 2 Polynomifunktiot, 2005, authors: Jukka Kangasaho, Jukka Mäkinen, Juha Oikkonen, Johannes Paasonen, Maija Salmela, Jorma Tahvanainen
# Page 15
import math
print('''
Page 15, exercise 14: Which of the following numbers are in between [-4.5, -pi[?
a) -4.5
b) -4.501
c) -4.49999
d) -3.14
e) -(355/113)
f) -pi
''')
options = [-4.5, -4.501, -4.49999, -3.14, -(355/113), -(math.pi)]
for i in options:
    if -4.5 <= i < -(math.pi):
        print(str(i) + " --> true")
    else:
        print(str(i) + " --> false")