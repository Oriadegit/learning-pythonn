
# # def number(num):
# #     #a=num&2
# #     if num&2 == 0:
# #         print(str(num) + ' is an even number')
# #     else:
# #         print(str(num) +' is an odd number')

# # number(8)
# # number(15)


# """listing"""

# # creating and calling list
# from os import remove
# from turtle import clear


# list = ['name','class','color', 'shape','texture']
# # print(list)
# # print(list[1:3])
# # print(len(list))
# # print(type(list))

# # slicing list
# listb = ['Daniel', 'cargo',34.5,34,'atm',1/4]
# # print(listb)
# # print(listb[2:5])

# # list of list
listc = [
    ['mife','erijesu','emma','taiwo','shola'],
    [18, 34,2,9,47,97],
    [23.4,0.3,25.2,98.7],
    [True,False,False]
]
# # print(listc[1])
# # print(listc[0][1])
# # if len(listc)==3:
# #     print('three lists')
# # else:
# #     print('not three')
# # if len(listc[2])>=3:
# #     print('hurray')
# # else:
# #     print('invalid list')

# # updating list
listc[3] = ['holiness','faith','kindness','love','gentleness','meekness','temperance']
listc[0][2]='tijesunimi'
listc[0].append('segun')
listc[0].insert(3,'adewumi')
# # print(listc)
# # print(listc[0])

# #sum of list and others
# # print(sum(listc[1]))
# # print(sum(listc[2]))
# # print(sum(listc[1] + listc[2]))
# # print(max(listc[0]))
# # print(max(listc[2]))
# # print(min(listc[0][0]))

# # delete list

# # listb.remove('atm')
# # print(listb)
# # listb.pop(2)
# # print(listb)
# # del listb[2]
# # print(listb)
# # del listb
# # print(listb)
# # #  or
# # clear(list)

# #loop through a list
# # for x in listc:
# #     print(x)
# # for y in listb:
# #     print(y)
# # for z in listc[0][:3]:
# #     print(z)
# # for a in range(len(listc[0])):
# #     print(listc[3])

# # #using while to loop
# # i=0
# # while i < len(listc[1]):
# #     print(listc[0][1])
# #     i=i+1


# del listb[2:4]
# listb.remove(1/4,)
# print(listb)

# # #add lists together
# list.extend(listb)
# print(list)


# # #list comprehension
# listt=[]
# for t in list:
#     if 'r' in t:
#         listt.append(t)
# print(listt)

# #or

# listtt=[m for m in list if "n" in m]
# # print(listtt)

# #list sort
# listt.sort()
# listc[1].sort()
# listc[2].sort(reverse=True)
# # print(listt)
# # print(listc[1])
# # print(listc[2])

# #customizing list sorting
# def lister(n):
#     return abs(n-40) #customize on how close the number is to 40
# listc[1].sort(key=lister)
# print(listc[1])

# #copy a list
# lista=listc[0].copy()
# print(lista)
# #or (list method-will not work on this page cause the word 'list' has been assign to a certain list)
# # listm=list(listc[4])
# # print(listm)

# #dictionaries
tdict={
    'name':'ewa',
    'sex':'female',
    'height':'165',
    'pname':'sugar',
    'hobbies':['talking','dancing','skiing','swimmiing','cooking']
}
# print(tdict)
# print(tdict['pname'])
# print(tdict['hobbies'][4])
# tdict['complx']='fair'
# tdict['hobbies'][2]='gaming'
# print(tdict)

x=tdict.get('name')
print(x)

#loops
# t = 1
# while t < 5:
#     print(t)
#     t += 1

# j=1
# while j<6:
#     print(j)
#     if j==4:
#         break
#     j += 1

# for r in listc[0]:
#     print(r)

# for t in listc[3]:
#     for x in listc[2]:
#         print(t,x)

# for x in range(6):
#     print(x)

# for f in range(2,4):
#     print(f)

# for h in range(0,18,3):
#     print(h)

