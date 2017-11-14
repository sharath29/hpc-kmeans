import numpy as np
import matplotlib.pyplot as plt

with open("x.txt") as fx:
	data = fx.readlines()
x = [float(row.rstrip('\n')) for row in data]

with open("group_out.txt") as group:
	data = group.readlines()
gr = [int(row.rstrip('\n')) for row in data]

with open("y.txt") as fy:
	data = fy.readlines()
y = [float(row.rstrip('\n')) for row in data]

with open("mu_x_out.txt") as mu:
	data = mu.readlines()
mu_x_out = [float(row.rstrip('\n')) for row in data]
with open("mu_y_out.txt") as mu:
	data = mu.readlines()
mu_y_out = [float(row.rstrip('\n')) for row in data]
with open("mu_x.txt") as mu:
	data = mu.readlines()
mu_x = [float(row.rstrip('\n')) for row in data]
with open("mu_y.txt") as mu:
	data = mu.readlines()
mu_y = [float(row.rstrip('\n')) for row in data]



# fig = plt.figure()
# ax1 = fig.add_subplot(111)

# ax1.set_title("Plot title")    
# ax1.set_xlabel('x label')
# ax1.set_ylabel('y label')


# ax1.plot(x,y,'bo',c='b')
# ax1.plot(mu_x,mu_y,'r^',ms=10)

# leg = ax1.legend()

# plt.show()

while 1:
	print "\ninput graph:1\noutput graph:2\n"
	temp = int(input())
	if temp == 1:
		plt.scatter(x,y,c='b',s=70)
		plt.scatter(mu_x,mu_y,s=180,marker='^',c="yellow")
		plt.show()
	else:
		plt.scatter(x,y,c=gr,s=70)
		plt.scatter(mu_x_out,mu_y_out,s=180,marker='^',c="yellow")
		plt.show()

