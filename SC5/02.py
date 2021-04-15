import string

# '%(key1)d, %(key2)d, ...' % dict
Dic = {'beef noodles': 100, 'dumplings': 60, 'rice': 10, 'vegetable': 40, 'tea': 30, 'juice': 20}
print('Customer: What are you serving today?')
print('Server: We have beef noodles ($%(beef noodles)d), dumplings ($%(dumplings)d), rice ($%(rice)d), \
vegetable ($%(vegetable)d), tea ($%(tea)d), juice ($%(juice)d)' % Dic)

order = input('customer 1: ').split(', ') +\
input('customer 2: ').split(', ') +\
input('customer 3: ').split(', ') +\
input('customer 4: ').split(', ')

Sum = order.count('beef noodles') * Dic['beef noodles'] +\
      order.count('dumplings') * Dic['dumplings'] +\
      order.count('rice') * Dic['rice'] +\
      order.count('vegetable') * Dic['vegetable'] +\
      order.count('tea') * Dic['tea'] +\
      order.count('juice') * Dic['juice']

# using both single quotes and bouble quote to avoid errors
print(f'beef noodles * {order.count("beef noodles")}, \
dumplings * {order.count("dumplings")}, \
rice * {order.count("rice")}, \
vegetable * {order.count("vegetable")}, \
tea * {order.count("tea")}, \
juice * {order.count("juice")}, \
total in ${Sum}')
