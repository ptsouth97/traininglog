#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt


def main():

	filename = 'Training Log - Log.csv'

	df = pd.read_csv(filename, header=1, index_col=0, parse_dates=True)
	
	df = df.drop(df.index[0])

	weight(df)


def weight(df):

	df["Weight (pounds)"].plot()


	plt.title('Weight Maintenance')
	plt.xlabel('Date')
	plt.ylabel('Weight (pounds)')
	plt.show()


if __name__ == '__main__':
	main()
