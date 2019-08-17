from functools import wraps


def make_bold(fn):
    @wraps(fn)
    def wrapped(*args,**kwargs):

        return "<b>"+fn(args,kwargs)+"</b>"
    return wrapped


def make_italic(fn):
    @wraps(fn)
    def wrapped(*args,**kwargs):
        return "i"+fn(args,kwargs)+"i"
    return wrapped

@make_bold
@make_italic
def hello():
    return "hello world"


print(help())