#!/usr/bin/python3

import pandas as pd
import data_manipulations
import run_stats


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
	metric1 = 'Pace (min/mile)'
	metric2 = 'Average Cadence (spm)'
	inv_x_axis = 1
	inv_y_axis = 0

	run_stats.two_variable_correlation(df, metric1, metric2, inv_x_axis, inv_y_axis)


if __name__ == '__main__':
	main()
