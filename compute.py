def compute_mean(values): 
    if not values: 
        raise ValueError("Values must not be empty") 
    return sum(values) / len(values) 
