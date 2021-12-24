#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt


def main():
	'''main function'''

	#filename = 'Training Log - Log.csv'
	sheet_id = '1epQ4axsxFBJ4sTvhTiahAuDX1MqcWfj9iY7igJK5oHA'
	sheet_name = 'Log'
	url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

	df = pd.read_csv(url, index_col=0, parse_dates=True, header=0)
	
	df = df.drop(df.index[0])
	#print(df.columns)
	single_variable_time_series(df)


def single_variable_time_series(df):
	''' builds a time series plot for a single variable'''

	variable = 'Weight Gurus Weight (pounds)'

	df[variable].plot(marker='.', linewidth=1, color='r')
	
	df['SMA_30'] = df[variable].rolling(30).mean()
	df['SMA_30'].plot(legend=True)


	plt.title(variable + ' changes over time')
	plt.xlabel('Date')
	plt.ylabel(variable)
	plt.show()



if __name__ == '__main__':
	main()
