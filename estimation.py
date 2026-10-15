def mean_absolute_error(actual, predicted): 
    if len(actual) != len(predicted) or not actual: 
        raise ValueError("Lists must be non-empty and have equal length") 
    return sum(abs(a - p) for a, p in zip(actual, predicted)) / len(actual) 
