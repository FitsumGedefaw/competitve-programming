class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        result = []

        Kevin = celsius + 273.15
        Fahrenheit = celsius *1.80 +32.00
        result.append (Kevin)
        result.append (Fahrenheit)

        return result