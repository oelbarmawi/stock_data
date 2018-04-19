import sys
import csv

def main():
	filename = sys.argv[1]
	with open(filename, encoding='utf-8') as file:
		reader = csv.reader(file)
		for row in reader:
			if len(row) >= 15:
				print(row[10])
				high = row[9]
				low = row[8]
				percent_diff = round(abs(high - low) / ((high + low) / 2) * 100, 2)



if __name__ == '__main__':
	main()