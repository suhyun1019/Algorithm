def numJewelsInStones(self, jewels: str, stones: str) -> int:
  sum = 0
  
  for stone in stones :
    if stone in jewels :
      sum+=1
     
  return sum

"""

def numJewelsInStones(self, jewels: str, stones: str) -> int :
  
    return sum(stone in jewels for stone in stones)
    
"""
