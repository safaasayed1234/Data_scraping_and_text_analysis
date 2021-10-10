from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.youtube.com/c/AlexTheAnalyst/videos'

video_urls = []
video_titles = []
video_views = []
video_upload_times = []
video_counts_temp = []


def get_video_urls(url):
    print('Process has been started...\n')
    path = 'data/chromedriver.exe' # selenium web driver path
    driver = webdriver.Chrome(executable_path=path)
    driver.get(url)

    # scrolling to the bottom of the page
    for item in range(50):
        page = driver.find_element_by_tag_name('html')
        page.send_keys(Keys.END)
        
    # extracting data from page
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'html.parser')
    
    # extracting views and time
    print('Extracting video views and time...\n')
    for views in soup.findAll('span', class_='style-scope ytd-grid-video-renderer'):
        video_counts_temp.append(views.get_text())

    # extracting and printing youtube video url from channel
    print('Extracting video titles and urls...\n')
    for url in soup.findAll('a', id='video-title'):
        video_urls.append('https://www.youtube.com' + url.get('href')) 
        video_titles.append(url.get('title'))

    video_views = video_counts_temp[0::2]
    video_upload_times = video_counts_temp[1::2]    

    print('Printing results...\n')
    print(f'This youtube channel has {len(video_urls)} videos published')
    
    data = pd.DataFrame(list(zip(video_titles, video_views, video_upload_times, video_urls)), columns =['Titles', 'Views', 'Upload Time', 'Links']) 
    print(data)

    print('Process has been completed...\n')
    driver.quit()


if __name__ == '__main__':
    get_video_urls(url)
