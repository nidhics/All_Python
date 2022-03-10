import re
from unittest import result
str="This meeting will bill till be conducted on 1st and 21st of every month. meeting 9412163480"
str2="9412163489"
str1="one two three four five six seven 8 9 10"

# patt= re.compile(r'^meet') 

# result=patt.findall(str)
# x = re.search(r"^Th",str )

# result=re.findall(r"[a-z]ill",str)
result=re.findall(r"[7-9]\d{9}$",str)
print(result)

# for match in result:
#     print(match)s