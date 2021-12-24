#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt


def main():
	'''main function'''

	filename = 'Training Log - Log.csv'

	df = pd.read_csv(filename, header=1, index_col=0, parse_dates=True)
	
	df = df.drop(df.index[0])

	single_variable_time_series(df)


def single_variable_time_series(df):
	''' builds a time series plot for a single variable'''

	variable = 'HRV'

	df[variable].plot(marker='.', linewidth=1, color='r')
	

	plt.title(variable + ' changes over time')
	plt.xlabel('Date')
	plt.ylabel(variable)
	plt.show()



if __name__ == '__main__':
	main()
