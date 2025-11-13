from typing import Union,List,Tuple,Dict,Optional


count:int=5
# print(count.__add__("5"))


# price: List[int]=[12,13,14]
# price:Tuple[int,int,int]=(1,2,3)
# price:Dict[str,int]={"item":2,"item":300}

# print(price)
# x:List[Union[int,float]]=[1.2,5,5,2.3]
# print(x)

def int_to_usd(value: float):
    try:
        conversion_factor=75
        value=value/conversion_factor
        return value
    except TypeError:
        return None
    
print(int_to_usd(23))

# Image=List[List[int]]
# def flatten_image(pic:Image)->List:
#     flat_list=[]
#     for sublist in image:
#         for item in sublist:
#             flat_list.append(item)
#     return flat_list

# image=[[1,2,3],[4,5,6]]
# print(flatten_image(image))

# class Job:
#     def __init__(self,title:str,description:Optional[str])->None:
#         self.title:title
#         self.description:description
    
#     def __repr__(self):
#         return self.title

# job1=Job(title="Team Lead",description="SDFSD")
# job2=Job(title="Senior Manager",description="jinvd")

# jobs:List[job]=[job1,job2]
