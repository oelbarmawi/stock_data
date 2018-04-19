win_rate = .75 	# Strategy win rate 75% 
BROKER_FEE = 15 # Brokerage fee for buy and sell
WINNING_DAYS_IN_A_MONTH = (win_rate * 20) - ((1 - win_rate) * 20 * 0.5)


def compound_earnings(capital, num_months, percent_increase):
	if num_months == 0:
		print("Capital: ${}".format(round(capital,2)))
	else:
		total_fees = BROKER_FEE * WINNING_DAYS_IN_A_MONTH
		spending_power = 100000 if capital > 100000 else capital
		capital += (spending_power * percent_increase * WINNING_DAYS_IN_A_MONTH) - total_fees
		compound_earnings(capital, num_months-1, percent_increase)


account_size = 5000
daily_earnings_percentage = 0.01 # 1%
num_months = 1
compound_earnings(account_size, num_months, daily_earnings_percentage)