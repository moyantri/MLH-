from requests import get
from bs4 import BeautifulSoup
from time import sleep
from random import randint

names = []
years = []
imdb_ratings = []
metascores = []
votes = []

requests=0

pages = [str(i) for i in range(1,5)]
years_url = [str(i) for i in range(2018,2020)]

# Extract data from individual movie container
for year_url in years_url:
  for page in pages:
    url = 'http://www.imdb.com/search/title?release_date='+str(year_url)+'&sort=num_votes,desc&page='+str(page)
    response = get(url)
    sleep(randint(8,15))
    #print(response.text)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
    for container in movie_containers:

      if container.find('div', class_ = 'ratings-metascore') is not None:
        name = container.h3.a.text
        names.append(name)
    
        year = container.h3.find('span', class_ = 'lister-item-year').text
        years.append(year)
    
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)
 
        m_score = container.find('span', class_ = 'metascore').text
        metascores.append(int(m_score))
    
        vote = container.find('span', attrs = {'name':'nv'})['data-value']
        votes.append(int(vote))

import pandas as pd
movie_ratings = pd.DataFrame({'movie': names,
'year': years,
'imdb': imdb_ratings,
'metascore': metascores,
'votes': votes
})

movie_ratings = movie_ratings[['movie', 'year', 'imdb', 'metascore', 'votes']]
movie_ratings.loc[:, 'year'] = movie_ratings['year'].str[-5:-1].astype(int)
movie_ratings.to_csv('movie_ratings.csv')
