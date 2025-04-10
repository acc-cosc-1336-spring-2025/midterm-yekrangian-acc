def reverse_string(string1):
    reversed_str = ""
    index = len(string1) - 1
    while index >= 0:
        reversed_str += string1[index]
        index -= 1
    return reversed_str 
