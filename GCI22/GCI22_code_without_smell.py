def run_code():
    a = 10
    b = 3
    x = 5
    y = 8
    n1 = 0b1010
    n2 = 0b1100

    result_add = a + b
    result_sub = a - b
    result_mul = a * b
    result_div = a / b
    result_mod = a % b
    result_pow = a ** b

    is_equal   = x == y
    is_greater = x > y
    is_less    = x < y
    is_gte     = x >= y
    is_lte     = x <= y
    is_not_eq  = x != y

    my_list = [1, 2, 3, 4, 5]
    size = len(my_list)

    words = ["This", "is", "a", "test"]
    found = "test" in words

    first = "Hello"
    last  = "World"
    greeting1 = first + ", " + last
    greeting2 = f"{first}, {last}"

    flag_a = True
    flag_b = False
    result_and = flag_a and flag_b
    result_or  = flag_a or flag_b

    bit_and    = n1 & n2
    bit_or     = n1 | n2
    bit_xor    = n1 ^ n2
    bit_lshift = n1 << 2
    bit_rshift = n1 >> 2

    repeated_str  = "abc" * 3
    repeated_list = [0] * 5

    data     = {"key": 42}
    my_list2 = [10, 20, 30]
    val = data["key"]
    my_list2[1] = 99
    del my_list2[0]

for _ in range(10000):
    run_code()