#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import data_manipulations


def main():
	'''main function'''

	#filename = 'Training Log - Log.csv'
	sheet_id = '1epQ4axsxFBJ4sTvhTiahAuDX1MqcWfj9iY7igJK5oHA'
	sheet_name = 'Log'
	url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

	df = pd.read_csv(url, index_col=0, parse_dates=True, header=0)
	
	df = df.drop(df.index[0])

	df = data_manipulations.convert_pace(df)
	#df = select_run_type(df)
	#df = single_variable_time_series(df)
	
	#df = filter_dates(df)
	two_variable_correlation(df)

	#plot_two(df)


def filter_dates(df):
	''' selects a range of dates based on user input'''

	start_date = '2021-12-1'
	end_date = '2021-12-25'
	
	df = df.loc[start_date:end_date]

	
	return df


def two_variable_correlation(df):
	''' plots one variable versus another to test correlation'''

	variable1 = 'Average Cadence (spm)'
	variable2 = 'Pace (min/mile)'

	df.plot(x=variable1, y=variable2, kind='scatter')

	df = df.dropna(subset=[variable1, variable2])

	column = df[variable1]
	upper_end = column.max()
	lower_end = column.min()
	
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

	'''
def convert_pace(df):
	 converts 0:8:00 min/mile to 8.0 min/mile

	df['datetime'] = pd.to_datetime(df['Average Pace (min/mile)'])
	df['minutes'] = df['datetime'].dt.minute
	df['seconds'] = (df['datetime'].dt.second)/60
	df['Pace (min/mile)'] = round(df['minutes'] + df['seconds'], 2)

	return(df)
	'''

if __name__ == '__main__':
	main()
