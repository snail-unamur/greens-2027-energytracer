def run_code():
    a = 10
    b = 3
    x = 5
    y = 8
    n1 = 0b1010
    n2 = 0b1100

    result_add = a.__add__(b)
    result_sub = a.__sub__(b)
    result_mul = a.__mul__(b)
    result_div = a.__truediv__(b)
    result_mod = a.__mod__(b)
    result_pow = a.__pow__(b)

    is_equal   = x.__eq__(y)
    is_greater = x.__gt__(y)
    is_less    = x.__lt__(y)
    is_gte     = x.__ge__(y)
    is_lte     = x.__le__(y)
    is_not_eq  = x.__ne__(y)

    my_list = [1, 2, 3, 4, 5]
    size = my_list.__len__()

    words = ["This", "is", "a", "test"]
    found = list.__contains__(words, "test")

    first = "Hello"
    last  = "World"
    greeting1 = first.__add__(", " + last)
    greeting2 = "".join([first, ", ", last])

    flag_a = True
    flag_b = False
    result_and = flag_a.__and__(flag_b)
    result_or  = flag_a.__or__(flag_b)

    bit_and    = n1.__and__(n2)
    bit_or     = n1.__or__(n2)
    bit_xor    = n1.__xor__(n2)
    bit_lshift = n1.__lshift__(2)
    bit_rshift = n1.__rshift__(2)

    repeated_str  = "abc".__mul__(3)
    repeated_list = [0].__mul__(5)

    data     = {"key": 42}
    my_list2 = [10, 20, 30]
    val = data.__getitem__("key")
    my_list2.__setitem__(1, 99)
    my_list2.__delitem__(0)

for _ in range(10000):
    run_code()