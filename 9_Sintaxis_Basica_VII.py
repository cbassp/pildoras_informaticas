# Diccionarios

new_dictionary = {"Germany": "Berlin", "France": "Paris", "UK": "London", "Spain": "Madrid"}

print(new_dictionary["Germany"])  # To acces to a element of that dictionary

print(new_dictionary)  # To access to the full dictionary

new_dictionary["Italy"] = "Lisbon"  # To add a new element to my dictionary

new_dictionary["Italy"] = "Roma"  # To modify a value that we attached to a key

del new_dictionary["UK"]  # To delete an elemet from the dictionary

new_dictionary_2 = {"UK": "London", 23: "Jordan", "Mosqueteros": 3}  # Dictionary with differents types

tuple1 = ("Spain", "France", "UK", "Germany")  # Use elements of a tuple as keys, I declare a tuple then each index can
# be a key
new_dictionary_3 = {tuple1[0]: "Madrid", tuple1[1]: "Paris", tuple1[2]: "London", tuple1[3]: "Berlin"}
print(new_dictionary_3["Germany"])  # You can access to the dictionary in these forms
print(new_dictionary_3[tuple1[3]])  # You can access to the dictionary in these forms

# New dictionary with a tuple inside
dictionary_tuple = {23: "Jordan", "Name": "Michael", "Team": "Chicago", "Rings": (1991, 1992, 1993, 1996, 1997, 1998)}

# A dictionary inside another dictionary
dictionary_tuple2 = {
    23: "Jordan", "Name": "Michael", "Team": "Chicago",
    "Rings": {"Seasons": (1991, 1992, 1993, 1996, 1997, 1998)}}
# PEP-8 recommends you indent lines to the opening parentheses if you put anything on the first line, so it should
# either be indenting to the opening bracket

# Other interesting methods for the dictionaries; .keys(); .values(); len()
print(dictionary_tuple.keys())  # Output all keys for the dictionary

print(dictionary_tuple.values())  # Output all values for the dictionary

print(len(dictionary_tuple))  # Lenght of my dictionary
