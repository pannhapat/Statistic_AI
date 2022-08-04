import numpy as np
from scipy import stats

x=np.fromstring('12.848 9.769 5.309 5.335 12.179 5.018 6.707 8.984',dtype = float, sep=" ")

mean_x = np.mean(x)
std_x = np.std(x, ddof=1)
print(mean_x)
print(std_x)

#95 confidence interval
alpha = 0.05
n = x.size
t_a = stats.t.isf(alpha/2, n-1)
std_err = std_x/np.sqrt(n)
margin_err = t_a*std_err
L=mean_x - margin_err
U = mean_x + margin_err
print("{}% confidence interval {:.2f} +- {:.2f} = [{:.2f}, {:.2f}]".format(int((1-alpha)*100),mean_x,margin_err, L,U))
