import numpy as np
import matplotlib.pyplot as plt
from random import random
import math

points_x = []
points_y = []
def rand_cluster(n,r):
    x,y = 0,0
    for i in range(n):
        theta = 2*math.pi*random()
        s = r*random()
        points_x.append(x+s*math.cos(theta))
    	points_y.append(y+s*math.sin(theta))

with open("input_files/mu_x.txt") as mu:
	data = mu.readlines()
mu_x = [float(row.rstrip('\n')) for row in data]
with open("input_files/mu_y.txt") as mu:
	data = mu.readlines()
mu_y = [float(row.rstrip('\n')) for row in data]

def write_into_file():
	with open('input_files/x.txt', 'r+') as the_file:
		the_file.truncate()
		for i in points_x:
			the_file.write(str(i)+'\n')

	with open('input_files/y.txt', 'r+') as the_file:
		the_file.truncate()
		for i in points_y:
			the_file.write(str(i)+'\n')


rand_cluster(100,30)
write_into_file()
plt.scatter(points_x,points_y,c='b',s=70)
plt.scatter(mu_x,mu_y,s=180,marker='^',c="yellow")
plt.savefig('images/input')
