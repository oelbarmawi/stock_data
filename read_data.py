import sys
import csv
from tkinter import *


ACCOUNT_SIZE = 5000
root = ''
num_refreshes = 0
"""
	main() loads the column names of each entry in the table.

Args:
    None
Returns:
	None
"""
def main():
	global root
	root = Tk()
	root.title("Stock Info")

	# Set up Labels
	# use 'sticky=(N, S, E, or W)' argument for alignment 
	symbol_label = Label(root, text="Symbol")
	symbol_label.grid(row=0, column=0)

	pd_label = Label(root, text="Percent Difference")
	pd_label.grid(row=0, column=1)

	entry_label = Label(root, text="Entry Price")
	entry_label.grid(row=0, column=2)

	entry_label = Label(root, text="Number of Shares")
	entry_label.grid(row=0, column=3)

	target_label = Label(root, text="Target Price")
	target_label.grid(row=0, column=4)

	stop_loss_label = Label(root, text="Stop Loss Price")
	stop_loss_label.grid(row=0, column=5)
	
	open_file()

"""
	open_file() checks the command line arguments for an excel filename
and opens it with csv filereader.

Args:
    None
Returns:
	None
"""
def open_file():
	filename = sys.argv[1] if len(sys.argv) > 1 else print("Please enter filename.")
	if not filename:
		sys.exit()

	with open(filename, encoding='utf-8') as file:
		reader = csv.reader(file)
		get_data(reader)

"""
	get_data(...) will parse through the excel document and compute
the percent difference between the highest and lowest price of the 
stock value of the day for each stock. It will then store it into the
'info' dictionary with key being the percent difference and the value 
being the stock's data.

Args:
    reader (csv.reader): The csv reader for this excel document.
Returns:
	None
"""
def get_data(reader):
	percent_diff_list = []
	info = {}

	for row in reader:
		if len(row) >= 15:
			try:
				details = []
				high = round(float(row[11]), 2)
				low = round(float(row[12]), 2)
				symbol = row[0]
				shares = str(ACCOUNT_SIZE // high)
				percent_diff = round(abs(high - low) / ((high + low) / 2) * 100, 2)
				percent_diff_list.append(percent_diff)
				target = str(round(high + high * 0.1, 2))
				stop_loss = str(round(high - high * 0.01, 2))

				# Find condition for correct functionality. (Open >?< Current/Last)
				bg_color = "green" if high > low else "red"

				dollar = "$"
				details.append(symbol)
				details.append(str(percent_diff)+"%")
				details.append(dollar+str(high))
				details.append(shares)
				details.append(dollar+target)
				details.append(dollar+stop_loss)
				details.append(bg_color)
				info[percent_diff] = details
				
			except ValueError:
				pass
	load_gui(percent_diff_list, info)

"""
	load_gui(...) checks the command line arguments for an excel filename
and opens it with csv filereader.

Args:
    percent_diff_list (list of ints): sorted list of percent differences.
    info (dictionary): key is the percent difference, value is the details
    	of the particular stock.
Returns:
	None
"""
def load_gui(percent_diff_list, info):
	global num_refreshes
	row_number = 1

	for p in sorted(percent_diff_list, reverse=True):
		details = info[p]
		symbol = details[0]
		percent_diff = details[1]
		high = details[2]
		shares = details[3]
		target = details[4]
		stop_loss = details[5]
		bg_color = details[6]
		Label(root, text=symbol).grid(row=row_number, column=0)
		Label(root, text=percent_diff).grid(row=row_number, column=1)
		Label(root, text=high).grid(row=row_number, column=2)
		Label(root, text=shares).grid(row=row_number, column=3)
		Label(root, text=target).grid(row=row_number, column=4)
		Label(root, text=stop_loss).grid(row=row_number, column=5)
		row_number += 1

	# TODO: ensure that the file is closed before reopening in case of changes.
	print("Refresh ({})\n".format(num_refreshes))
	num_refreshes += 1
	refresh_button = Button(root, text="Refresh", command=open_file)
	refresh_button.grid(row=row_number, column=5)
	root.mainloop()


if __name__ == '__main__':
	main()
