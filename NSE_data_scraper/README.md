<div align="right">
<img src="https://user-images.githubusercontent.com/41562231/141720820-090897f9-f564-45e2-9265-15c1269db795.png" height="120" width="900">
</div>

# NSE market data scraper
This project involves web scrapping technique, demonstrated how to collect the information about NSE market with live data. In this, we have provided user choice to get the market data as per indices, sectors, etc without selenium web driver.
Currenly script collect NSE data as __Live Market Data, Pre Market Data__ and __Market Holiday Data__ with file saving option in csv format. 

<div align="center">
  <a href="https://github.com/kunalk3/Data_scraping_and_text_analysis/tree/main/NSE_data_scraper/issues"><img src="https://img.shields.io/github/issues/kunalk3/Data_scraping_and_text_analysis" alt="Issues Badge"></a>
  <a href="https://github.com/kunalk3/Data_scraping_and_text_analysis/tree/main/NSE_data_scraper/graphs/contributors"><img src="https://img.shields.io/github/contributors/kunalk3/Data_scraping_and_text_analysis?color=872EC4" alt="GitHub contributors"></a>
  <a href="https://www.python.org/downloads/release/python-390/"><img src="https://img.shields.io/static/v1?label=python&message=v3.9&color=faff00" alt="Python 3.9"</a>
  <a href="https://github.com/kunalk3/Data_scraping_and_text_analysis/blob/main/LICENSE"><img src="https://img.shields.io/github/license/kunalk3/Data_scraping_and_text_analysis?color=019CE0" alt="License Badge"/></a>
  <a href="https://github.com/kunalk3/Data_scraping_and_text_analysis/tree/main/NSE_data_scraper"><img src="https://img.shields.io/badge/lang-eng-ff1100"></img></a>
  <a href="https://github.com/kunalk3/Data_scraping_and_text_analysis/tree/main/NSE_data_scraper"><img src="https://img.shields.io/github/last-commit/kunalk3/Data_scraping_and_text_analysis?color=309a02" alt="GitHub last commit">
</div>

