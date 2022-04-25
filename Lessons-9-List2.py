#          0    1       2       3       4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

print(cars)

for x in cars:
    print(x.upper())

for x in range(1, 6):
   print(x)

mynumber_list = list(range(0, 10))
#print(mynumber_list)

for x in mynumber_list:
    x =x * 2
    print(x)

mynumber_list.sort(reverse=True)
print(mynumber_list)

print("Max number is:" + str(max(mynumber_list)))


#          0    1       2       3       4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

mycars = cars[1:4]
print(mycars)

#          0    1       2       3       4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

mycars = cars[:] # [:] - do cloning current set

