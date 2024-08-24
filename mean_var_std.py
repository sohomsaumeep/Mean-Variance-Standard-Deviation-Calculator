import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(list).reshape(3,3)
    mean_list, var_list, std_list, max_list, min_list, sum_list = [], [], [], [], [], []  

    for i in range(0,2):
        mean_list.append(np.mean(matrix, axis = i).tolist())
        var_list.append(np.var(matrix, axis = i).tolist())
        std_list.append(np.std(matrix, axis = i).tolist())
        max_list.append(np.max(matrix, axis = i).tolist())
        min_list.append(np.min(matrix, axis = i).tolist())
        sum_list.append(np.sum(matrix, axis = i).tolist())

    mean_list.append(np.mean(matrix))
    var_list.append(np.var(matrix))
    std_list.append(np.std(matrix))
    max_list.append(np.max(matrix))
    min_list.append(np.min(matrix))
    sum_list.append(np.sum(matrix))

    calculations = {
                    'mean': mean_list,
                    'variance': var_list,
                    'standard deviation': std_list, 
                    'max': max_list,
                    'min': min_list,
                    'sum': sum_list
                    }

    return calculations