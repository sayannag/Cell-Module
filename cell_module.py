import numpy as np

class cell:
    def __init__(self, *args):
        self.args = args
        if len(args)>0:
            self.row = args[0]
            self.column = args[1]
            empty_list = [None]*self.column
            self.data = np.array([empty_list])
            self.mylist = empty_list
            for i in range(0,self.row-1):
                self.data = np.concatenate((self.data, [empty_list]), axis = 0)
        elif len(args) == 0:
            emp_list = []
            self.data = np.array([emp_list])
            self.mylist = emp_list
    
    # used when the dimension of the cell is not predefined and only cell will be of the shape = (1,N)
    def append(self,X): # here X is a matrix, generally
        self.mylist.append(X)
        self.mylist.append([None])
        dummydata = np.array([self.mylist])
        self.data = dummydata[0][0:len(self.mylist)-1]
        self.mylist.pop()
        self.data = np.array([self.data])
        return self.data
        
    def show(self):
        print(self.data)
        
    def insert(self,i,j,X):
        self.data[i][j] = X
        return self.data
    
    def get(self,i,j):
        if i is 'all' and j is not 'all':
            return self.data[:,j]
        elif j is 'all' and i is not 'all':
            return self.data[i,:]
        elif i is 'all' and j is 'all':
            return self.data
        else:
            return self.data[i][j]
    
    def shape(self):
        return self.data.shape
    
    def flatten(self):
        if self.data.shape[0] == 1:
            return self.data
        else:
            n = self.data.shape[0]
            m = self.data.shape[1]
            temp = cell(1,int(n*m))
            k = 0
            for i in range(0,n):
                for j in range(0,m):
                    temp.insert(0,k,self.data[i][j])
                    k = k + 1
            return temp
        
    def tolist(self):
        n = self.data.shape[0]
        if n == 1:
            lis = []
            m = self.data.shape[1]
            for i in range(0,m):
                lis.append(self.data[0][i])
            return lis
        else:
            return self.data.flatten().tolist()
        
    def iscell(self, X):
        if 'cell' in str(type(X)):
            return True
        else:
            return False
        
