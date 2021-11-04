'''
Given a string s with length greater than 2, return a new string where the first and last letter are the same, but the letters in between are replaced by their length.
Example 1
Input
s = "croneberry"
Output
"c8y"
Example 2
Input
s = "extracurricular"
Output
"e13r"
'''



s = input(" ")
len_of_s = len(s)
first_let = s[0]
last_let_index = len_of_s-1
last_let = s[last_let_index]

# make new string
letter_to_append = len_of_s - 2
new_s = first_let + str(letter_to_append) + last_let
print(new_s)