import requests
import pandas as pd
import os, datetime

class NSEIndia:                    
    def __init__(self):
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
        self.session = requests.Session()
        self.session.get('http://nseindia.com', headers=self.headers) 

    def NsePreMarketData(self):
        pre_market_keys = {'NIFTY 50': 'NIFTY', 'NIFTY BANK': 'BANKNIFTY', 'EMERGE': 'SME', 'SECURITIES IN F&O': 'FO', 
                            'OTHERS': 'OTHERS', 'ALL': 'ALL'}
        pre_market_keys_temp_keys = list(pre_market_keys.keys())
        print(list(pre_market_keys.keys()))

        try:
            user_input_key = str(input('Enter market index : ').upper())
            if user_input_key not in pre_market_keys_temp_keys:
                print('Error :: Invalid user input...')
            else:
                pass
        except:
            pass

        try:
            
            data = self.session.get(f"https://www.nseindia.com/api/market-data-pre-open?key={pre_market_keys[user_input_key]}", 
                    headers=self.headers).json()['data']
            new_data = []
            for i in data:
                new_data.append(i['metadata'])
            df = pd.DataFrame(new_data)
            return df, True
        except ValueError:
            print('Error :: Invalid user input / API failure...')

    def NseLiveMarketData(self):
        live_market_index = {
            'Broad Market Indices': ['NIFTY 50', 'NIFTY NEXT 50', 'NIFTY MIDCAP 50', 'NIFTY MIDCAP 100', 'NIFTY MIDCAP 150', 
                            'NIFTY SMALLCAP 50', 'NIFTY SMALLCAP 100', 'NIFTY SMALLCAP 250', 'NIFTY MIDSMALLCAP 400', 
                            'NIFTY 100', 'NIFTY 200', 'NIFTY500 MULTICAP 50:25:25', 'NIFTY LARGEMIDCAP 250'],
            'Sectorial Indices': ['NIFTY AUTO','NIFTY BANK', 'NIFTY ENERGY', 'NIFTY FINANCIAL SERVICES', 'NIFTY FINANCIAL SERVICES 25/50', 
                            'NIFTY FMCG', 'NIFTY IT', 'NIFTY MEDIA', 'NIFTY METAL', 'NIFTY PHARMA', 'NIFTY PSU BANK', 'NIFTY REALTY', 
                            'NIFTY PRIVATE BANK'], 
            'Others': ['Securities in F&O', 'Permitted to Trade'], 
            'Strategy Indices': ['NIFTY DIVIDEND OPPORTUNITIES 50', 'NIFTY50 VALUE 20', 'NIFTY100 QUALITY 30', 'NIFTY50 EQUAL WEIGHT', 
                            'NIFTY100 EQUAL WEIGHT', 'NIFTY100 LOW VOLATILITY 30', 'NIFTY ALPHA 50', 'NIFTY200 QUALITY 30', 
                            'NIFTY ALPHA LOW-VOLATILITY 30', 'NIFTY200 MOMENTUM 30'],
            'Thematic Indices': ['NIFTY COMMODITIES', 'NIFTY INDIA CONSUMPTION', 'NIFTY CPSE', 'NIFTY INFRASTRUCTURE', 'NIFTY MNC', 
                            'NIFTY GROWTH SECTORS 15', 'NIFTY PSE', 'NIFTY SERVICES SECTOR', 'NIFTY100 LIQUID 15', 'NIFTY MIDCAP LIQUID 15']}
        live_market_index_temp_keys = list(live_market_index.keys())
        print(live_market_index_temp_keys)

        try:
            user_input_view = str(input('Enter market index view : ').title())
            if user_input_view not in live_market_index_temp_keys:
                print('Error :: Invalid user input...')
            else:
                pass

            for dict_keys, dict_vals in live_market_index.items():
                 if user_input_view == dict_keys:
                    print(dict_vals)
            user_input_index = str(input('Enter market index : ').upper())
        except ValueError:
            print('Error :: Invalid user input...')

        try:
            data = self.session.get(f"https://www.nseindia.com/api/equity-stockIndices?index="
                    f"{live_market_index[user_input_view][live_market_index[user_input_view].index(user_input_index)].upper().replace(' ','%20').replace('&','%26')}",
                    headers=self.headers).json()['data'] 
                   
            df = pd.DataFrame(data)
            df = df.drop(['meta'], axis=1)
            return df, True
        except:
            print('Error :: API failure...')

    def NseHoliday(self):
        holiday = ['clearing', 'trading']
        print(holiday)

        user_input_holiday = str(input('Enter market holiday base : ').lower())
        if user_input_holiday not in holiday:
            print('Error :: Invalid user input...')
        else:
            pass

        try:
            data = self.session.get(f'https://www.nseindia.com/api/holiday-master?type={user_input_holiday}', headers = self.headers).json()
            df = pd.DataFrame(list(data.values())[0])
            return df, True
        except:
            print('Error :: API failure...')

now_dt = datetime.datetime.now()
now_dt = now_dt.strftime('%Y_%m_%d')
folder_name = 'NSE_Data_' + now_dt

cwd = os.getcwd()
directory_path = os.path.join(cwd, folder_name)
if not os.path.exists(directory_path):
    os.mkdir(directory_path)
else:
    pass

n = NSEIndia()
is_on = True

while is_on:
    try:
        print('--------------------------------------------')
        choice = int(input(" ### --- Select market data choice --- ### \n   (1) NSE Pre-market Data\n   (2) NSE Live-market Data\n   (3) NSE Holidays\n   (4) Exit\n   Your choice - "))
        print('--------------------------------------------')
        if choice == 4:
            is_on = False

        elif choice == 1:
            pre_market_data, status_ini1 = n.NsePreMarketData()
            print(pre_market_data)
            
            if status_ini1 == True:
                user_inout_export_data = input('You want to export data as CSV? Press "Y" for Yes, else "N" for No...').upper()
                if user_inout_export_data == 'Y':
                    pre_market_data.to_csv(directory_path + '\\' + 'PreMarketData.csv', header = True, index = False)
                    print('Info :: Data has been exported successfully to csv file "PreMarketData.csv"...')
                elif user_inout_export_data == 'N':
                    pass
                else:
                    print('Error :: Invalid user input...')
            status_ini1 = False

        elif choice == 2:
            live_market_data, status_ini2 = n.NseLiveMarketData()
            print(live_market_data)

            if status_ini2 == True:
                user_inout_export_data = input('You want to export data as CSV? Press "Y" for Yes, else "N" for No...').upper()
                if user_inout_export_data == 'Y':
                    live_market_data.to_csv(directory_path + '\\' + 'LiveMarketData.csv', header = True, index = False)
                    print('Info :: Data has been exported successfully to csv file "LiveMarketData.csv"...')
                elif user_inout_export_data == 'N':
                    pass
                else:
                    print('Error :: Invalid user input...')
            status_ini1 = False

        elif choice == 3:
            market_holiday_data, status_ini3 = n.NseHoliday()
            print(market_holiday_data)

            if status_ini3 == True:
                user_inout_export_data = input('You want to export data as CSV? Press "Y" for Yes, else "N" for No...').upper()
                if user_inout_export_data == 'Y':
                    market_holiday_data.to_csv(directory_path + '\\' + 'MarketHolidayData.csv', header = True, index = False)
                    print('Info :: Data has been exported successfully to csv file "MarketHolidayData.csv"...')
                elif user_inout_export_data == 'N':
                    pass
                else:
                    print('Error :: Invalid user input...')
            status_ini1 = False

        else:
            print('Error :: Invalid user input...')
    except:
        print('Error :: Invalid user input, please choice the above options...')
