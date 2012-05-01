def sumUp(aNumber, isSquared):
 if 0 == aNumber:
  return 0
 elif isSquared:
  return aNumber*aNumber + sumUp(aNumber-1, True)
 elif not isSquared:
  return aNumber + sumUp(aNumber-1, False)

if __name__ == "__main__":
 print sumUp(100, False)*sumUp(100, False) - sumUp (100, True)