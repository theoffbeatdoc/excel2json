
#pip install pandas
#pip install openpyxl
import pandas

excel_data_df = pandas.read_excel('data.xlsx', sheet_name='Sheet1')

#json_str = excel_data_df.to_json()
json_str = excel_data_df.to_json(orient='records')
#print (json_str)

#writing the string onto a file
#open output file
outputfile = open("data.json", "w")
 
#write string to file
outputfile.write(json_str)
 
#close file
outputfile.close()

print("data.json file generated successfully.")



