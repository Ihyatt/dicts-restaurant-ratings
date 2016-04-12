# your code goes here
def alphabetize_restaurants(path):
    path_file = open(path)
    restaurants = {}

    for line in path_file:
        line_split = line.rstrip()
        line_split2 = line_split.split(":")
        for item in line_split2:
            restaurants[line_split2[0]] = line_split2[1]


    sorted_restaurant = sorted(restaurants)
    
    for restaurant_name in sorted_restaurant:
        print restaurant_name, "is rated at", restaurants[restaurant_name]



alphabetize_restaurants("scores.txt")