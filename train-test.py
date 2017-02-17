#!/bin/py
import csv

def split_dataset(filename):
	user_dict = {}
	with open(filename) as fin:
		#fin.next()
		for line in fin:
			linearray = line.strip().split(',')
			user_id = linearray[0]
			#print user_id
			if user_id in user_dict:
				user_dict[user_id].append(linearray)
			else:
				user_dict[user_id] = [linearray]
	
	train_file = open("train.csv",'wb')
	test_file = open("test.csv",'wb')
	train_writer = csv.writer(train_file, delimiter = ",")
	test_writer = csv.writer(test_file, delimiter = ",")
	
	for user in user_dict:
		length = len(user_dict[user])
		if(length>2):
			train_length = int(length*0.8)
			test_length = length - train_length
			for i in range(train_length):
				row = user_dict[user].pop()
				#print row
				train_writer.writerow(row)
			for i in range(test_length):
				row = user_dict[user].pop()
				#print type(row)
				test_writer.writerow(row)
				
		else:
			for i in length:
				train_writer.writerow(user_dict[user].pop())
				
if __name__ == "__main__":
	split_dataset("Data_TripAdvisor_v1.csv")