import os, datetime, csv, sqlite3

#Functions

def parse_time_column( x, date = True, start = True, ):
	#x is a row from a csv
	# the start time column is the second column
	if start == True:
		col_index = 1
	else:
		col_index = 2

	if date == True:
		part_index = 0
		part1 = x[col_index].partition(' ')[part_index]
		part2 = part1.split('-')
	else:
		part_index = 2
		part1 = x[col_index].partition(' ')[part_index]
		part2 = part1.replace(":", "")

	return part2

def dow(triprow):
	date = parse_time_column(triprow)
	print date
	dow = datetime.date(date[0], date[1], date[2]).weekday()
	return dow

def get_year(triprow, start = True):
	date = parse_time_column(triprow, date=True, start = start)
	year = date[0]
	return year

def get_month(triprow, start = True ):
	date = parse_time_column(triprow, date=True, start = start)
	month = date[1]
	return month

def get_day(triprow, start = True):
	date = parse_time_column(triprow, date=True, start=start)
	day = date[2]
	return day

# def db_connect():


# def populate_table(table, data):


#Main

if __name__ == '__main__':

	filename = '2014-04-Citi Bike trip data.csv'

	stations = []
	trips = []

	with open(filename, 'rw') as f:
		content = csv.reader(f, delimiter=",")
		firstline = True
		for row in content:
			if firstline:
				firstline = False
				continue
			trip=[]
			trip.append(get_year(row, start=True))
			trip.append(get_month(row, start=True))
			trip.append(get_day(row, start=True))
			trip.append(parse_time_column(row, date=False, start=True))
			trip.append(get_year(row, start=False))
			trip.append(get_month(row, start=False))
			trip.append(get_day(row, start=False))
			trip.append(parse_time_column(row, date=False, start=False))
			trip.append(row[4])
			trip.append(row[8])
			trip.append(dow(row))

			trips.append(trip)

	print len(trips)
	print trips[1:3]