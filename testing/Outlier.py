import numpy as np
import matplotlib
import seaborn as sns
from matplotlib import pyplot, pyplot as plt
# sort the data
# calculate q1 and q3
# IQR (q1-q3)
# find the lower fence (q1-1.5(IQR))
# find the higher fence (q1 + 1.5(IQR))

# sort the data
dataset=[11,10,12,14,12,15,14,13,15,102,12,14,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]
sorted_data = sorted(dataset)
print(sorted_data)

# calculate q1 and q3
q1,q3=np.percentile(dataset,[25,75])
print(q1,q3)

#IQR
IQR=q3-q1
print(IQR)

# find the lower fence & higher fence
lower_fence=q1-(1.5*IQR)
higher_fence=q3+(1.5*IQR)
print(lower_fence,higher_fence)

sns.boxplot(dataset)
