#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


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


	df = select_run_type(df)
	single_variable_time_series(df)
	
	#df = filter_dates(df)
	#two_variable_correlation(df)

	#plot_two(df)


def plot_two(df):
	''' plots one chart above another'''

	figure, axis = plt.subplots(2, 1)

	'''
	axis[0, 0].plot(y=df['Training Load'], use_index=True)

	axis[0, 1].plot(y=df['HRV'], use_index=True)'''
	
	bc = axis[0, 0].single_variable_time_series(df)
	#bca=single_variable_time_series(df)

	plt.show()

	return
	

def filter_dates(df):
	''' selects a range of dates based on user input'''

	start_date = '2021-12-1'
	end_date = '2021-12-25'
	
	df = df.loc[start_date:end_date]

	#print(df) 

	return df


def single_variable_time_series(df):
	''' builds a time series plot for a single variable'''

	variable = 'Running speed (mph)'

	abc=df[variable].plot(marker='.', linewidth=1, color='r')
	
	df['SMA_30'] = df[variable].rolling(30).mean()
	df['SMA_30'].plot(legend=True)


	plt.title(variable + ' changes over time')
	plt.xlabel('Date')
	plt.ylabel(variable)

	top_end = df[variable].max()
	low_end = df[variable].min()

	plt.vlines('2021-12-11', low_end, top_end, colors='green', linestyle='dashed', label='Kiawah marathon')
	plt.vlines('2021-7-24', low_end, top_end, colors='brown', linestyle='dashed', label='Red Top Roaster')
	plt.vlines('2021-5-22', low_end, top_end, colors='orange', linestyle='dashed', label='Sweetgrass half marathon')
	plt.vlines('2021-1-17', low_end, top_end, colors='black', linestyle='dashed', label='Charleston virtual marathon')
	plt.legend()
	plt.savefig(variable+'.png')
	plt.show()

	return


def two_variable_correlation(df):
	''' plots one variable versus another to test correlation'''

	variable1 = 'Training Load'
	variable2 = 'HRV'

	df.plot(x=variable1, y=variable2, kind='scatter')

	df = df.dropna(subset=[variable1, variable2])

	column = df[variable1]
	upper_end = column.max()
	lower_end = column.min()
	print(lower_end)
	reg = LinearRegression()
	prediction_space = np.linspace(lower_end, upper_end).reshape(-1,1)
	X = df[variable1].values.reshape(-1,1)
	y = df[variable2].values.reshape(-1,1)
	reg.fit(X,y)
	y_pred = reg.predict(prediction_space)

	r2 = reg.score(X, y)
	
	plt.plot(prediction_space, y_pred, color='red', linewidth=1)
	plt.title(variable2 + ' versus ' + variable1 + ', r^2=' + str(round(r2,2)))
	plt.show()

	return


def select_run_type(df):
	''' select specific types of run only from dataframe'''

	df = df.loc[df['STRAVA Run type'].isin(['Long run', 'Medium long'])]
	
	return(df)


if __name__ == '__main__':
	main()
