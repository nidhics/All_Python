# Python program for
# Creation of Arrays
import numpy as np
 
# # Creating a rank 1 Array
# arr = np.array([1, 2, 3])
# print("Array with Rank 1: \n",arr)
 
# # Creating a rank 2 Array
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])
# print("Array with Rank 2: \n", arr)
 
# # Creating an array from tuple
# arr = np.array((1, 3, 2))
# print("\nArray created using "
#       "passed tuple:\n", arr)

# --------------------------------------------------------------------------
# Initial Array

# [[(0,0), (0,1),(0,2),(0,3)],
# [(1,0),(1,1),(1,2),(1,3)]]

arr2 = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr2)
 



# Printing a range of Array
# with the use of slicing method
sliced_arr = arr2[:2, ::2]
print ("Array with first 2 rows and"
    " alternate columns(0 and 2):\n", sliced_arr)
 
# Printing elements at
# specific Indices
Index_arr = arr2[[1, 1, 0, 3], 
                [3, 2, 1, 0]]
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", Index_arr)