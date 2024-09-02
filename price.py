#this module has two function. 
import csv

#price_record takes current price and the datetime and stores it to price_record.csv file

def price_record(price, datetime):
    with open('record/price_record.csv', 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([price, datetime])
        file.close()


#last_price retrieves the previous price of MacBook from the csv file.
# Note: the price_record.csv file store prices with most recent price at the bottom. 

def last_price():
        with open('record/price_record.csv', "r", encoding="utf-8", errors="ignore") as file:
                return int(file.readlines()[-1][:4])
