import csv
import csv  

header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']
data_m = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]
rows = [
    {'name': 'Albania',
    'area': 28748,
    'country_code2': 'AL',
    'country_code3': 'ALB'},
    {'name': 'Algeria',
    'area': 2381741,
    'country_code2': 'DZ',
    'country_code3': 'DZA'},
    {'name': 'American Samoa',
    'area': 199,
    'country_code2': 'AS',
    'country_code3': 'ASM'}
]

# 1.
with open('countries.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

# 2.
with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

# 3.
with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

    import csv

# 4.
with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(rows)