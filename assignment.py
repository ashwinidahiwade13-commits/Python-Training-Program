# list=[1,2,3,4,45,5,6,7,7,1]
# duplicate_list=[]
# seen=set()
# for i in list:
#         if i in seen:
#             duplicate_list.append(i)
#         else:
#             seen.add(i)
#
# print('list=',list)
# print('duplicate_list=',duplicate_list)


#---

# dict={'apple':'fruits',
#       'dog':'animals',
#       'cat':'animals',
#       'mango':'fruits',
#       'red':'colour'}
# output={}
# for key,value in dict.items():
#     if value not in output:
#         output[value]=[]
#     output[value].append(key)
# print(output)

#--TO FIND MAX ELEMENT IN A LIST---

list=[1,2,3,4,5,6,7,8,9,10]
max=list[0]
for num in list:
     if num>max:
         max=num
print(max)

#--TO FIND MIN ELEMENT IN A LIST---
min=list[0]
for num in list:
     if num<min:
         min=num
print(min)


