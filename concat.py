import os
import glob
import pandas as pd

curr = ['btc','inr','usdt','wrx']
filenames = []
Dict = {}
for currency in curr:
	filenames.append(currency+'data')
	
#print(filenames)

##starting the concatenation of the file
for i in range(0,4):
	if i == 0:
		os.chdir("./data/"+curr[i])
	else:
		os.chdir(curr[i])
	extension = 'csv'
	all_filenames = [j for j in glob.glob('*.{}'.format(extension))]
	combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
	#print(combined_csv)
	#print(os.path.dirname(os.getcwd()))
	os.chdir(os.path.dirname(os.getcwd()))
	#print(os.getcwd())	
	combined_csv.to_csv("./"+filenames[i]+"/summary.csv",index = False, encoding='utf-8-sig')
