import re
text = "The rain in Spain"

#Search for a sequence that starts with "ra":
x = re.findall("ra.", text)

print(x)
print(type(x))


# Return a list containing every occurrence of "ai" in the string:
x = re.findall("ai", text)

print(x)

# Return a list containing every occurrence of "a" or "e" in the string:
x = re.findall("[ae]", text)

print(x)