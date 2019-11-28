# tuples

tuple1 = ("yellow", 45, True, 0.56, [31, "pizza"], "rice", 56, 56)

list1 = list(tuple1)   # to transform a tuple into a list list()

list1 = tuple(list1)   # to transform a list into a tuple tuple()

print(tuple1[4])       # to access to a part of the tuple

print(45 in tuple1)    # to check if an element is on the tuple

print(tuple1.count(0.56))  # returns how many times is the element on the tuple .count()

print(len(tuple1))         # returns the length of the tuple len()

tuple2 = ("hello",)        # unitary tuple

tuple3 = 23, "yes", 45     # empaquetado de tupla, escribirlas raw, another way to write a tuple

colour, number, boolean, floatt, listt, string, number2, number3 = tuple1   # desempaquetado de tupla, it assign a
# variable to each element o a tuple

print(colour)
print(number)
print(number3)
print(string)
print(boolean)
print(floatt)
print(number2)
print(listt)
