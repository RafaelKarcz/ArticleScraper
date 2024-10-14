import requests
import string
import os
from bs4 import BeautifulSoup

def articles_finder(soup):
    return soup.find_all('article', class_='u-full-height c-card c-card--flush')

def directory_maker(x):
    directory_name = 'Page_' + str(x)
    path_ = os.path.exists(directory_name)
    if path_:
        return directory_name
    else:
        os.mkdir(directory_name)
        return directory_name

def article_type_finder(article):
    return article.find('span', {'data-test': 'article.type'})

def article_title_finder(article):
    return article.find('h3', class_='c-card__title')

def file_name_formatter(article_title):
    cleaned_file_name = ''.join(char for char in article_title if char not in string.punctuation)
    file_name_undersore = cleaned_file_name.replace(' ', '_') + '.txt'
    return file_name_undersore

def article_link_retriever(article):
    base_url = 'https://www.nature.com'
    a_tag = article.find('a', {'data-track-action': 'view article'})
    if a_tag:
        return base_url + a_tag.get('href')
    
def article_text_retriever(article_link):
    article_request = requests.get(article_link)
    article_soup = BeautifulSoup(article_request.content, 'lxml')

    container = article_soup.find('p', class_='article__teaser')    
    if container:
        return container.text.strip()
    else:
        return "No text found"

def file_creator(file_name, saving_directory, article_text):
    current_wd = os.getcwd()
    with open(os.path.join(current_wd, saving_directory, file_name), 'w', encoding='utf-8') as article_file:
        article_file.write(article_text)

def main():    
    base_scraping_url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page='
    
    webpage_number = int(input())
    article_type = input()
    
    for i in range(1, webpage_number + 1):
        
        scraping_url = base_scraping_url + str(i)
        request = requests.get(scraping_url)
        soup = BeautifulSoup(request.content, 'lxml')
        
        articles = articles_finder(soup)
        saving_directory = directory_maker(i)
        
        for article in articles:
            article_type_found = article_type_finder(article)
            if article_type_found and article_type_found.text.strip() == article_type:
                article_title = article_title_finder(article)
                if article_title:
                    article_title_text = article_title.text.strip()
                    file_name = file_name_formatter(article_title_text)
                    article_link = article_link_retriever(article)
                    article_text = article_text_retriever(article_link)
                    file_creator(file_name, saving_directory, article_text)
    print('Saved all articles.')
                
if __name__ == '__main__':
    main()