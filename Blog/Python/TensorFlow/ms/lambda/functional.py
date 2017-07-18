"""functional utilities
"""


def is_false(arg): return not arg


def is_true(arg): return not is_false(arg)


def is_sequence(arg):
    t = type(arg)
    return t is list or t is tuple or t is str


def is_dict(arg):
    t = type(arg)
    return t is dict


def each(seq, func):
    if (is_false(seq)): return

    if is_sequence(seq):
        [func(x) for x in seq]
    elif is_dict(seq):
        [func(x) for x in seq.values()]


def curry(func):
    def func_a(*a):
        def func_b(*b):
            return func(*(a+b))
        return func_b
    return func_a


def curryr(func):
    def func_a(*a):
        def func_b(*b):
            return func(*(b+a))
        return func_b
    return func_a


def map(obj, func):
    if not is_sequence(obj): return []
    _iter = obj
    if is_dict(obj): _iter = obj.values()

    return [func(x) for x in _iter]


def filter(obj, pred):
    if not is_sequence(obj): return []
    _iter = obj
    if is_dict(obj): _iter = obj.values()

    return [x for x in _iter if pred(x)]


def reject(obj, pred):
    return filter(obj, lambda x: not pred(x))


def reduce(obj, func, start):
    if not is_sequence(obj): return None
    acc = start

    def reducer(x):
        nonlocal acc
        acc = func(acc, x)

    each(obj, reducer)
    return acc


def pipe(*args):
    def runner(arg):
        return reduce(list(args), lambda acc, func: func(acc), arg)
    return runner;


def go(*args):
    start = args[0]
    rest = args[1:]
    return pipe(*rest)(start)


def has_key(obj, key):
    if not is_dict(obj): return False
    return True if key in obj.keys() else False


def get(obj, key):
    if not is_dict(obj): return None
    return obj[key] if has_key(obj, key) else None

def all(arg, pred):
    if not is_sequence(arg): return False
    for x in arg:
        if not pred(x):
            return False
    return True

def any(arg, pred):
    if not is_sequence(arg): return False
    for x in arg:
        if pred(x):
            return True
    return False

def sum(arg):
    if not is_sequence(arg): return None
    return reduce(arg,lambda a,b: a+b,0)





