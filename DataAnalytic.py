import matplotlib.pyplot as plt
from  matplotlib import style
import pandas as pd
import numpy as np
import pickle

#style.use('ggplot')
style.use('seaborn-dark')
#print(plt.style.available)



def read_data():
	df =pd.read_csv('County_Level_Wood_Fuel_Demand.csv')
	return df

def load_data():
	dataframe=read_data()


	woodconsumption=dataframe[[u'County', u' Total demand in kilo tonnes oven-dry (Minimum)',
       u'Total demand in kilo tonnes oven-dry (Medium)',
       u'Total demand in kilo tonnes oven-dry (Maximum)',]]

	# save as python object using pickle

	serialized_data_out=open('wood_consumption.pickle','wb')
	pickle.dump(woodconsumption,serialized_data_out)
	serialized_data_out.close()

def open_data():
	serialized_data_in=open('wood_consumption.pickle','rb')
	Data=pickle.load(serialized_data_in)
	return Data


def plot_items():
	data=open_data()
	#plt.legend().remove()
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))
	data.set_index('County').plot(ax=ax1,linewidth=3)

	plt.title("County Wood Fuel Consumption ")
	plt.ylabel('Consumption')
	plt.xlabel('County')

	plt.show()

def plot_correlation_of_data():
	data=open_data()

	# Correlatae data to generate corelated table for colums of how consumptions(min,medium,max) within counties
	corelateddata=data.corr()
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))
	corelateddata.plot(ax=ax1,linewidth=3)

	plt.title("County Wood Fuel Consumption Correlation")
	plt.ylabel('Consumption')
	plt.xlabel('County')

	plt.show()

	print(corelateddata)



def histogram_plot():
	data=open_data()
	data.set_index('County').plot.bar(rot=0,title='Usage Histogram',figsize=(15,10),fontsize=11)

	plt.show()





  

if __name__ =='__main__':

	plot_items()
	plot_correlation_of_data()
	histogram_plot()