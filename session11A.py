"""
Inheritance Types:
1. Single Level
2. Multi Level
3. Hierarchy
4. Multiple
5. Hybrid

take use case zomato and explore the onheritance in it except hybrid

find if there is a role of _ and__ that is protected and private
"""

# Single Level
class A:
    pass

class B(A):
    pass

# Multi Level
class C(B):
    pass
#Heirarchy
class D(A):
    pass

#Multiple
class E:
    pass
class F(A,E):
    pass

#Hybrid
class G(F):
    pass



