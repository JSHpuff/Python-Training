def division(a, b):
    try:
        return {
            'success': True,
            'message': 'OK',
            'result': a/b
        }
    except Exception as e:
        return {
            'success': False,
            'message': 'b cannot be zero',
            'result': None
        }
    
result = division('10', '2')
print(result)