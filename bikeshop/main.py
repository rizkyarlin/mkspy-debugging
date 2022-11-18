from bike import Bike, Condition
from marketing import promote_bike

my_bike = Bike("Red Releigh cruiser", Condition.GOOD, 450, 50)

print(f"popularity: {my_bike.popularity}")
promote_bike(my_bike)
print(f"popularity: {my_bike.popularity}")

# print(my_bike)

# my_bike.update_sale_price(400)
my_bike.service(100)
profit = my_bike.sell()

print(f"Profit for -{my_bike.description}- is {profit}")

# my_bike.update_sale_price(1000)