import requests
from bs4 import BeautifulSoup
import pandas as pd

#Download page
def get_page(url):
    res = requests.get(url)
    page = res.status_code
    if page != 200:
        raise Exception('Failed to load page')
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

#Parsing page
def find_title(soup):
    tag_title = soup.find_all('h3')
    titles = []
    for t in tag_title:
        titles.append(t.text)
    return titles

#Convert Data to csv
def data_to_csv(titles):
    topic_df = pd.DataFrame(titles)
    title = 'top_job_ph.csv'
    return topic_df.to_csv(title, index=False)

def main():
    url = 'https://bukas.ph/blog/best-paying-jobs-for-filipino-fresh-graduates/'
    page = get_page(url)
    title = find_title(page)
    data_to_csv(title)

if __name__ == '__main__':
    main()