from typing import List


class Solution:
    def convertTemperature(celsius: float) -> List[float]:
        return[celsius+273.15, celsius*1.80+32.00]
        
print(Solution().convertTemperature(36.50))