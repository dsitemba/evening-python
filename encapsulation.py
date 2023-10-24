#Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of

class Robot(object):
   def init(self):
      self.version = 22

   def getVersion(self):
      print(self.version)

   def setVersionself,version):
      self.version =version

obj = Robot()
obj.getVersion()
obj.setVersion(23)
obj.getVersion()
print(obj.version)