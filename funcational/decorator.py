#装饰器
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*arg, **kwarg):
            print('%s()' % (func.__name__) if callable(text) else \
                      '%s %s():' % (text, func.__name__))
            return func(*arg, **kwarg)
        return wrapper
    return decorator(text) if callable(text) else decorator

@log
def now():
    print('Current local time：' + get_now_local_time())
now()

print('==' * 50)

@log('execute current the function')    # 为函数添加带参数装饰器
def now():
    print('Current local time：' + get_now_local_time())
now()