<div align="center">   
  
  [![Windows](https://img.shields.io/badge/WindowsOS-000000?style=flat-square&logo=windows&logoColor=white)](https://www.microsoft.com/en-in/)
  [![Visual Studio Code](https://img.shields.io/badge/VSCode-0078d7.svg?style=flat-square&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
  [![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?style=flat-square&logo=Jupyter&logoColor=white)](https://jupyter.org/)
  [![Pycharm](https://img.shields.io/badge/Pycharm-41c907.svg?style=flat-square&logo=Pycharm&logoColor=white)](https://www.jetbrains.com/pycharm/)
  [![Colab](https://img.shields.io/badge/Colab-F9AB00.svg?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/?utm_source=scs-index/)
  [![Spyder](https://img.shields.io/badge/Spyder-838485.svg?style=flat-square&logo=spyder%20ide&logoColor=white)](https://www.spyder-ide.org/)
</div>
  
---
## :books: Introduction NSE Market segments
- Pre-market -->
  
      ['NIFTY 50': 'NIFTY', 'NIFTY BANK': 'BANKNIFTY', 'EMERGE': 'SME', 'SECURITIES IN F&O': 'FO', 'OTHERS': 'OTHERS', 'ALL': 'ALL']
  
- Live Market -->
  
      'Broad Market Indices': ['NIFTY 50', 'NIFTY NEXT 50', 'NIFTY MIDCAP 50', 'NIFTY MIDCAP 100', 'NIFTY MIDCAP 150', 'NIFTY SMALLCAP 50', 'NIFTY SMALLCAP 100', 'NIFTY SMALLCAP 250', 
                              'NIFTY MIDSMALLCAP 400', 'NIFTY 100', 'NIFTY 200', 'NIFTY500 MULTICAP 50:25:25', 'NIFTY LARGEMIDCAP 250'],
      'Sectorial Indices': ['NIFTY AUTO','NIFTY BANK', 'NIFTY ENERGY', 'NIFTY FINANCIAL SERVICES', 'NIFTY FINANCIAL SERVICES 25/50', 'NIFTY FMCG', 'NIFTY IT', 'NIFTY MEDIA', 'NIFTY METAL', 
                           'NIFTY PHARMA', 'NIFTY PSU BANK', 'NIFTY REALTY', 'NIFTY PRIVATE BANK'], 
      'Others': ['Securities in F&O', 'Permitted to Trade'], 
      'Strategy Indices': ['NIFTY DIVIDEND OPPORTUNITIES 50', 'NIFTY50 VALUE 20', 'NIFTY100 QUALITY 30', 'NIFTY50 EQUAL WEIGHT', 'NIFTY100 EQUAL WEIGHT', 'NIFTY100 LOW VOLATILITY 30', 
                          'NIFTY ALPHA 50', 'NIFTY200 QUALITY 30', 'NIFTY ALPHA LOW-VOLATILITY 30', 'NIFTY200 MOMENTUM 30'],
      'Thematic Indices': ['NIFTY COMMODITIES', 'NIFTY INDIA CONSUMPTION', 'NIFTY CPSE', 'NIFTY INFRASTRUCTURE', 'NIFTY MNC', 'NIFTY GROWTH SECTORS 15', 'NIFTY PSE', 'NIFTY SERVICES SECTOR', 
                          'NIFTY100 LIQUID 15', 'NIFTY MIDCAP LIQUID 15']}

- Market Holidays -->
  
      ['Trading', 'Clearing']
---
  
## :bulb: Demo
- Below is the demonstrated sample at my local environments/ system with platform as __Visual Studio Code__ (V1.61.2) on OS __Windows 10__. 
  
https://user-images.githubusercontent.com/41562231/138689514-a9a04a74-edc3-4c3d-b9a3-5c98bcc94496.mp4
 
#### :pencil2: _Input_ - 
- Run python code __main.py__ and enter user choice as per choice menu as,
 
      ### --- Select market data choice --- ###
        (1) NSE Pre-market Data
        (2) NSE Live-market Data
        (3) NSE Holidays
        (4) Exit
        Your choice - 2

 - It shows Live market indices, enter the market indice as per user as,
  
    _['Broad Market Indices', 'Sectorial Indices', 'Others', 'Strategy Indices', 'Thematic Indices']_

        Enter market index view : Sectorial Indices

- It shows specific market domain where all the market data is available as per domain. Enter the domain choice as,
 
    _['NIFTY AUTO', 'NIFTY BANK', 'NIFTY ENERGY', 'NIFTY FINANCIAL SERVICES', 'NIFTY FINANCIAL SERVICES 25/50', 'NIFTY FMCG', 'NIFTY IT', 'NIFTY MEDIA', 'NIFTY METAL', 'NIFTY PHARMA', 'NIFTY PSU BANK', 'NIFTY REALTY', 'NIFTY PRIVATE BANK']_

      Enter market index : NIFTY IT
  
#### :bookmark: _Output_ - 
  
  Output csv files are created with current date folder __NSE_DATA_YYYY_MM_DD__ if the user choice from menu tick as __Y__ / __y__.
  
- `NSE Live-market data`

![image](https://user-images.githubusercontent.com/41562231/138696139-d6947a75-1aca-4eaa-9c18-1b2ad92f6681.png)

- `NSE Pre-market data`
  
![image](https://user-images.githubusercontent.com/41562231/138695964-19781f5f-3b7d-463e-9c93-c369350fabf0.png)

- `NSE market holiday data`
  
![image](https://user-images.githubusercontent.com/41562231/138695237-2da546ca-ce76-48e4-a736-7f3bb0494d44.png)

---
  
## :wrench: Installation
- Create __virtual environment__ `python -m venv VIRTUAL_ENV_NAME` and activate it `.\VIRTUAL_ENV_NAME\Scripts\activate`.
- Install necessary library for this project from the file `requirements.txt` or manually install by `pip`.
  ```
  pip install -r requirements.txt
  ```
  To create project library requirements, use below command,
  ```
  pip freeze > requirements.txt
  ```
- In code, write your browser user-agent in headers before proceeding the script.
  ```python
  import requests
  
  def __init__(self):
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
        self.session = requests.Session()
        self.session.get('http://nseindia.com', headers=self.headers)
  ```
  __How to capture the user-agent and API from NSE?__ _Refers below steps/ tutorial._
  
    1. Open NSE website https://www.nseindia.com/ and __inspect__ (Right click __->__ Inspect).
    2. Go to __Network__ and select www.nseindia.com under __Name__.
    3. Go to __Headers__ and copy the __user-agent__ value from bottom.

https://user-images.githubusercontent.com/41562231/138703511-2f6a2c8c-af46-493b-9878-02c3a1f47ee1.mp4

- Now run python file.
  ``` 
  python main.py
  ```
---  

## :bookmark: Directory Structure 
```bash
    .                                   # Root dir
    ├── main.py                         # Python code
    ├── NSE_Data_YYYY_MM_DD             # Output folder with current date (will create once execution of script)
    │   ├── LiveMarketData.csv          # Output live market data csv file
    │   ├── PreMarketData.csv           # Output pre market data csv file
    │   └── MarketHolidayData.csv       # Output market holiday data csv file
    ├── requirements.txt                # Project requirements library with versions
	└── README.md			# Project README file
	
```

---  
  
## :iphone: Connect with me
`You say freak, I say unique. Don't wait for an opportunity, create it.`
  
__Let’s connect, share the ideas and feel free to ping me...__
  
<div align="center"> 
  <p align="left">
    <a href="https://linkedin.com/in/kunalkolhe3" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg" alt="kunalkolhe3" height="30" width="40"/></a>
    <a href="https://github.com/kunalk3/" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="kunalkolhe3" height="30" width="40"/></a>
    <a href="mailto:kunalkolhe333@gmail.com" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/gmail.svg" alt="kunalkolhe333" height="30" width="40"/></a>
    <a href="https://www.hackerrank.com/kunalkolhe333" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/hackerrank.svg" alt="kunalkolhe333" height="30" width="40"/></a>
    <a href="https://fb.com/kunal.kolhe.98" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/facebook.svg" alt="kunal.kolhe.98" height="30" width="40"/></a>
    <a href="https://instagram.com/kkunalkkolhe" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/instagram.svg" alt="kkunalkkolhe" height="30" width="40"/></a>
  </p>
</div> 


<div align="left">
<img src="https://user-images.githubusercontent.com/41562231/141720940-53eb9b25-777d-4057-9c2d-8e22d2677c7c.png" height="120" width="900">
</div>
