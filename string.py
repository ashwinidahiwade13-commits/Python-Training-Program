# String = 'Software'
# print(String)
#
#
# output=sorted(String)
# result=''.join(output)
# print(result)
from itertools import count
from multiprocessing.reduction import duplicate
from unittest import result

# string ='Software Test'
# output1=min(string.split(),key=len)
# print(output1)
# output1=max(string.split(),key=len)
# print(output1)
# list=string.split()
# result=[]
# for i in list:
#     if i not in result:
#         result.append(i[::-1])
# output=''.join(result)
# print(output)

# str='software987654!#$%%^'
# #output=[word for word in str if not word.isalnum()]
# output=[word for word in str if  word.isnumeric()]
# result=''.join(output)
# print(result)


# count=0
# for i in str:
#     if i.isnumeric():
#         count=count+1
#         print(count)

# str='apple mango orange mango'
# list=str.split()
# duplicate=[]
# seen = set()
# for i in list:
#     if i in seen:
#         duplicate.append(i)
#     else:
#         seen.add(i)
# output=''.join(duplicate)
# print(output)

str='software897462534'
# list=sorted(str)
# output=''.join(list)
# print(output)
# alphabet=[]
# numeric=[]
# for i in str:
#     if i.isalpha():
#         alphabet.append(i)
#     else:
#         numeric.append(i)
# output=''.join(sorted(alphabet)+sorted(numeric))
# print(output)


# string = 'Bangalore'
# char_count = {}
# output = ''
#
# for ch in string:
#     char_count[ch] = char_count.get(ch, 0) + 1
#
# for key, value in char_count.items():
#     output = output + key + f"{value}"
#
# print(output)

# string='5n6k7s9w3v2a'
# output=''
# for ch in string:
#     if ch.isdigit():
#         d=int(ch)
#     else:
#         x = ch
#
#         output=output+x*d
# print(output)

