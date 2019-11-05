import bs4 as bs
import re
from bs4 import BeautifulSoup as soup
import selenium
from selenium import webdriver
import time
import pymysql
import insert

def getStats():

    db = pymysql.connect("localhost", "root", "", "firstbase")

    print("getting player fielding stats ...")

    #fileName = 'playerHitting.csv'
    #f = open(fileName, 'w')
    #headers = 'Rank, Player, Team, Position, Games, At Bats, Runs, Hits, Doubles, Triples, Home Runs, Runs Batted, Walks, Strikeout, Bases Stolen, Caught Stealing, Avg. Hits (hits/at bats), On-base %, Slugging %, O+S\n'
    #f.write(headers)

    my_url = "http://mlb.mlb.com/stats/sortable_es.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+fielding&game_type='R'&season=2018&season_type=ANY&league_code='MLB'&sectionType=sp&statType=fielding&page=1&ts=1572842052396&playerType=QUALIFIER&sportCode='mlb'&split=&team_id=&active_sw=&position=&page_type=SortablePlayer&sortOrder='desc'&sortColumn=fpct&results=&perPage=50&timeframe=&last_x_days=&extended=0"

    browser = webdriver.Firefox()
    browser.get(my_url)

    html = browser.page_source
    webpageSoup = bs.BeautifulSoup(html, 'html.parser')
    time.sleep(3)
    currentPage = 1
    totalPages = webpageSoup.find_all('button',
                                      {'class': 'paginationWidget-last'})
    print(totalPages[0].text)

    while (currentPage <= int(totalPages[0].text)):

        html = browser.page_source
        webpageSoup = bs.BeautifulSoup(html, 'html.parser')
        table = webpageSoup.find_all('tr', {'tabindex': '0'})
        #print(tableRows)
        #print(len(tableRows)) #50/50

        for row in table:
            rank = row.find_all('td', {'class': 'dg-rank'})
            jugador = row.find_all('td',
                                   {'class': 'dg-name_display_last_init'})
            equipo = row.find_all('td', {'class': 'dg-team_abbrev'})
            pos = row.find_all('td', {'class': 'dg-position'})
            juegos = row.find_all('td', {'class': 'dg-g'})
            era = row.find_all('td', {'class': 'dg-gs'})
            g = row.find_all('td', {'class': 'dg-inn'})
            chances = row.find_all('td', {'class': 'dg-tc'})
            putout = row.find_all('td', {'class': 'dg-po'})
            assists = row.find_all('td', {'class': 'dg-a'})
            errors = row.find_all('td', {'class': 'dg-e'})
            dgh = row.find_all('td', {'class': 'dg-dp'})
            dgr = row.find_all('td', {'class': 'dg-sb'})
            dger = row.find_all('td', {'class': 'dg-cs'})
            dghr = row.find_all('td', {'class': 'dg-sbpct'})
            bb = row.find_all('td', {'class': 'dg-pb'})
            so = row.find_all('td', {'class': 'dg-c_wp'})
            fpct = row.find_all('td', {'class': 'dg-fpct'})
            whip = row.find_all('td', {'class': 'dg-rf'})

            #f.write(rank[0].text + ',' + '"' + jugador[0].a.text + '"' + ',' + equipo[0].text + ',' + pos[0].text + ',' + juegos[0].text + ',' + era[0].text + ',' + g[0].text + ',' + chances[0].text + ',' + putout[0].text + ',' + assists[0].text + ',' + errors[0].text + ',' + dgh[0].text + ',' + dgr[0].text + ',' + dger[0].text + ',' + dghr[0].text + ',' + bb[0].text + ',' + so[0].text + ',' + fpct[0].text + ',' + whip[0].text + '\n')

            insert.playerFielding(
                db,
                jugador[0].a.text,
                equipo[0].text,
                rank[0].text,
                chances[0].text,
                putout[0].text,
                assists[0].text,
                errors[0].text,
                fpct[0].text,
                pos[0].text,
            )

        currentPage += 1

        if (currentPage <= int(totalPages[0].text)):
            print('loading next page ...')
            nextPage = browser.find_elements_by_xpath(
                '/html/body/div[2]/div/div[3]/div/div[1]/div[11]/fieldset/button[4]'
            )
            nextPage[0].click()
            time.sleep(5)

    #f.close()
    browser.close()
    db.close()