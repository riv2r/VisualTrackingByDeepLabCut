import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r'C:\Users\user\Desktop\XJTUGraduationProject\VisualTrackingByDeepLabCut\test-riv2r-2021-04-20\videos\test1DLC_resnet_50_testApr20shuffle1_5000.csv')

xdata = []
ydata = []
xdata = data.loc[2:,'DLC_resnet_50_testApr20shuffle1_5000'].values
ydata = data.loc[2:,'DLC_resnet_50_testApr20shuffle1_5000.1'].values
xdata =[float(x) for x in xdata]
ydata = [float(x) for x in ydata]
plt.plot(xdata,ydata,'b-',linewidth=1)
plt.axis('equal')
plt.show()