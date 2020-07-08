import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if (self.h==1 and self.w==1):
            return self.g
        else:
            determinant = self.g[0][0]*self.g[1][1]-self.g[0][1]*self.g[1][0]
            return determinant

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace = 0
        for row in range(len(self.g)):
            trace += self.g[row][row]
        
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
#         print('Debug start')
        if(len(self.g)==1):
            val = self.g[0][0]
            inv = Matrix([[1/val]])
            return inv
        else:
            det = self.determinant()
#             print('det= ',det)
            
            det_inv = 1/det
#             print('det_inv= ',det_inv)
            
            trace_self = self.trace()
#             print('trace_self= ',trace_self)
            
            iden = identity(len(self.g))
#             print('iden= ',iden)
            
            tr_a_x_iden = trace_self * iden
#             print('tr_a_x_iden= ',tr_a_x_iden)
            
            tr_a_x_iden_min_A = tr_a_x_iden-self
#             print('iden_x_A_min_A= ',tr_a_x_iden_min_A)
            
            inv = det_inv * tr_a_x_iden_min_A
            
            return inv

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transpose = [ [ [] for row in range(len(self.g))] for col in range(len(self.g[0]))]
        print('len(transpose)= ', len(transpose))
        for row in range(len(self.g)):
            r_s = self.g[row]
            for i in range(len(r_s)):
                print('i= ',i)
                transpose[i][row] = r_s[i]
        
#         print(transpose)
        return Matrix(transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        summation = []
        for row in range(len(self.g)):
            result = []
            for col in range(len(self.g[0])):
                result.append(self.g[row][col]+other.g[row][col])
            summation.append(result)
        return Matrix(summation)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        negation = []
        for row in range(len(self.g)):
            result = []
            for col in range(len(self.g[0])):
                result.append(self.g[row][col]*-1)
            negation.append(result)
        return Matrix(negation)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        subtraction = []
        for row in range(len(self.g)):
            result = []
            for col in range(len(self.g[0])):
                result.append(self.g[row][col]-other.g[row][col])
            subtraction.append(result)
        return Matrix(subtraction)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
#         multiplication = [ [ [] for col in range(len(other.g[0])) ] for row in range(len(self.g)) ]
        multiplication = []
        for r_s in range(len(self.g)):
            row = self.g[r_s]
            res_dot_mult = []
            for c_o in range(len(other.g[0])):
                col = []
                for r_o in range(len(other.g)):
                    col.append(other.g[r_o][c_o])
                
                res_it = 0
                for it in range(len(row)):
                    res_it += row[it]*col[it]
                    
                res_dot_mult.append(res_it)                     
            multiplication.append(res_dot_mult)
        return Matrix(multiplication)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            output = [ [ [] for col in range(len(self.g[0]))] for row in range(len(self.g))]
            for row in range(len(self.g)):
                for col in range(len(self.g[0])):
                    output[row][col] = other * self.g[row][col]
            
            return Matrix(output)
            