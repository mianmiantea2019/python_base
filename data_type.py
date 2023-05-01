a = 42             # integer
b = 3.14           # float
c = 2 + 3j        # complex number 
print(a, type(a))
print(b, type(b))
print(c, type(c))


my_list = [1, 2, 3]              # list
my_tuple = (4, 5, 6)             # tuple
my_range = range(0, 10, 2)   # range object
print(my_list, type(my_list))
print(my_tuple, type(my_tuple))
print(my_range, type(my_range))


my_string = "Hello, World!"    # string

my_dict = {"name": "John", "age": 30, "city": "New York"}    # dictionary
print(my_dict, type(my_dict))

my_set = {1, 2, 3}            # set
my_frozenset = frozenset({4, 5, 6})   # frozenset
print(my_set, type(my_set))
print(my_frozenset, type(my_frozenset))


my_bool = True            # boolean value
print(my_bool, type(my_bool))

my_bytes = b"hello"              # bytes object
my_bytearray = bytearray(b"world")   # bytearray object
print(my_bytes, type(my_bytes))
print(my_bytearray, type(my_bytearray))

