import pandas as np
import numpy as np
from scipy import stats

pm_df = pd.read_csv('Developer/data/pm25.csv')

x = pm_df['PM2.5']
alpha = 0.05
n = x.size

t_a = t.isf(alpha/2, n-1)
std_x = np.std(x, ddof=1)
mean_x = np.mean(x)
std_err = std_x/np.sqrt(n)
margin_err = t_a *std_err
L= mean_x - margin_err
U = mean_x + margin_err

print("{}% confidence interval {:.2f} +- {:.2f} = [{:.2f}, {:.2f}]".format(int((1-alpha)*100),mean_x,margin_err, L,U))

print("Relative precision:{:.2f}%".format(margin_err*100/np.abs(mean_x)))


