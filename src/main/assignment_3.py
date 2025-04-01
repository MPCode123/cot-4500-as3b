import numpy as np 

def GaussAndBack(A,b):
            x = np.linalg.solve(A,b) # Solve matrix equation

            print(x) # Solution
            
def LU_Factor(A):
            n = len(A)
            
            L = np.eye(n) # L = matrix with 1's on diagonals with 0's below it
            U = A.astype(float)
            
            for i in range(n):
                for j in range(i+1,n):
                    factor = U[j,i] / U[i,i]
                    L[j,i] = factor
                    U[j] -= factor * U[i]
            
            print("Part A:", np.linalg.det(U)) # Matrix Determinent
            print("Part B:\n", L) # L 
            print("Part C:\n", U) # U
            
def Diagon_Domin(A):
            n = len(A)
            for i in range(n):
                diagonal = abs(A[i,i]) # Represents numbers diagonal in any matrix
                non_diagonal_sum = np.sum(np.abs(A[i])) - diagonal # Sum of other numbers in that row
                
            if (diagonal < non_diagonal_sum): # If the absolute value of diagonal is less than sum of other row entries
                print("The matrix is NOT diagonally dominant")
            else:
                print("The matrix is diagonally dominant")
                
def Positive_Definite(A):
            if (A == A.T).all(): # If matrix is symmetric, do this...
                if (np.all(np.linalg.eigvals(A) > 0)): # If the eigenvalues are positive
                    print("The matrix is positive definite")
                else:
                    print("The matrix is NOT positive definite")

