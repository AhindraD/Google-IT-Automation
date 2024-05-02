class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)


'''
__str__ special method controls how your object is converted to a string representation for output.
When you print() something, Python calls the object’s __str__() method 
and outputs whatever that method returns. In most cases, 
the default output is just the class name and a memory location:

print(honeycrisp)
<__main__.Apple object at 0x7ffa68d78970
'''

honeycrisp = Apple("red", "sweet")
print(honeycrisp)

'''
__len__ returns the length of the object or collection.

__contains__ tests whether the object contains an item.

__eq__ tests whether two objects are equal.
'''
