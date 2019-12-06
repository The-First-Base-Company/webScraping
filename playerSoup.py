import bs4 as bs
import re
from bs4 import BeautifulSoup as soup
import selenium
from selenium import webdriver
import time
import pymysql
import insert


def getPlayerHitting(host, user, password, database):

    db = pymysql.connect(host, user, password, database)

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
    #print(totalPages[0].text)

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

            player_bio = getPlayerInfo(jugador[0].a['href'])

            foto = player_bio[0]
            nombre = player_bio[1]
            numero = player_bio[2]
            altura = player_bio[3]
            edad = player_bio[4]
            nickname = player_bio[5]
            nacimiento = player_bio[6]
            draft_año = player_bio[7]
            draft_equipo = player_bio[8]
            draft_ronda = player_bio[9]
            debut = player_bio[10]

            insert.playerHitting(
                db,
                foto,
                nombre,
                numero,
                altura,
                edad,
                nickname,
                nacimiento,
                draft_año,
                draft_equipo,
                draft_ronda,
                debut,
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


def getPlayerPitching(host, user, password, database):

    db = pymysql.connect(host, user, password, database)

    print("getting player pitching stats ...")

    #fileName = 'playerHitting.csv'
    #f = open(fileName, 'w')
    #headers = 'Rank, Player, Team, Position, Games, At Bats, Runs, Hits, Doubles, Triples, Home Runs, Runs Batted, Walks, Strikeout, Bases Stolen, Caught Stealing, Avg. Hits (hits/at bats), On-base %, Slugging %, O+S\n'
    #f.write(headers)

    my_url = "http://mlb.mlb.com/stats/sortable_es.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+pitching&game_type='R'&season=2018&season_type=ANY&league_code='MLB'&sectionType=sp&statType=pitching&page=1&ts=1572842167057&playerType=QUALIFIER&sportCode='mlb'&split=&team_id=&active_sw=&position='1'&page_type=SortablePlayer&sortOrder='desc'&sortColumn=avg&results=&perPage=50&timeframe=&last_x_days=&extended=0"

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
            victoria = row.find_all('td', {'class': 'dg-w'})
            derrota = row.find_all('td', {'class': 'dg-l'})
            era = row.find_all('td', {'class': 'dg-era'})
            g = row.find_all('td', {'class': 'dg-g'})
            gs = row.find_all('td', {'class': 'dg-gs'})
            sv = row.find_all('td', {'class': 'dg-sv'})
            svo = row.find_all('td', {'class': 'dg-svo'})
            dfip = row.find_all('td', {'class': 'dg-ip'})
            h = row.find_all('td', {'class': 'dg-h'})
            r = row.find_all('td', {'class': 'dg-r'})
            dger = row.find_all('td', {'class': 'dg-er'})
            hr = row.find_all('td', {'class': 'dg-hr'})
            bb = row.find_all('td', {'class': 'dg-bb'})
            so = row.find_all('td', {'class': 'dg-so'})
            dgavg = row.find_all('td', {'class': 'dg-avg'})
            whip = row.find_all('td', {'class': 'dg-whip'})

            player_bio = getPlayerInfo(jugador[0].a['href'])

            foto = player_bio[0]
            nombre = player_bio[1]
            numero = player_bio[2]
            altura = player_bio[3]
            edad = player_bio[4]
            nickname = player_bio[5]
            nacimiento = player_bio[6]
            draft_año = player_bio[7]
            draft_equipo = player_bio[8]
            draft_ronda = player_bio[9]
            debut = player_bio[10]

            insert.playerPitching(
                db,
                foto,
                nombre,
                numero,
                altura,
                edad,
                nickname,
                nacimiento,
                draft_año,
                draft_equipo,
                draft_ronda,
                debut,
                equipo[0].text,
                rank[0].text,
                g[0].text,
                dgavg[0].text,
                r[0].text,
                h[0].text,
                hr[0].text,
                victoria[0].text,
                derrota[0].text,
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


def getPlayerFielding(host, user, password, database):

    db = pymysql.connect(host, user, password, database)

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
    time.sleep(5)
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

            player_bio = getPlayerInfo(jugador[0].a['href'])
            nombre = player_bio[1]
            numero = player_bio[2]

            insert.playerFielding(
                db,
                nombre,
                numero,
                pos[0].text,
                rank[0].text,
                chances[0].text,
                putout[0].text,
                assists[0].text,
                errors[0].text,
                fpct[0].text,
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


def transformDate(date):
    date = date.split("/")
    #print(date)
    if (len(date[0]) == 1):
        date = date[2] + '-' + '0' + date[0] + '-' + date[1]
    else:
        date = date[2] + '-' + date[0] + '-' + date[1]
    #print(date)
    return date


def calculateAge(date):
    date = date.split("/")
    #print(date)
    age = 2019 - int(date[2])
    #print(date)
    return age


def getPlayerInfo(playerURL):
    my_url = "http://mlb.com" + playerURL

    browser = webdriver.Firefox()
    browser.get(my_url)
    try:
        html = browser.page_source
        webpageSoup = bs.BeautifulSoup(html, 'html.parser')
        time.sleep(3)

        picture = webpageSoup.find('img', {'class': 'player-headshot'})['src']
        name = webpageSoup.find('span', {
            'class': 'player-header--vitals-name'
        }).text
        number = webpageSoup.find('span', {
            'class': 'player-header--vitals-number'
        }).text

        height = webpageSoup.find('li',
                                  {'class': 'player-header--vitals-height'})
        height = height.text[height.text.find("/") + 1:len(height.text)]

        missingAge = False

        if (str(webpageSoup).find("Age: ") > 0):
            age = webpageSoup.find('li', {
                'class': 'player-header--vitals-age'
            }).text.replace("Age: ", "")
        else:
            missingAge = True

        bio = webpageSoup.find_all('ul', attrs={'class': None})
        bio = bio[1].find_all('li')

        #full_name = bio[0].text[bio[0].text.find(":") + 1 : len(bio[0].text)].strip()
        #nickname = bio[1].text[bio[1].text.find(":") + 1 : len(bio[1].text)].strip()

        #birth = bio[2].text[bio[2].text.find(":") + 1 : bio[2].text.find(":") + 12].strip()
        #birth = transformDate(birth)
        nickname = 'NULL'
        birth = 'NULL'
        draft_year = 'NULL'
        draft_team = 'NULL'
        draft_round = 'NULL'
        debut = 'NULL'

        i = 0
        for info in bio:
            if (bio[i].span.text == 'Nickname:'):
                nickname = bio[i].text[bio[i].text.find(":") +
                                       1:len(bio[i].text)].strip()
            if (bio[i].span.text == 'Born:'):
                birth = bio[i].text[bio[i].text.find(":") +
                                    1:bio[i].text.find(":") + 12].strip()
                birth = transformDate(birth)
                if missingAge:
                    age = bio[i].text[bio[i].text.find(":") +
                                      1:bio[i].text.find(":") + 12].strip()
                    age = calculateAge(age)
            if (bio[i].span.text == 'Draft:'):
                draft = bio[i].text[bio[i].text.find(":") +
                                    1:len(bio[i].text)].strip().replace(
                                        "Round:",
                                        "").replace("Overall Pick:",
                                                    "").split(",")
                draft_year = draft[0].strip()
                draft_team = draft[1].strip()
                draft_round = draft[2].strip()
            if (bio[i].span.text == 'Debut:'):
                debut = bio[i].text[bio[i].text.find(":") +
                                    1:len(bio[i].text)].strip()
                debut = transformDate(debut)
            i += 1
        '''
        draft = bio[3].text[bio[3].text.find(":") + 1 : len(bio[3].text)].strip().replace("Round:", "").replace("Overall Pick:", "").split(",")
        draft_year = draft[0].strip()
        draft_team = draft[1].strip()
        draft_round = draft[2].strip()

        debut = bio[5].text[bio[5].text.find(":") + 1 : len(bio[5].text)].strip()
        debut = transformDate(debut)

        '''
        player_bio = [
            picture, name, number, height, age, nickname, birth, draft_year,
            draft_team, draft_round, debut
        ]
        browser.close()
        return player_bio
    except:
        pass


#print(getPlayerInfo("/team/player.jsp?lang=es&player_id=542255"))


def getStats(host, user, password, database):
    #getPlayerHitting(host, user, password, database)
    #getPlayerPitching(host, user, password, database)
    getPlayerFielding(host, user, password, database)