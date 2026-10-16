    #--TO FIND UPPER AND LOWER NUMBER IN STRING----

string = 'SOFTWARE test'
# output=''
# for ch in string:
#     if ch.isupper():
#     if ch.islower():
#         output=output+ch
# print(output)

#---TO CONVERT UPPER NUMBER IN LOWER---
# output=''
# for ch in string:
#     if ch.isupper():
#         output=output+ch.lower()
#     if ch.islower():
#         output=output+ch.upper()
# print(output)

# #---how to remove string data--
# str='software89775'
# output=str.removeprefix('software')
# print(output)

# str='software89775'
# output=str.removesuffix('89775')
# print(output)

#--TO FIND PARTICULAR  ONE DATA IN STRING---
# string=('software')
# output=''
# for i in string:
#     if i =='r':
#         output=output+'$'
#     else:
#         output=output+i
# print(output)

# string='softwaretest'
# vowel='AEIOUaeiou'
# output=''
# for i in string:
#     if i in vowel:
#         output=output+i
# print(output)

#---HOW TO FIND EVEN AND ODD NUMBERS IN  STRING----
# string='one two three four five six seven eight nine'
# list=string.split()
# result=[]
# for i in range(len(list)):
#     if i % 2!=0:
#         result.append(list[i])
#
# output=''.join(result)
# print(output)

#--HOW TO SORT A STRING USING FOR LOOP---
# string='software'
# char=list(string)
# n=len(char)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if char[i]>char[j]:
#             char[i],char[j]=char[j],char[i]
#     output=''.join(char)
# print(output)

#--HOW TO SORT A STRING USING FOR LOOP---
string='software'
ch=list(string)
for i in range(len(ch)):
    for j in range(i+1,len(ch)):
        if ch[i]>ch[j]:
            ch[i],ch[j]=ch[j],ch[i]
    output=''.join(ch)
print(output)

