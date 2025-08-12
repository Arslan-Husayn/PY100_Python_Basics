cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city != None:
        print(len(city))
    else:
        continue

#not using the else here 

terry = ['terry', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in terry:
    if city is None:
        continue

    print(len(city))
