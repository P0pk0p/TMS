def counter(func):
    def wrapper(*args, **kwargs):
        result = func((*args, **kwargs)) # вызов фукнци
        return result
    return  wrapper

def create_list(count:int)
    result []
    for i in range(1, count +1)
        result.append(i)
    return result


