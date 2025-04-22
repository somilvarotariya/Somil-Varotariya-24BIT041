def count_lower_upper(s):
    uppercase = [char for char in s if char.isupper()]
    lowercase = [char for char in s if char.islower()]
    return [len(uppercase),len(lowercase)]
str1 = "How Are You"
s2=count_lower_upper(str1)
print(s2)
    
