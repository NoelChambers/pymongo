###	test.py
###	Illustrating comprehension of basic pymongo skills
###	Noel Chambers - 13 JAN 2015

import pymongo
from collections import Counter
import csv

# Open a connection
try:
	conn = pymongo.Connection()
	print "Connected sucessfully!!"
except pymongo.errors.ConnectionFailure, e:
	print "Could not connect to MongoDB: %s" % e

db = conn.customers

# Drop old collection
db.user_record.drop()

# Ingest the CSV file
with open('MOCK_DATA.csv') as f:
	records = csv.DictReader(f)
	db.user_record.insert(records)

# build a cursor filled with country names from the database using the find() function
cursor = db.user_record.find({}, ['country'])

# Count the number of users from a given country 
counts_by_country = Counter(str(user['country']) for user in cursor)

# iterate through the cursor and report counts
for x in counts_by_country:
	print "{} users from {}".format(counts_by_country[x], x)

# Some final reporting
print '\n\nTotal number of records processed: ', db.user_record.count()
print 'End script\n'
