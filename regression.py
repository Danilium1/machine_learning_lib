def predict_linear(x, slope=1.0, intercept=0.0):  
    return [slope * value + intercept for value in x] 
