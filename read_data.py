import sys
import csv

def main():
	account_size = 5000
	percent_diff_list = []
	info = {}
	filename = sys.argv[1]

	print("-"*50)
	with open(filename, encoding='utf-8') as file:
		reader = csv.reader(file)
		for row in reader:
			if len(row) >= 15:
				try:
					message = ""
					high = float(row[11])
					low = float(row[12])
					symbol = row[0]
					shares = str(account_size // high)
					percent_diff = round(abs(high - low) / ((high + low) / 2) * 100, 2)
					percent_diff_list.append(percent_diff)
					message = "[{}]\tPercent Difference: {}% --> Entry ${}".format(symbol, percent_diff, high)
					message += "\n\tVolume: " + row[9]
					message += "\n\tNumber of shares: " + shares
					info[percent_diff] = message
				except ValueError:
					pass

	for p in sorted(percent_diff_list, reverse=True):
		print(info[p])
		print("-"*50)

if __name__ == '__main__':
	main()

