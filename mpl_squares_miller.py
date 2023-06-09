import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)

# Creating the Chart Title and the labels for the chart
ax.set_title("Squre Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Setting the size of the tickes for the graph
ax.tick_params(axis="both", labelsize=14)

plt.show()