from dataclasses import dataclass, field


# DataClass-→ designed to hold data values and doesn’t contain methods but could have
# typically used to store information that will passed between differents part of a programme with init method already implemented in the background along couple of other methods

class personclass():
    def __init__(self,name,age,height,email):
        self.name=name 
        self.age=age
        self.height=height
        self.email=email
        


@dataclass(order=True)
class person:
    sort_index: int =field(init=False, repr=False)
    name:str="shaimaa"
    age:int =30
    height:float = 1.75
    email:str="shaimaagamal666@gmail.com"
    def __post_init__(self):
        self.sort_index=self.age

# ===================================================================================================================================

personC=personclass("shaimaa",40,1.8,"shaimaa@gmail.com")
person1=person("shaimaa",40,1.8,"shaimaa@gmail.com")



# When attempting to print this, it displays a reference. 
# To improve the output and display attributes instead, the __repr__() dunder method needs to be overridden.
print(personC)


#  but this dataclasee can handle printing without overriding
print(person1)

# ==============================================================================================================================================





# the second advanatage for dataclass is comparsion
# because equal operator by defult compare reference so dunder method has to be  overrided to compare based on approach i want 
#  def __eq__(self,other)
personC2=personclass("shaimaa",40,1.8,"shaimaa@gmail.com")
personC3=personclass("shaimaa",40,1.8,"shaimaa@gmail.com")
print(personC2 == personC3)


#  in dataclase this method is implemented in background
person3=person("shaimaa",40,1.8,"shaimaa@gmail.com")
person4=person("shaimaa",40,1.8,"shaimaa@gmail.com")
print(person3 == person4)


# ==============================================================================================================================================

# There is an attribute called order, which is set to False by default. 
# To enable it (True), the dataclass automatically implements comparison methods like __lt__, __le__, and __gt__.

# To define a specific attribute for sorting, we import the field library. 
# Otherwise, the dataclass defaults to ordering by the first attribute.
person3=person("shaimaa",40,1.8,"shaimaa@gmail.com")
person4=person("shaimaa",50,1.8,"shaimaa@gmail.com")
print(person3 < person4)


# ===========================================================================================================================================================

# The frozen attribute is set to False by default. 
# When enabled (True), it prevents modification of attribute values, making the dataclass immutable.