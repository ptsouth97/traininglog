#!/usr/bin/python3

import pandas as pd
import data_manipulations
import run_stats
import load
import matplotlib.pyplot as plt

def main():
	'''main function'''

	df = load.data()
	
	#df = data_manipulations.convert_pace(df)
	#df = select_run_type(df)
	
	'''
	# Filters data frame for given dates in one year
	start_date = '2021-01-01'
	end_date = '2021-12-31'
	df1 = data_manipulations.filter_dates(df, start_date, end_date)
	#df1.plot(y='RHR')

	# Filters data frame for given dates in another year
	start_date2 = '2022-01-01'
	end_date2 = '2022-12-31'
	df2 = data_manipulations.filter_dates(df, start_date2, end_date2)
	#df2.plot(y='RHR')
	'''
	pv = pd.pivot_table(df, index=df.index.month, columns=df.index.year, values='RHR')

	pv.plot()
	plt.show()
	

	#df = run_stats.single_variable_time_series(df, 'RHR', 0, 0)

	#metric1 = 'Pace (min/mile)'
	#metric2 = 'Average Cadence (spm)'
	#inv_x_axis = 1
	#inv_y_axis = 0

	#run_stats.two_variable_correlation(df, metric1, metric2, inv_x_axis, inv_y_axis)
	

if __name__ == '__main__':
	main()
