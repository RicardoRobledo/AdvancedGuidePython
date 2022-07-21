'''
Created on 9 ene. 2021

@author: RSSpe
'''

import matplotlib
import sys

if 'matplotlib.backends' not in sys.modules:
    matplotlib.use('PS') #The argument passed to the matplotlib.use() function is case sensitive

import matplotlib.pyplot as pyplot

'''It should be noted that if you use the matplotlib.use() function, this must
be done before importing matplotlib.pyplot. Calling matplotlib.use()
after matplotlib.pyplot has been imported will have no effect.'''

# The default renderer is the ‘Agg’
