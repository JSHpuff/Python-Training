class TemperatureConverter:
    @staticmethod
    def celsius2fahrenheit(c):
        return 9 * c / 5 + 32
    @staticmethod
    def fahrenheit2celsius(f):
        return 5 * (f - 32) / 9
    
f = TemperatureConverter.celsius2fahrenheit(30)
print(f)