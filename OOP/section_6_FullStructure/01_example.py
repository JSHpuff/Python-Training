from abc import ABC

class Currency_Converter(ABC):
    def convert(self, from_currency, to_currency, amount) -> float:
        pass

class FX_Converter(Currency_Converter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using FX API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.15
    
class Alpha_Converter(Currency_Converter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using Alpha API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2
    
class App:
    def __init__(self, converter: Currency_Converter):
        self.converter = converter
    
    def start(self):
        self.converter.convert('EUR', 'USD', 100)

if __name__ == "__main__":
    converter = Alpha_Converter()
    app = App(converter)
    app.start()