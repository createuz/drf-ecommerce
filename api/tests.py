from django.test import TestCase

# Create your tests here.
d = [
    ('8:00', '10:00'),
    ('14:00', '15:00'),
    ('15:10', '15:45'),
    ('17:00', '17:30')
]

print(f'00:00 -> {d[0][0]}')

results = [f'{d[i - 1][1]} -> {d[i][0]}' for i in range(1, len(d))]
print(*results, sep='\n')

print(f'{d[-1][-1]} -> 23:59')
