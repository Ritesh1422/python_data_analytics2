import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from database import Article

base=declerative_base()

def oprndb():
    engine=create_engine('sqllite:///articles.db',echo=True)
    return sessionmaker(blind=engine)()

def get_page(url=''):
    try:
        url = 'https://blog.jetbrains.com/kotlin/'
        page = requests.get(url)
        if page.status_code == 200:
            print(f'👍 {page.status_code} Success!')
            soup = BeautifulSoup(page.content, 'html.parser')
        elif page.status_code == 404:
            print(f'👎 {page.status_code} Page Not Found.')
        elif page.status_code == 403:
            print(f'👎 {page.status_code} Forbidden.')
        elif page.status_code == 500:
            print(f'👎 {page.status_code} Internal Server Error.')
        else:
            print(f'👎 {page.status_code} Unknown Error.')
    except Exception as e:
        print(f'⚠️ Error: \n{e}')



def get_articles(soup):
    target = soup.find('div', class_ = 'row latest latest_posts_section')
    if target:
        print("Target section found!")
        articles = target.find_all('div', class_='col')
        if articles:
            print("Articles found!")
            print(f'Total articles: {len(articles)}')
            for item in articles:
                heading  = item.find('h3')
                publish = item.find('time')
                summary = item.find('p')
                author = item.find('span')
                try:
                    Article=Article(
                        title=heading.text,
                        author =author.text,
                        pub_date=publish['datetime'],
                        summary=summary.text
                    )
                    db=open()
                    db.add(Article)
                    db.commit()
                    db.close()
                except Exception as e:
                    print(f'error:\n(e)')
            else:
                print('doing wrong')
        else:
            print('wrng')

#executing the function
soup=get_page()
if soup:
    get_articles(soup)
else:
    print('something wrong')    