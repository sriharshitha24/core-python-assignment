def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10 * distance
    total_fare = base_fare + distance_fare
    return total_fare

def total_fare(trips):
    total = 0
    for i, distance in enumerate(trips):
        fare = calculate_fare(distance)
        print(f"Trip {i + 1}: ${fare}")
        total += fare
    print(f"Total Fare: ${total}")

trips = [5, 10, 3] 
total_fare(trips)
