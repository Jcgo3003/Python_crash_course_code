# 8-14. Cars: Write a function that stores information about a car in 
# a dictionary. The function should always receive a manufacturer and 
# a model name. It should then accept an arbitrary number of keyword 
# arguments. Call the function with the required information and two 
# other name-value pairs, such as a color or an optional feature. 
# Your function should work for a call like this one:

def cars(manufacturer, model , **car_details):
	car_details["Manufacturer"] = manufacturer
	car_details["Model"] = model
	return car_details

car = cars('subaru', 'outback', color='blue', tow_package=True)
print(car)
