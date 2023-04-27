import numpy as np
import pandas as pd

list = []

for i in range(9):
    i = float(input("Insert a float number: "))
    list.append(i)
print(list)



matrix = np.reshape(list, (3,3))
print(matrix)


def calculate(M):
    mean, meanC, meanR = np.mean(matrix), np.mean(matrix, axis = 0).tolist(), np.mean(matrix, axis = 1).tolist()
    var, varC, varR = np.var(matrix), np.var(matrix, axis = 0).tolist(), np.var(matrix, axis = 1).tolist()
    std, stdC, stdR = np.std(matrix), np.std(matrix, axis = 0).tolist(), np.std(matrix, axis = 1).tolist()
    max, maxC, maxR = np.max(matrix), np.max(matrix, axis = 0).tolist(), np.max(matrix, axis = 1).tolist()
    min, minC, minR = np.min(matrix), np.min(matrix, axis = 0).tolist(), np.min(matrix, axis = 1).tolist()
    sum, sumC, sumR = np.sum(matrix), np.sum(matrix, axis = 0).tolist(), np.sum(matrix, axis = 1).tolist()
    
    mean_dic = [meanC, meanR, mean]
    var_dic = [varC, varR, var]
    std_dic = [stdC, stdR, std]
    max_dic = [maxC, maxR, max]
    min_dic = [minC, minR, min]
    sum_dic = [sumC, sumR, sum]
    



    
          

    dictionary = {'mean': mean_dic,
                  'variance': var_dic,
                   'standard deviation': std_dic,
                    'max': max_dic,
                     'min': min_dic,
                      'sum': sum_dic
                        }
    

    return dictionary

solve = calculate(matrix)

print(solve)

