'''
Created on 14 ene. 2021

@author: RSSpe
'''

import matplotlib.pyplot as pyplot

# Set up the data
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 2, 6, 14, 30, 43, 75]

# Set the title
pyplot.title("Speed v Time")

# Set the axes headings
pyplot.ylabel('Speed', fontsize=12)
pyplot.xlabel('Time', fontsize=12)

# Plot and display the graph
# Using blue circles for markers ('bo')
# and a solid line ('-')

'''
b—this indicates the colour to use when drawing the line; in this case the letter
‘b’ indicates the colour blue (in the same way ‘r’ would indicate red and ‘g’
would indicate green).

o—this indicates that each marker (each point being plotted) should be represented by a cirlce. The lines between the markers then create the line plot.

‘–’—This indicates the line style to use. A single dash (‘-’) indicates a solid line,
where as a double dash (‘–’) indicates a dashed line.
'''

pyplot.plot(x, y, 'bo-')
pyplot.show()

# There are numerous options that can be provided via the format string, the following
# tables summarises some of these: The following colour abbreviations are supported by
# the format string:

'''
Character | Color
-----------------
‘b’       | blue
‘g’       | green
‘r’       | red
‘c’       | cyan
‘m’       | magenta
‘y’       | yellow
‘k’       | black
‘w’       |white
'''

# Different ways of representing the markers (points on the graph) connected by
# the lines are also supported including:

'''
Character | Description
--------------------------------
‘.’       | point marker
‘,’       | pixel marker
‘o’       | circle marker
‘v’       | triangle_down marker
‘^’       | triangle_up marker
‘ < ’     | triangle_left marker
‘ > ’     | triangle_right marker
‘s’       | square marker
‘p’       | pentagon marker
‘*’       | star marker
‘h’       | hexagon1 marker
‘ + ’     | plus marker
‘x’       | x marker
‘D’       | diamond marker
'''

# Finally, the format string supports different line styles:

'''
Character | Description
--------------------------------
‘-’       | solid line style
‘–’       | dashed line style
‘-.’      | dash-dot line style
‘:’       | dotted line style
'''
