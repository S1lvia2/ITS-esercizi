class Restaurant:
    def __init__(self, restaurant_name : str, cuisine_type:str ):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} è aperto! ")


restaurant = Restaurant("Il mare in tavola", "Mediterranea")

restaurant.describe_restaurant()
restaurant.open_restaurant()

    
