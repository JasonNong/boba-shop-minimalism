list_of_items = ['drink', 'topping', 'size', 'sugar',
    'ice']
order = []
for item in list_of_items:
    request = input(f'What {item} would you like?\n')
    order.append(f'{item}: {request}')
for i in order:
    print(i)