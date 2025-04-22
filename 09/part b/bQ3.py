c=0
def vowel(s):
    global c
    if s[0] in ('a','e','i','o','u'):
        c=c+1
    if len(s)==1:
        return None
    vowel(s[1::])
vowel("hello world")
print(c)
    
