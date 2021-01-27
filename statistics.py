import math

def calculateStats(numbers):
  Nums = {}
  if len(numbers) == 0:
    Nums = dict.fromkeys(['avg','min','max'],math.nan)   #Sets all stats value to Nan for an empty list
  else:
    Nums["avg"] = sum(numbers)/len(numbers)
    Nums["min"] = min(numbers)
    Nums["max"] = max(numbers) 
  return Nums
