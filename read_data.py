import sys
import csv
from tkinter import *

root = Tk()

symbol_label = Label(root, text="Symbol")
symbol_label.grid(row=0, column=0)

pd_label = Label(root, text="Percent Difference")
pd_label.grid(row=0, column=1)

entry_label = Label(root, text="Entry Price")
entry_label.grid(row=0, column=2)

target_label = Label(root, text="Target Price")
target_label.grid(row=0, column=3)

stop_loss_label = Label(root, text="Stop Loss Price")
stop_loss_label.grid(row=0, column=4)

#sticky for alignment in grid




def main():
	global root
	account_size = 5000
	percent_diff_list = []
	info = {}

	filename = sys.argv[1] if len(sys.argv) > 1 else print("Please enter filename.")
	if not filename:
		sys.exit()

	print("-"*50)
	with open(filename, encoding='utf-8') as file:
		reader = csv.reader(file)
		row_number = 1
		for row in reader:
			if len(row) >= 15:
				try:
					dollar = "$"
					high = round(float(row[11]), 2)
					low = round(float(row[12]), 2)
					symbol = row[0]
					shares = str(account_size // high)
					percent_diff = round(abs(high - low) / ((high + low) / 2) * 100, 2)
					percent_diff_list.append(percent_diff)
					target = str(round(high + high * 0.1, 2))
					stop_loss = str(round(high - high * 0.01, 2))
					# message = "[{}]\tPercent Difference: {}% --> Entry ${}".format(symbol, percent_diff, high)
					# message += "\t[Target = ${} :: Stop Loss = ${}]".format(target, stop_loss)
					# message += "\n\tVolume: " + row[9]
					# message += "\n\tNumber of shares: " + shares
					if (high > low):
						bg_color = "green"
					else:
						bg_color ="red"
					Label(root, text=symbol, bg=bg_color).grid(row=row_number, column=0)
					Label(root, text=str(percent_diff)+"%", bg=bg_color).grid(row=row_number, column=1)
					Label(root, text=dollar+str(high), bg=bg_color).grid(row=row_number, column=2)
					Label(root, text=dollar+target, bg=bg_color).grid(row=row_number, column=3)
					Label(root, text=dollar+stop_loss, bg=bg_color).grid(row=row_number, column=4)
					# info[percent_diff] = message
					row_number += 1
				except ValueError:
					pass


	for p in sorted(percent_diff_list, reverse=True):
		details = info[p]
		symbol = details[0]
		percent_diff = details[1]
		high = details[2]
		target = details[3]
		stop_loss = details[4]
		Label(root, text=symbol, bg=bg_color).grid(row=row_number, column=0)
		Label(root, text=str(percent_diff)+"%", bg=bg_color).grid(row=row_number, column=1)
		Label(root, text=dollar+str(high), bg=bg_color).grid(row=row_number, column=2)
		Label(root, text=dollar+target, bg=bg_color).grid(row=row_number, column=3)
		Label(root, text=dollar+stop_loss, bg=bg_color).grid(row=row_number, column=4)
		
	root.mainloop()

if __name__ == '__main__':
	main()

