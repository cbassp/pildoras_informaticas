# Listas

list1 = [1, "hello", 1.7, [0.17, "ham and sugar"]]

print(list1[:])     # [:] to access the whole list

print(list1[0])     # [0] to access to the first element

print(list1[-1])    # [0] to access to the last one element

print(list1[2:])    # [2:] to access to a part of the list

print(list1[1:4])   # [1:4] to access from the first until the fourth element (this one excluded)

list1.append(345)   # to add elements to a list .append() it add the element at the end of the list

list1.insert(1, True)  # to add elements to an index that we choose .insert() we need to specify an index on the method

list1.extend(["tree", False])  # to add several elements to continue the list .extend([]), is like add other list

print(list1.index(1.7))    # Python returns the index of the element in the list .index() if there are the same elements
# on a list Python returns the first one

print('hello' in list1)    # to check if an element is on the list "element_name" in name_of_my_list, it returns True
# or False

list1.remove([0.17, "ham and sugar"])    # to delete an element we use .remove(), before print anything

list1.pop()       # to remove the last element of a list .pop()

list2 = ["burguer", 26] * 3    # * multiply the list

list3 = list1 + list2          # + add both lists
