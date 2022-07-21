'''
Created on 7 ene. 2021

@author: RSSpe
'''

import matplotlib.pyplot as pyplot
# Plot a sequence of values

pyplot.plot([1, 0.25, 0.5, 2, 3, 3.75, 3.5])
# Display the chart in a window
pyplot.show()

'''In this example, the plot() function takes a sequence of values which will be
treated as the y axis values; the x axis values are implied by the position of the y
values within the list. Thus as the list has six elements in it the x axis has the range
0–6. In turn as the maximum value contained in the list is 3.75, then the y axis
ranges from 0 to 4.'''
