#Indexing

#Indexing

# string

x = "small"
print(x[3])

# list
x = ['pig', 'horse', 'aapie']
print(x[1])

#tuple

x = ('kim', 'makes', 'Juo', 'Creed')
print(x[3])

# Slicing

x = 'computer'

print(x[1:4])
print(x[1:6:2])
print(x[3:])
print(x[:5])
print(x[-1])
print(x[-3:])
print(x[:-2])

# string concat
x= 'horse' + 'shoe'
print(x)

# list
c = ['pop', 'out'] + ['in it', 'for glory']
print(c)

# tuple
z = ('Keloo', 'Amazon') + ( 'Aloutaba',)
print(z)

# string

x = 'bug'*4
print(x)

# list
f = [8, 5] * 3
print(f)
# tuple

x = (3, 5) * 2
print(x)

# testing membership

# string
x = 'hug'
print('u' in x)

#list
y = ['piffer', 'cone', 'hey ya']
print('cone' not in y)

# tuple will yield a Boolean

z = ('Kevin', 'Sisanda', 'Juluka', 'Ambeso')
print('Ambeso' not in z)

# itreration is a sequence
x = [2,5,8,3]
for item in x:
    print(item)

# index & item
y = [2, 5,8,3]
for index, item in enumerate(y):
    print (index, item)

# number of items - count the number of items

#string
x = 'mug'
print(len(x))

# list
y = {'pigeon', 'inkomu', 'lala'}
print(len(y))

# tuple
z = ("Kabawo", "Naxola", 'Jean', 'Khaloma')
print(len(z))

# minimum in a sequence
x = 'bugging'
print(min(x))

#list
y = ['poorly','connect', 'haze']
print(min(y))

# tuple
y = ('Kinakonke', 'Khazin', 'Jeppers', 'Crayons')
print(min(y))

# maximum item in a sequence- lexicographically

#string
x = 'bowin'
print(max(x))

#list
y = ['piggy', 'kool', 'hp']
print(max(y))

#tuple

z = ('koko', 'miol', 'kerr','craig')
print(max(z))

# summing items in a sequence

# string -> error
# x - [5,8,'no']
# print (sum(x))...generates an error

# list
x = [3,8,12,9]
print(sum(x))
print(sum(x[-3:]))

# tuple
z = (30, 6, 2, 90)
print(sum(z))
