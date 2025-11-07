from array import array
import numpy as np

vals=array('i',[5,10,15,20,25])
vals1=array('I',[30,35,40,45,50])
vals2=array('f',[1.5,2.5,3.5,4.5,5.5])
vals3=array('d',[2.5,3.5,4.5,5.5,6.5])
vals4=array('u',['a','b','c','d','e'])

for i in range(len(vals)):
    print(vals[i])
    
while i < range(len(vals1)):
    print(vals1[i])
    i+=1
    
    
arr=np.array([1,2,3,4,5])
arr1=arr+5
print(arr1)

arr2=np.array([10,20,30,40,50])
arr3=np.array([5,4,3,2,1])
arr4=arr2+arr3
print(arr4)
print(np.concatenate((arr2,arr3)))

