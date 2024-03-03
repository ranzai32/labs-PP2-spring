# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

# Write a Python program to find sequences of lowercase letters joined with a underscore.

# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

# Write a python program to convert snake case string to camel case string.

# Write a Python program to split a string at uppercase letters.

# Write a Python program to insert spaces between words starting with capital letters.

# Write a Python program to convert a given camel case string to snake case.
import re
# ex 1
text = "ab a0b"
x = re.findall(r'(ab|a[0])', text)
print(x)

# ex 2
text = "abbb abbb abb abc abd"
x = re.findall(r'abb|abbb', text)
x = re.findall(r'ab{2,3}', text)
print(x)

# ex 3
text = "aaaa_a_a aaa A_A"
x = re.findall(r"[a-z]_[a-z]+",text)
print(x)

# ex 4
text = "Aaaaaa aaaa"
x = re.findall(r"([A-Z][a-z]+)",text)
print(x)

# ex 5
text = "asdsdb"
x = re.search(r"a.*?b$",text)
print(x)

# ex 6
text = "dsds hello.ds jdjfs,dsds"
x = re.sub(r"[ ,.]", ":", text)
print(x)

# ex 7
test = "_ggg_sd_ff_midka"
list = re.split(r"[_]+", test)
result = ""
for x in list:
    result += x.capitalize()
print(result)


# ex 8
result = ""
test = "aaAAsBBBdsdsdCCCdsDDD"
list = re.split(r"[A-Z]",test)
for x in list:
        if x != "":
            result += x
    
print(result)

# ex 9
test = "SplitStringOooGood"
resub = re.sub(r"(\w)([A-Z])", r"\1 \2", test)
print(resub)

# ex 10
test = "helloWorld_world"
snake_case = re.sub(r'([a-z])([A-Z])', r'\1_\2', test).lower()
print(snake_case)



