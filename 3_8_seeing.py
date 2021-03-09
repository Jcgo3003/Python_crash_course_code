places = ["London", "Madrid", "Paris", "Alicante"]

print(f"Lista de lugares a visitar {places}")

# Lista en orden alfabetico de forma temporal
print(sorted(places))
print(places)

# Using sorted reversed
print("Using sorted reversed")
print(sorted(places, reverse=True))

print(places)

# Using reverse 
print("Using reverse")
places.reverse()
print(places)

# Using reverse to get back to the original order
print("Using reverse to get back to the original order")
places.reverse()
print(places)

# Using sort
print("Using sort")
places.sort()
print(places)

# Using sorting reverse True
print("Using sorting reverse True")
places.sort(reverse=True)
print(places)