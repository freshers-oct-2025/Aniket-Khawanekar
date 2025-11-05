import array

# list=[1,2,3,4,5,6,7]

# for i in list:
#     print(i)

tuple={"afvd","aniket","nvkdv","aniket"}

ar=array.array('i',[10,11,12,13,14,15,16,17,18,19,20])
print(ar)
for i, val1 in enumerate(ar):
    print("i",val1)
    for j, val2 in enumerate(ar):
        print("j",val1)
        if val1 == val2 and i != j:
            print(i, j)
    
for i in range(10):
    print(i)

print( enumerate(tuple))

# str="abba"
# s=0 
# e=len(str)-1
# isPalindrome=True
# while s<e:
#     if(str[s]!=str[e]):
#         isPalindrome=False
#         break
#     s+=1
#     e-=1

# if(isPalindrome!=False):
#     print("palindrome")
# else:
#     print("not palindrome")

