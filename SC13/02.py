class Matrix:
    def __init__(self, data):
        self.List = [list(row) for row in data]
        self._nrows = len(data)
        self._ncolumns = len(data[0])
    def row(self, r):
        # return the r-th row in the form of a list
        # r is from 0.. number of rows
        # in the exmaple above, M.row(1) would return
        # [4, 5, 6]
        return self.List[r]
    def column(self, c):
        # retun a the c-th column in the form of a list.
        # in the example above, M.column(2) would return
        # [3, 6, 9]
        ret = []
        for row in self.List:
            ret.append(row[c])
        return ret
    @property
    def nrows(self):
        return self._nrows
    @property
    def ncolumns(self):
        return self._ncolumns
    def __getitem__(self, ij):
        # return the matrix element at ij, where ij is a tuple
        # for the (row, column). For example above,
        i, j = ij
        return self.List[i][j]
    def __setitem__(self, ij, val):
        # assign the value to the matrix as ij, where ij is
        # a tuple for (row, column)
        i, j = ij
        self.List[i][j] = val
    def transpose(self):
        # return a new Matrix whose content is same as this
        # Matrix except the row and column positions are
        # switched. In the example above,
        # M.transpose() would return
        # Matrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        # Note: use zip() to do the transpose
        return Matrix(list(zip(*self.List)))
    def randomize(self):
        # return another matrix whose content is the same as
        # this matrix except their positions are randomized.
        print('Ran')
    def __matmul__(self, other):
        # return the matrix product for the two matrices A B
        # p[i,j] = sum(A[i,k] * B[k,j]) for 0 <= k <=
        #　A.ncolumns where A.ncolumns must be == B.nrows
        print('Pro')

M = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])