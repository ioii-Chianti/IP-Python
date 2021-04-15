import string

Dic = {'beef noodle': 100, 'dumpling': 60, 'rice': 10, 'vegetable': 40, 'tea': 30, 'juice': 20}
print('Customer: What are you serving today?')
print('Server: We have beef noodle ($%(beef noodle)d), dumpling ($%(dumpling)d), rice ($%(rice)d), \
vegetable ($%(vegetable)d), tea ($%(tea)d), juice ($%(juice)d)' % Dic)

order = input('customer 1: ').split(', ') +\
input('customer 2: ').split(', ') +\
input('customer 3: ').split(', ') +\
input('customer 4: ').split(', ')

Sum = order.count('beef noodle') * Dic['beef noodle'] +\
      order.count('dumpling') * Dic['dumpling'] +\
      order.count('rice') * Dic['rice'] +\
      order.count('vegetable') * Dic['vegetable'] +\
      order.count('tea') * Dic['tea'] +\
      order.count('juice') * Dic['juice']

print(f'You ordered beef noodle * {order.count('beef noodle')}, \
dumpling * {order.count('dumpling')}, \
rice * {order.count('rice')}, \
vegetable * {order.count('vegetable')}, \
tea * {order.count('tea')}, \
juice * {order.count('juice')}, \
total in ${Sum}')

