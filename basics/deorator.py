def decorator(func):
    # inside the decorator function we have another function
    def wrapper():
        print('Wrapper up side')
        # now here I call the func
        func()
        print('Wrapper down side')

    # now the decorator needs to return this wrapper
    return wrapper


@decorator
def chocolate():
    print('chocolate')


chocolate()