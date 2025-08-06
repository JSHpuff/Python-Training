class Payroll:
    def __init__(self, length):
        self.length = length
    
    def __len__(self):
        print('Len was called...')
        return self.length

payroll = Payroll(0)
print(bool(payroll))

payroll.length = 10
print(bool(payroll))

