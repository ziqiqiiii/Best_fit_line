import numpy as np
import matplotlib.pyplot as plt
import math

# experiment data
x = [3.03, 0.79, 1.85, 2.12, 4.29, 4.05]
y = [1.3, 0.8, 1.0, 1.1, 1.6, 1.5]

# find the best fit line to the data
fit = np.polyfit(x, y, 1)
# the function polyfit will return the coefficient of the best fit line/curve
# in this case is line
# slope(gradient) and y-intercept is being return as fit
# fit = m, c
f = np.poly1d(fit)
# the 'poly1d' function create a polynomial function from fit coefficients 

x.append(0)
y.append(f(0))
# append y-intercept into the list 

plt.figure(figsize=(10,10.5))
plt.scatter(x, y, label="original experiment data")
# plot the original experiment data 
plt.plot(x, f(x), '-', label="Best fit line")
# plot the best fit line
plt.plot(0, f(0), 'ro', markersize=10, label="y-intercept")
# plot y-intercept
plt.annotate('y-intercept', (0, f(0) + 0.05))


plt.xticks(x, size=10)
plt.yticks(y)
plt.xlim(min(x), max(x) + 0.5)


line_equation = 'f(x) = ' + '{:.2}'.format(fit[0]) + 'x' + ' + {:.2f}'.format(fit[1])
plt.text(0.8, 1.3, line_equation)
plt.xlabel('Current, I (A)')
plt.ylabel('Force, F(N)')
plt.title('2004 Oct/Nov P5', fontsize= 10, fontweight ='bold')


plt.legend()
plt.grid()
plt.show()
