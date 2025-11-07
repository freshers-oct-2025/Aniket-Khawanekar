def person(name, age):
    print("Name:", name)
    print("Age:", age)



person("Aniket", 24)
person(age=24, name="Aniket")
person(name="Aniket", age=24)
person("Aniket", age=24)

def person1(name,*data):
    print("Name:", name)
    print(item)
    
    
def person2(name,**data):
    print("Name:", name)
    for key,value in data.items():
        print(f"{key}: {value}")

person1("Aniket", 24, "Engineer", "India")
person2("Aniket", age=24, profession="Engineer", country="India")
