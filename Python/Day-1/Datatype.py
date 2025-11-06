list=[1,3,"nvkdv",7.5,True]
print(type(list))
print(list)
print(list[2])
print(list[1:4])
print(list)
print(len(list))
print(type(list[3]))
print(list*2)

list[0]=100
print(list)
list.append("hello")
print(list)
list.insert(2,"aniket")
print(list)
list.remove(7.5)
print(list)
x=list.pop()
print(x)
print(list)
list.append(7.5)
print(list)


set={1,"nvd",3.5,True}
set1={1,2,3,4,5,6,7,8}
print(type(set))
set.add("hello")
print(set)
set.add(3)
print(set)
set.remove(3.5)
print(set)
set.add(3)
print(set)
set.update(set1)
print(set)
set1.remove(5)
print(set1)
# set.remove(0)
set.discard(0)
print(set)


tuple=(1,3,"nvkdv",7.5,True)
tuple1=(1,2,3,4,5,6,7,8)
print(type(tuple))
print(tuple)
print(tuple[2])
print(tuple[1:4]) 
print(len(tuple))
tuple2=tuple+tuple1
print(tuple2)
print(tuple)

a,b,c,d,e=tuple
print(b)


dict={"name":"aniket","age":21,"is_student":True}
print(type(dict))
print(dict)
dict["age"]=22
print(dict)
print(dict["name"])
print(dict.get("name"))
dict.pop("is_student")
print(dict)
del dict["age"]
print(dict)

