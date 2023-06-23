#Write a decorator with 1 argument = limit, specifying number of times the decorated callable can be called.
# If limit is exceeded raise RuntimeError on call. 


def call_limit_decorator(limit):
    def decorator_func(func):
        calls_counter = 0

        def wrapper(*args, **kwargs):
            nonlocal calls_counter
            if calls_counter >= limit:
                raise RuntimeError(f"Call limit of {limit} exceeded")
            calls_counter += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator_func


@call_limit_decorator(5)
def fun(a):
    print("Hello, world!")
    return a
    

print(fun(2))
fun(2)
fun(2)
fun(2)
fun(2)
fun(2)
