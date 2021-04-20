import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv


xdata = []
ydata = []

with open(r'C:\Users\user\Desktop\XJTUGraduationProject\VisualTrackingByDeepLabCut\test-riv2r-2021-04-20\dlc-models\iteration-0\testApr20-trainset95shuffle1\train\learning_stats.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    xdata = [row[0] for row in reader]
    
with open(r'C:\Users\user\Desktop\XJTUGraduationProject\VisualTrackingByDeepLabCut\test-riv2r-2021-04-20\dlc-models\iteration-0\testApr20-trainset95shuffle1\train\learning_stats.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    ydata = [row[1] for row in reader]

xdata = [float(data) for data in xdata]
ydata = [float(data) for data in ydata]
plt.plot(xdata[:100],ydata[:100],'b+-',linewidth=1)
# plt.axis('equal')
plt.show()