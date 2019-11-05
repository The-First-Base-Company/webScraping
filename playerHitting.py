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

    print("getting player hitting stats ...")

    #fileName = 'playerHitting.csv'
    #f = open(fileName, 'w')
    #headers = 'Rank, Player, Team, Position, Games, At Bats, Runs, Hits, Doubles, Triples, Home Runs, Runs Batted, Walks, Strikeout, Bases Stolen, Caught Stealing, Avg. Hits (hits/at bats), On-base %, Slugging %, O+S\n'
    #f.write(headers)

    my_url = "http://mlb.mlb.com/stats/sortable_es.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+hitting&game_type='R'&season=2018&season_type=ANY&league_code='MLB'&sectionType=sp&statType=hitting&page=1&ts=1569359008122&playerType=QUALIFIER&sportCode='mlb'&split=&team_id=&active_sw=&position=&page_type=SortablePlayer&sortOrder='desc'&sortColumn=avg&results=&perPage=50&timeframe=&last_x_days=&extended=0"

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
            pos = row.find_all('td', {'class': 'dg-pos'})
            noJuegos = row.find_all('td', {'class': 'dg-g'})
            ab = row.find_all('td', {'class': 'dg-ab'})
            carreras = row.find_all('td', {'class': 'dg-r'})
            hits = row.find_all('td', {'class': 'dg-h'})
            doble = row.find_all('td', {'class': 'dg-d'})
            triple = row.find_all('td', {'class': 'dg-t'})
            homeRuns = row.find_all('td', {'class': 'dg-hr'})
            impulsadas = row.find_all('td', {'class': 'dg-rbi'})
            baseXbola = row.find_all('td', {'class': 'dg-bb'})
            strikeout = row.find_all('td', {'class': 'dg-so'})
            baseRobada = row.find_all('td', {'class': 'dg-sb'})
            caught = row.find_all('td', {'class': 'dg-cs'})
            avgHits = row.find_all('td', {'class': 'dg-avg'})
            onBasePercent = row.find_all('td', {'class': 'dg-obp'})
            sluggingPercent = row.find_all('td', {'class': 'dg-slg'})
            sumaPercent = row.find_all('td', {'class': 'dg-ops'})

            insert.playerHitting(
                db,
                jugador[0].a.text,
                equipo[0].text,
                pos[0].text,
                rank[0].text,
                noJuegos[0].text,
                avgHits[0].text,
                ab[0].text,
                carreras[0].text,
                hits[0].text,
                homeRuns[0].text,
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