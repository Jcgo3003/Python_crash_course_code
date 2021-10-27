import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	next = next(reader) 
	print(header_row)
	print(next)

# for index, column_header in enumerate(header_row):
# 	print(index, column_header)