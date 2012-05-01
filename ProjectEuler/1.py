class IsMultipliedClass():
   def by3(self, number):
      if 0 == number % 3: 
         return True
      else:
         return False
   def by5(self, number):
      if 0 == number % 5:
         return True
      else:
         return False

if __name__ == "__main__":
   theSum = 0
   myClass = IsMultipliedClass()
   for number in range(1, 100000):
      if myClass.by3(number) or myClass.by5(number):
         theSum += number
   print "theSum for 1000 = " + str(theSum)
