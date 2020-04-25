# Cell-Module
# Creates a python cell array using numpy
# Some examples:
A = cell(5,5) # creates a 5 x 5 cell array
A.insert(0,0,4)
A.insert(2,0,'s')
A.get(0,0) # output is 4
A.show()
'''
Output is:

[[4 None None None None]
 [None None None None None]
 ['s' None None None None]
 [None None None None None]
 [None None None None None]]
 
'''
A.flatten().show() # for flattening
'''
Output is:
[[4 None None None None None None None None None 's' None None None None
  None None None None None None None None None None]]
'''
A.iscell(A) # True
A.iscell(cell(1,3)) # True
A.iscell('s') # False
A.iscell(1) # False
A.iscell(np.array([1,2])) # False
A.iscell(np.zeros((4,4))) # False
A.iscell(np.zeros((5,5))) # False
A.iscell(np.zeros((1,1))) # False
A.iscell([1,2,3,4,5]) # False
