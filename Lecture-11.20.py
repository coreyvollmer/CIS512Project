
#imported as example from https://stackoverflow.com/questions/22611446/perform-2-sample-t-test
import dataframe as df
import numpy as np
import scipy.stats as ss

np.random.seed(1)

# Create sample data.
label = [i for i in range(1,40)]
a = np.random.randn(40)
b = np.random.randn(40)+3
print(a)
print(b)

# Use scipy.stats.ttest_ind.
t, p = ss.ttest_ind(a, b, equal_var=False)
print("ttest_ind:            t = %g  p = %g" % (t, p))


#get avg and stdev for a and b
avgA = np.mean(a)
avgB = np.mean(b)
print("Average for A: ", avgA,"Average for B: ", avgB)

#get std dev
stdDevA = np.std(a)
stdDevB = np.std(b)
print("Standard Dev for A: ", stdDevA,"Average for B: ", stdDevB)

#example from
#box and whisker plot

import matplotlib.pyplot as plt

#combine data into a two-dimensional array
#data = [a,b]
#plt.boxplot(data)
#plt.show()



aPlusb=[]
for i in label:
    aPlusb.append(a[i]+b[i])

print(aPlusb)

#df = df.DataFrame(data=[a, b, aPlusb], index=label)
#df.cumsum()
#df.plot()

#plt.figure()
