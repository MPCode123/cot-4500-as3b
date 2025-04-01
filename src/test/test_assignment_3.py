import sys
import os

# For using functions from assignment_3 to test in test_assignment_3
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.main.assignment_3 import *

print("Question 1: Gaussian Elimination and Backward substitution")

A = np.array([[2,-1,1],[1,3,1],[-1,5,4]])
b = np.array([6,0,-3])

GaussAndBack(A,b)
print("\n")

print("Question 2: LU Factorization")
M = np.array([[1,1,0,3],[2,1,-1,1],[3,-1,-1,2],[-1,2,3,-1]])

LU_Factor(M)
print("\n")

print("Question 3: Determine if the matrix is diagonally dominate")
N = np.array([[9,0,5,2,1],[3,9,1,2,1],[0,1,7,2,3],[4,2,3,12,2],[3,2,4,0,8]])

Diagon_Domin(N)
print("\n")

print("Question 4: Determine if the matrix is positive definite")
O = np.array([[2,2,1],[2,3,0],[1,0,2]])

Positive_Definite(O)
