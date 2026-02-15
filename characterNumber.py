"""
Task3. Write a function that calculates the number of characters included in given string
• input: "hello"
• output: {"h":1, "e":1, "l":2, "o":1}
"""
def number_character(string : str = "") -> dict[str,int]:
    dict1 = {}
    for i in string:
        if (i in dict1):
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1  # type: ignore

# Test
str1 = "hello  aaahhh"
print(number_character())
print(number_character(str1))