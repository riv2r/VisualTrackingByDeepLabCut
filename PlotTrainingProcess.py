import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

xdata = []
ydata = []

with open(r'C:\Users\user\Desktop\XJTUGraduationProject\VisualTrackingByDeepLabCut\test-riv2r-2021-05-16\dlc-models\iteration-0\testMay16-trainset95shuffle1\train\learning_stats.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    xdata = [row[0] for row in reader]
    
with open(r'C:\Users\user\Desktop\XJTUGraduationProject\VisualTrackingByDeepLabCut\test-riv2r-2021-05-16\dlc-models\iteration-0\testMay16-trainset95shuffle1\train\learning_stats.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    ydata = [row[1] for row in reader]

xdata = [float(data) for data in xdata]
ydata = [float(data) for data in ydata]
plt.plot(xdata[:500],ydata[:500],'b-')
plt.xlabel('iters',fontsize=20)
plt.ylabel('loss',fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid()
# plt.axis('equal')
plt.show()