import bs4 as bs
import re
import selenium
from selenium import webdriver
 
url = "http://mlb.mlb.com/stats/sortable_es.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+hitting&game_type='R'&season=2018&season_type=ANY&league_code='MLB'&sectionType=sp&statType=hitting&page=1&ts=1569359008122&playerType=QUALIFIER&sportCode='mlb'&split=&team_id=&active_sw=&position=&page_type=SortablePlayer&sortOrder='desc'&sortColumn=avg&results=&perPage=50&timeframe=&last_x_days=&extended=0"

driver = webdriver.Firefox()
driver.get(url)
html = driver.page_source
soup = bs.BeautifulSoup(html)

table = soup.find_all('div', attrs={'id':'datagrid'})
print(table)
