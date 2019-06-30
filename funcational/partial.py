#偏函数 固定函数的默认值
import functools
int2 = functools.partial(int, base=2)
max2 = functools.partial(max, 10)
