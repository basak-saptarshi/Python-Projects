import numpy as np

def calculate(list_data):
    if len(list_data) != 9:
        raise ValueError ("List must contain nine numbers.")
    arr1 = np.array(list_data)
    arr2 = arr1.reshape(3,3)

    mean = np.mean(arr2)
    column_mean = np.mean(arr2, axis = 0)
    row_mean = np.mean(arr2, axis = 1)

    std = np.std(arr2)
    column_std = np.std(arr2, axis = 0)
    row_std = np.std(arr2, axis = 1)

    var = np.var(arr2)
    column_var = np.var(arr2, axis = 0)
    row_var = np.var(arr2, axis = 1)

    max = np.max(arr2)
    column_max = np.max(arr2, axis = 0)
    row_max = np.max(arr2, axis = 1)

    min = np.min(arr2)
    column_min = np.min(arr2, axis = 0)
    row_min = np.min(arr2, axis = 1)

    sum = np.sum(arr2)
    column_sum = np.sum(arr2, axis = 0)
    row_sum = np.sum(arr2, axis = 1)

    result = {
            'mean': [column_mean , row_mean, mean ],
            'variance': [column_var , row_var, var ],
            'standard deviation': [column_std , row_std, std ],
            'max': [column_max , row_max, max ],
            'min': [column_min , row_min, min ],
            'sum': [column_sum , row_sum, sum ]
            }
    
    return result



calculate([0,1,2,3,4,5,6,7,8])

