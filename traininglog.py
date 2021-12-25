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

	###RENAME certain columns here####

	#print(df.columns)
	#single_variable_time_series(df)
	#select_run_type(df)
	two_variable_correlation(df)


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


def two_variable_correlation(df):
	''' plots one variable versus another to test correlation'''

	variable1 = 'Running speed (mph)'
	variable2 = 'Average Cadence (spm)'

	df.plot(x=variable1, y=variable2, kind='scatter')
	plt.show()


def select_run_type(df):
	''' select specific types of run only from dataframe'''

	df = df.loc[df['STRAVA Run type'] == 'Long run']
	print(df)


if __name__ == '__main__':
	main()
