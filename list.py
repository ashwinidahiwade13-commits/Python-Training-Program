#list = [1,2,3,4,5,6,7,8,9,10]
# list.append(10)
# list.append(11)
# list.reverse()
# list.sort()
# list.remove(10)
# list.pop(0)
# print(list)
#list = [1,2,3,4,5,6,7,8,9,10]
# output = [num **2 for num in list if num % 2==0] #formula for square numbers and even or odd also
# print(output)
# list = [1,2,3,4,5,6,7,8,9,10]
# max=list[0]
# for num in list:
#     if num>max:
#         max=num
# print(max)
from operator import add
from unittest import result

#--Count Numbers using for loop--
# list=[1,2,3,4,5,6,7,8,9,10,11,12,45,65,87,90]
# print(sum(list))

#-- find Duplicates elements in list--
# list=[1,2,3,4,5,6,7,8,9,10,10,4,7]
# duplicate_list=[]
# seen=set()
# for i in list:
#     if i in seen:
#         duplicate_list.append(i)
#     else:
#         seen.add(i)
# print('list=',list)
# print('duplicate_list=',duplicate_list)

# list1=[1,1,2,2,3,3,4,5,6]
# output=set(list1)
# print(output)
#How to find alternates in a list
# list =[12,34,57,78,91,90,21]
# output=list[0::2]
# result=[num **2 for num in output]
# print(result)

# list=['Ashu','Sanu','Shree','Tush','Raaj','Ashish']
# output=[word[0] for word in list]
# result=''.join(output)
# print(result)

# list=['##','###','####','#','###']
# list.sort(key=len,reverse=True)
# print(list)

#--How to find prime number--
# Number=int(input('Enter the prime number:'))
# for i in range(2,Number):
#     if Number%i==0:
#         print('This is not prime number:')
#         break
# else:
#     print('This is prime Number:')


#--SET--> stores unique elements

# set={1,2,3,4,5,6,7,8,9,10}
# print(set)
# set.add(11)
# set.remove(11)
# set.pop()
# print(set)
# set1=set.copy()
# print(set1)

# tuple=(1,2,3,4,5,6,7,8,9,10)
# print(tuple)
# print(tuple.count(10))
# tuple.index(4)
# print(tuple)


#--Dictionary--
# dict={'Name':'Ashu','RollNo':1234,'Address':'Pune'}
# #for i in dict.keys():
# #print(dict['RollNo'])#--to print particular parameter from dict
# #print(dict['Name'])
# #print(dict['Address'])
# dict['Mobile No']=9020304050#-->To add new parameter in dict
# dict['Address']='Mumbai'#-->To update
# del dict['Name']
# dict.pop('Address')
# print(dict)

Student = {
    'Student1': {'Name': 'Ashwini', 'RollNo': 1234, 'Address': 'Pune'},
    'Student2': {'Name': 'Sanika', 'RollNo': 12345, 'Address': 'Mumbai'}
}
print(Student['Student1'])
#print(Student['Student2'])
Student['Student1']['mobileNo']=9010203040  #-->tO ADD NEW KEY AND VALUE IN DICT
print(Student['Student1'])
del Student['Student1']['Address']  #-->TO DELETE PARTICULARE KEY VALUE FROM DICTIOANRY
print(Student['Student1'])

#print(Student)














