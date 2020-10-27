#https://web.facebook.com/permalink.php?story_fbid=994669841008275&id=100013958058927
import math

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
