import numpy as np
import matplotlib.pyplot as plt
from random import random
import math

with open("input_files/x.txt") as fx:
	data = fx.readlines()
x = [float(row.rstrip('\n')) for row in data]
with open("input_files/y.txt") as fy:
	data = fy.readlines()
y = [float(row.rstrip('\n')) for row in data]

with open("output_files/group_out.txt") as group:
	data = group.readlines()
gr = [int(row.rstrip('\n')) for row in data]


with open("output_files/mu_x_out.txt") as mu:
	data = mu.readlines()
mu_x_out = [float(row.rstrip('\n')) for row in data]
with open("output_files/mu_y_out.txt") as mu:
	data = mu.readlines()
mu_y_out = [float(row.rstrip('\n')) for row in data]


plt.scatter(x,y,c=gr,s=70)
plt.scatter(mu_x_out,mu_y_out,s=180,marker='^',c="yellow")
plt.savefig('images/output')


