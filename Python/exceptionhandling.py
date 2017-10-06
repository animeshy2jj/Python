def exceptionhandling(a,b):
    try:
        return (a/b)
    except Exception as e:
        return (e)
print(exceptionhandling(1,0))
