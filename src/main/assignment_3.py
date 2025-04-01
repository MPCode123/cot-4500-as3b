import numpy as np 

def GaussAndBack(A,b):
            n = len(A)
            # Convert A,b to augmented matrix
            aug_matrix = np.hstack([A, b.reshape(-1, 1)])

            for i in range(n):
                # Partial Pivoting: Swap rows if needed
                max_row = i
                max_val = abs(aug_matrix[i][i])
                
                for k in range(i + 1, n):
                    if abs(aug_matrix[k][i] > max_val):
                        mas_val = abs(aug_matrix[k][i])
                        max_row = k
            
                # Make the pivot 1 (row normalization)
                pivot = aug_matrix[i, i]
                if pivot == 0: # Failsafe if divide by 0
                    print("Can't Divide by 0")
                aug_matrix[i] = aug_matrix[i] / pivot
            
            # Make zeros below pivot
                for j in range(i + 1, n):
                    factor = aug_matrix[j][i]
                    aug_matrix[j] = aug_matrix[j] - (factor * aug_matrix[i])

            # Back Substitution
            x = np.zeros(n)
                                        
            for i in range(n-1, -1, -1):
                x[i] = aug_matrix[i][-1]
        
                for j in range(i+1, n):
                    x[i] = x[i] - aug_matrix[i][j] * x[j]

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
                
            if (diagonal < non_diagonal_sum):
                print("The matrix is NOT diagonally dominant")
            else:
                print("The matrix is diagonally dominant")
                
def Positive_Definite(A):
            if (A == A.T).all():
                if (np.all(np.linalg.eigvals(A) > 0)):
                    print("The matrix is positive definite")
                else:
                    print("The matrix is NOT positive definite")

