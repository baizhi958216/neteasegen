def log(keywords):
    def decorate(fn):
        print(keywords)
        return fn
    return decorate