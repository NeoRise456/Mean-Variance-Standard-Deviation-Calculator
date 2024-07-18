import numpy as np

def calculate(data:list) -> dict:
    calculations = {
        'mean':[[],[],None],
        'variance':[[],[],None],
        'standard deviation':[[],[],None],
        'max':[[],[],None],
        'min':[[],[],None],
        'sum':[[],[],None]
    }
    
    if len(data) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(data).reshape(3,3)
    
    #matrix[:,numero columna]
    
    #mean
    for i in range(len(matrix)):
        #mean
        calculations['mean'][0].append(np.mean(matrix[:,i]).item())
        calculations['mean'][1].append(np.mean(matrix[i]).item())
        #variance
        calculations['variance'][0].append(np.var(matrix[:,i]).item())
        calculations['variance'][1].append(np.var(matrix[i]).item())
        
        #standard deviation
        calculations['standard deviation'][0].append(np.std(matrix[:,i]).item())
        calculations['standard deviation'][1].append(np.std(matrix[i]).item())
        
        #max
        calculations['max'][0].append(np.max(matrix[:,i]).item())
        calculations['max'][1].append(np.max(matrix[i]).item())
        
        #min
        calculations['min'][0].append(np.min(matrix[:,i]).item())
        calculations['min'][1].append(np.min(matrix[i]).item())
        
        #sum
        calculations['sum'][0].append(np.sum(matrix[:,i]).item())
        calculations['sum'][1].append(np.sum(matrix[i]).item())
    
    #mean
    calculations['mean'][2] = np.mean(matrix.flatten()).item()
    
    #variance
    calculations['variance'][2] = np.var(matrix.flatten()).item()
    
    #standard deviation
    calculations['standard deviation'][2] = np.std(matrix.flatten()).item()
    
    #max
    calculations['max'][2] = np.max(matrix.flatten()).item()
    
    #min
    calculations['min'][2] = np.min(matrix.flatten()).item()
    
    #sum
    calculations['sum'][2] = np.sum(matrix.flatten()).item()
    
    return calculations