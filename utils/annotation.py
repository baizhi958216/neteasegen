def log(info:str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(info+'...')
            result = func(*args, **kwargs)
            print(info+'完成!')
            return result
        return wrapper
    return decorator