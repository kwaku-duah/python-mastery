class Restaurant:
    """ a model for a restaurant"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name} and cuisine type is {self.cuisine_type}")


    def open_restaurant(self):
        print('The restaurant is OPEN!')
    
    def set_number_served(self, num):
        self.number_served = num

    def increase_number_served(self,new):
        self.number_served += new

        
restaurant = Restaurant('Nsuomunam','seafood')
restaurant.set_number_served(45)
restaurant.increase_number_served(45)

print(f"Name of restaurant is {restaurant.restaurant_name} and food served here is {restaurant.cuisine_type} and {restaurant.number_served} have been served today"
        f"{restaurant.number_served} have been served today")


restaurant_1 = Restaurant('Mickey','Van Bruisen')
restaurant_1.number_served = 23_500
print(f"name is restaurant {restaurant_1.restaurant_name} and {restaurant_1.cuisine_type} and {restaurant_1.number_served} customers have been served today")

restaurant.describe_restaurant()
restaurant.open_restaurant()