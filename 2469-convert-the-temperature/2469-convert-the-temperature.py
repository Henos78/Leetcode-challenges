class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
    
        k= 273.15 + celsius
        f = (celsius*1.80)+32.00
        return [k,f]