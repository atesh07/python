import matplotlib.pyplot as plt

# Data
x = [1, 1, 1,0.98,1.01,0.98,1]
y = [1, 1.8, 6,3,3,5.5,1 ]
#star pattern 
# Create plot
plt.plot(x, y)

# Labels
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Simple Line Plot")

# Show graph
plt.show()
