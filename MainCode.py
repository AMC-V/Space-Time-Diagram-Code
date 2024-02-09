import numpy as np
import matplotlib.pyplot as plt
import time
#%matplotlib inline

plt.style.use("dark_background")

def center(ax = None, centerx = 0, centery = 0): # weird i guess we dont need give parameter when calling function since it gets set for us
  fig = plt.figure(figsize=(7,7)) # intizations figure window with size
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
#====================================================
# calls function again and reworks things like adding lines to the existing plot ie plt that was created
center() # having a definition of a function that draws centered axes and labels them above, you will not need to do it again for each plot.

# first we create a matrix
x = np.arange(-12, 12) # probably creates a row matirx with from -12 to 12
y = x # creates a new varible that holds the same information 

# to correctly visuaize the slope the y
y1 = 0.7 * x # so from x's get y's
y2 = 0.7 * x - 3.5

# helps create correct spacing because it plots the x and y in the plot but doesnt show it
plt.plot(x,y,linestyle='') #sizes of the plot and lets the vertical lines have a coordinet system to use
plt.plot(x, y1)
plt.plot(x, y2)
#color = next(ax._get_lines.prop_cycler)['color'] #lets you lock a color for some plots

# need to figure out how this line works
side1 =plt.axvline(x=4,linestyle='--') # creates a vertical line at giving x, needs a values for x and y to work
#plt.gca().set_prop_cycle(None) #resets the cycling through colors, keep this line
side2 =plt.axvline(x=9,linestyle='--')

# don't have your own set_prop_cycle line when you make your additions here

plt.axis('equal') # Sets the aspect ratio of the plot to be equal in both x and y directions. maintains the correct proportions in the plot.
plt.show()