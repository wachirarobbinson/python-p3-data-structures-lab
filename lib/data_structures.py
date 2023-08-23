spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(food_list):
    names = [food['name'] for food in food_list]
    return names


def get_spiciest_foods(food_list):
    spiciest_foods = [food for food in food_list if food['heat_level'] > 5]
    return spiciest_foods


def print_spicy_foods(food_list):
    for food in food_list:
        heat_level = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")


def get_spicy_food_by_cuisine(food_list, cuisine):
    for food in food_list:
        if food['cuisine'] == cuisine:
            return food
    return None


def print_spiciest_foods(food_list):
    for food in food_list:
        if food['heat_level'] > 5:
            heat_level_emojis = "🌶" * food['heat_level']
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")


def get_average_heat_level(food_list):
    total_heat_level = sum(food['heat_level'] for food in food_list)
    average_heat_level = total_heat_level / len(food_list)
    return average_heat_level


def create_spicy_food(food_list, new_food):
    new_spicy_foods = food_list.copy()
    new_spicy_foods.append(new_food)
    return new_spicy_foods
