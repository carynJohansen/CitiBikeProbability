import os, glob, csv
from flaskr import init_db
path = './data/'

def parseTime(time):
  print time
  arr = time.split()
  rtn = arr[0].split('/')
  rtn.append(arr[1].replace(':',''))
  return rtn

init_db()

for filename in glob.glob(os.path.join(path, '*.csv')):
  with open(filename) as csvfile:
    contents = csv.reader(csvfile, delimiter=',');
    first = True
    for row in contents:
      if first:
        first = False
      else:
        startStationId = row[4]
        startStationName = row[5]
        startLat = row[6]
        startLong = row[7]

        endStationId = row[8]
        endStationName = row[9]
        endLat = row[10]
        endLong = row[11]

        startTimeInfo = parseTime(row[1])
        startMonth = startTimeInfo[0]
        startDay = startTimeInfo[1]
        startYear = startTimeInfo[2]
        startTime = startTimeInfo[3]

        endTimeInfo = parseTime(row[2])
        endMonth = endTimeInfo[0]
        endDay = endTimeInfo[1]
        endYear = endTimeInfo[2]
        endTime = endTimeInfo[3]