import numpy as np 

def gini_impurity(a):
  ratio_squared = sum((a/sum(a))**2)
  return 1- ratio_squared