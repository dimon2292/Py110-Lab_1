
list_cities = [str(input('введите список городов')) for i in range(3)]

print(list_cities)
print(min(list_cities, key= len))

