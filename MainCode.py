import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

plt.style.use("dark_background")

def center(ax = None, centerx = 0, centery =0):
  fig = plt.figure(figsize=(7,7))
  ax = plt.gca()

  # Move left y-axis and bottim x-axis to centre, passing through (0,0)
  ax.spines['left'].set_position('center')
  ax.spines['bottom'].set_position('center')

  # Eliminate upper and right axes
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')

  # Show ticks in the left and lower axes only
  ax.xaxis.set_ticks_position('none') #coomment out this line to get x-axis marks
  ax.xaxis.set_ticklabels('') # comment out this line to get x-axis values
  ax.xaxis.set_label_coords(1.0,0.45)
  ax.xaxis.set_label_text('$x$',fontsize=16)

  ax.yaxis.set_ticks_position('none')
  ax.yaxis.set_ticklabels('')
  ax.yaxis.set_label_coords(0.55,1.0)
  ax.yaxis.set_label_text('$ct$',fontsize=16)
