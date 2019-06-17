 """
 everything you make is child of "Object"
        Object #God Class
        int str Customer



"""
#class CA:
#class CA():
class CA (object):
    pass

"""class CB(CA):
    pass
"""
cRef = CA()
print("Object Data:", cRef.__dict__)
print("Class Data:", CA.__dict__)
#print("CB class Data:", CB.__dict__)
