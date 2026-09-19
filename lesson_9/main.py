import matplotlib.pyplot as plt

days   = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
scores = [70, 85, 60, 90, 75]

plt.plot(days, scores,color='green',marker='o',linestyle='dashed')
plt.title("satvik")
plt.xlabel("days of week")
plt.ylabel("score")

plt.show()
