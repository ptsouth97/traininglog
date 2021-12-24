#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt


def main():

	df = pd.read_csv('Training Log - Log.csv', header=1, index_col=0, parse_dates=True)
	
	df = df.drop(df.index[0])
	#df = df.set_index('Date')
	print(df)

	df["Weight (pounds)"].plot()
	plt.show()

if __name__ == '__main__':
	main()
