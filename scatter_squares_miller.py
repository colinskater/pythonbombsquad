import matplotlib.pyplot as plt

# X values and Y values for the graph
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# Styling the graph 
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues,s=10)

# Creating the labels for the graph
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Setting the range for the graph or either axis
ax.axis([0, 1100, 0, 1100000])

# Set the size of the ticks of the graph
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()