import bs4 as bs
import re
from bs4 import BeautifulSoup as soup
import selenium
from selenium import webdriver
import time
import pymysql
import insert


def getPlayerHitting():

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

    firstTable = webpageSoup.find_all('tr', {'tabindex': '0'})
    #print(tableRows)
    #print(len(tableRows)) #50/50

    for row in firstTable:

        rank = row.find_all('td', {'class': 'dg-rank'})
        jugador = row.find_all('td', {'class': 'dg-name_display_last_init'})
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

        #f.write(rank[0].text + ',' + '"' + jugador[0].a.text + '"' + ',' + equipo[0].text + ',' + pos[0].text + ',' + noJuegos[0].text + ',' + ab[0].text + ',' + carreras[0].text + ',' + hits[0].text + ',' + doble[0].text + ',' + triple[0].text + ',' + homeRuns[0].text + ',' + impulsadas[0].text + ',' + baseXbola[0].text + ',' + strikeout[0].text + ',' + baseRobada[0].text + ',' + caught[0].text + ',' + avgHits[0].text + ',' + onBasePercent[0].text + ',' + sluggingPercent[0].text + ',' + sumaPercent[0].text + '\n')

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

    print('loading second page ...')

    secondPage = browser.find_elements_by_xpath(
        '/html/body/div[2]/div/div[3]/div/div[1]/div[11]/fieldset/button[4]')
    secondPage[0].click()

    time.sleep(3)

    html = browser.page_source
    webpageSoup = bs.BeautifulSoup(html, 'html.parser')

    secondTable = webpageSoup.find_all('tr', {'tabindex': '0'})

    for row in secondTable:

        rank = row.find_all('td', {'class': 'dg-rank'})
        jugador = row.find_all('td', {'class': 'dg-name_display_last_init'})
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

        #f.write(rank[0].text + ',' + '"' + jugador[0].a.text + '"' + ',' + equipo[0].text + ',' + pos[0].text + ',' + noJuegos[0].text + ',' + ab[0].text + ',' + carreras[0].text + ',' + hits[0].text + ',' + doble[0].text + ',' + triple[0].text + ',' + homeRuns[0].text + ',' + impulsadas[0].text + ',' + baseXbola[0].text + ',' + strikeout[0].text + ',' + baseRobada[0].text + ',' + caught[0].text + ',' + avgHits[0].text + ',' + onBasePercent[0].text + ',' + sluggingPercent[0].text + ',' + sumaPercent[0].text + '\n')
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
    print('loading third page ...')

    thirdPage = browser.find_elements_by_xpath(
        '/html/body/div[2]/div/div[3]/div/div[1]/div[11]/fieldset/button[4]')
    thirdPage[0].click()

    time.sleep(3)

    html = browser.page_source
    webpageSoup = bs.BeautifulSoup(html, 'html.parser')

    thirdTable = webpageSoup.find_all('tr', {'tabindex': '0'})

    for row in thirdTable:
        rank = row.find_all('td', {'class': 'dg-rank'})
        jugador = row.find_all('td', {'class': 'dg-name_display_last_init'})
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

        #f.write(rank[0].text + ',' + '"' + jugador[0].a.text + '"' + ',' + equipo[0].text + ',' + pos[0].text + ',' + noJuegos[0].text + ',' + ab[0].text + ',' + carreras[0].text + ',' + hits[0].text + ',' + doble[0].text + ',' + triple[0].text + ',' + homeRuns[0].text + ',' + impulsadas[0].text + ',' + baseXbola[0].text + ',' + strikeout[0].text + ',' + baseRobada[0].text + ',' + caught[0].text + ',' + avgHits[0].text + ',' + onBasePercent[0].text + ',' + sluggingPercent[0].text + ',' + sumaPercent[0].text + '\n')

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

    #f.close()
    browser.close()
    db.close()


def getPlayerPitching():

    db = pymysql.connect("localhost", "root", "", "firstbase")

    print("getting player pitching stats ...")

    #fileName = 'playerPitching.csv'
    #f = open(fileName, 'w')
    #headers = 'Wins, Losses, Avg. Earned Runs, Games, Games Started, Saves, Save Opportunities, Innings Pitched, Hits Allowed, Runs Allowed, Earned Runs Allowed, Home Runs Allowed, Base on Balls, Strikeouts, Avg. (Hits / At Bats), WHIP ((H+W)/IP)\n'
    #f.write(headers)

    my_url = "http://mlb.mlb.com/stats/sortable_es.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+pitching&game_type='R'&season=2019&season_type=ANY&league_code='MLB'&sectionType=sp&statType=pitching&page=1&ts=1569861695577&playerType=QUALIFIER&sportCode='mlb'&split=&team_id=&active_sw=&position=&page_type=SortablePlayer&sortOrder='desc'&sortColumn=avg&results=&perPage=50&timeframe=&last_x_days=&extended=0"

    browser = webdriver.Firefox()
    browser.get(my_url)

    html = browser.page_source
    webpageSoup = bs.BeautifulSoup(html, 'html.parser')

    firstTable = webpageSoup.find_all('tr', {'tabindex': '0'})

    for row in firstTable:
        rank = row.find_all('td', {'class': 'dg-rank'})
        jugador = row.find_all('td', {'class': 'dg-name_display_last_init'})
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

        #f.write(rank[0].text + ',' + '"' + jugador[0].a.text + '"' + ',' + equipo[0].text + ',' + victoria[0].text + ',' + derrota[0].text + ',' +era[0].text + ',' + g[0].text + ',' + gs[0].text + ',' + sv[0].text + ',' + svo[0].text + ',' + dfip[0].text + ',' + h[0].text + ',' + r[0].text + ',' + dger[0].text + ',' + hr[0].text + ',' + bb[0].text + ',' + so[0].text + ',' + dgavg[0].text + ',' + whip[0].text + '\n')

        insert.playerPitching(
            db,
            jugador[0].a.text,
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

    print('loading second page ...')

    secondPage = browser.find_elements_by_xpath(
        '/html/body/div[2]/div/div[3]/div/div[1]/div[11]/fieldset/button[4]')
    secondPage[0].click()

    time.sleep(3)

    html = browser.page_source
    webpageSoup = bs.BeautifulSoup(html, 'html.parser')

    secondTable = webpageSoup.find_all('tr', {'tabindex': '0'})

    for row in secondTable:
        rank = row.find_all('td', {'class': 'dg-rank'})
        jugador = row.find_all('td', {'class': 'dg-name_display_last_init'})
        equipo = row.find_all('td', {'class': 'dg-team_abbrev'})
        victoria = row.find_all('td', {'class': 'dg-w'})
        derrota = row.find_all('td', {'class': 'dg-l'})
        era = row.find_all('td', {'class': 'dg-era'})
        g = row.find_all('td', {'class': 'dg-g'})
        gs = row.find_all('td', {'class': 'dg-gs'})
        sv = row.find_all('td', {'class': 'dg-sv'})
        svo = row.find_all('td', {'class': 'dg-svo'})
        dfip = row.find_all('td', {'class': 'dg-ip'})
        dgh = row.find_all('td', {'class': 'dg-h'})
        dgr = row.find_all('td', {'class': 'dg-r'})
        dger = row.find_all('td', {'class': 'dg-er'})
        dghr = row.find_all('td', {'class': 'dg-hr'})
        bb = row.find_all('td', {'class': 'dg-bb'})
        so = row.find_all('td', {'class': 'dg-so'})
        dgavg = row.find_all('td', {'class': 'dg-avg'})
        whip = row.find_all('td', {'class': 'dg-whip'})

        #f.write(rank[0].text + ',' + '"' + jugador[0].a.text + '"' + ',' + equipo[0].text + ',' + victoria[0].text + ',' + derrota[0].text + ',' +era[0].text + ',' + g[0].text + ',' + gs[0].text + ',' + sv[0].text + ',' + svo[0].text + ',' + dfip[0].text + ',' + dgh[0].text + ',' + dgr[0].text + ',' + dger[0].text + ',' + dghr[0].text + ',' + bb[0].text + ',' + so[0].text + ',' + dgavg[0].text + ',' + whip[0].text + '\n')

        insert.playerPitching(
            db,
            jugador[0].a.text,
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
    #f.close()
    browser.close()
    db.close()


def getPlayerFielding():

    db = pymysql.connect("localhost", "root", "", "firstbase")

    print("getting player fielding stats ...")

    #fileName = 'playerFielding.csv'
    #f = open(fileName, 'w')
    #headers = 'Games, Games Started, Innings, Total Chances, Putout, Total Assists, Total Error, Double Plays, Stolen Bases, Caught Stealing, Stolen Base Percentage, Passed Balls, Wild Pitches, Average of errors, Range Factor\n'
    #f.write(headers)

    my_url = "http://mlb.mlb.com/stats/sortable_es.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+fielding&game_type='R'&season=2019&season_type=ANY&league_code='MLB'&sectionType=sp&statType=fielding&page=1&ts=1569886534691&playerType=QUALIFIER&sportCode='mlb'&split=&team_id=&active_sw=&position=&page_type=SortablePlayer&sortOrder='desc'&sortColumn=avg&results=&perPage=50&timeframe=&last_x_days=&extended=0"

    browser = webdriver.Firefox()
    browser.get(my_url)

    html = browser.page_source
    webpageSoup = bs.BeautifulSoup(html, 'html.parser')

    firstTable = webpageSoup.find_all('tr', {'tabindex': '0'})

    for row in firstTable:
        rank = row.find_all('td', {'class': 'dg-rank'})
        jugador = row.find_all('td', {'class': 'dg-name_display_last_init'})
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
            pos[0].text,
            rank[0].text,
            juegos[0].text,
            chances[0].text,
            putout[0].text,
            assists[0].text,
            errors[0].text,
            fpct[0].text,
        )

    secondPage = browser.find_elements_by_xpath(
        '/html/body/div[2]/div/div[3]/div/div[1]/div[11]/fieldset/button[4]')
    print(secondPage)
    secondPage[0].click()

    time.sleep(3)

    html = browser.page_source
    webpageSoup = bs.BeautifulSoup(html, 'html.parser')

    secondTable = webpageSoup.find_all('tr', {'tabindex': '0'})

    for row in secondTable:
        rank = row.find_all('td', {'class': 'dg-rank'})
        jugador = row.find_all('td', {'class': 'dg-name_display_last_init'})
        equipo = row.find_all('td', {'class': 'dg-team_abbrev'})
        victoria = row.find_all('td', {'class': 'dg-position'})
        derrota = row.find_all('td', {'class': 'dg-g'})
        era = row.find_all('td', {'class': 'dg-gs'})
        g = row.find_all('td', {'class': 'dg-inn'})
        gs = row.find_all('td', {'class': 'dg-tc'})
        sv = row.find_all('td', {'class': 'dg-po'})
        svo = row.find_all('td', {'class': 'dg-a'})
        dfip = row.find_all('td', {'class': 'dg-e'})
        dgh = row.find_all('td', {'class': 'dg-dp'})
        dgr = row.find_all('td', {'class': 'dg-sb'})
        dger = row.find_all('td', {'class': 'dg-cs'})
        dghr = row.find_all('td', {'class': 'dg-sbpct'})
        bb = row.find_all('td', {'class': 'dg-pb'})
        so = row.find_all('td', {'class': 'dg-c_wp'})
        dgavg = row.find_all('td', {'class': 'dg-fpct'})
        whip = row.find_all('td', {'class': 'dg-rf'})

        #f.write(rank[0].text + ',' + '"' + jugador[0].a.text + '"' + ',' + equipo[0].text + ',' + victoria[0].text + ',' + derrota[0].text + ',' + era[0].text + ',' + g[0].text + ',' + gs[0].text + ',' + sv[0].text + ',' + svo[0].text + ',' + dfip[0].text + ',' + dgh[0].text + ',' + dgr[0].text + ',' + dger[0].text + ',' + dghr[0].text + ',' + bb[0].text + ',' + so[0].text + ',' + dgavg[0].text + ',' + whip[0].text + '\n')

        insert.playerFielding(
            db,
            jugador[0].a.text,
            equipo[0].text,
            pos[0].text,
            rank[0].text,
            juegos[0].text,
            chances[0].text,
            putout[0].text,
            assists[0].text,
            errors[0].text,
            fpct[0].text,
        )

    thirdPage = browser.find_elements_by_xpath(
        '/html/body/div[2]/div/div[3]/div/div[1]/div[11]/fieldset/button[4]')
    thirdPage[0].click()

    time.sleep(3)

    html = browser.page_source
    webpageSoup = bs.BeautifulSoup(html, 'html.parser')

    thirdTable = webpageSoup.find_all('tr', {'tabindex': '0'})

    for row in thirdTable:
        rank = row.find_all('td', {'class': 'dg-rank'})
        jugador = row.find_all('td', {'class': 'dg-name_display_last_init'})
        equipo = row.find_all('td', {'class': 'dg-team_abbrev'})
        victoria = row.find_all('td', {'class': 'dg-position'})
        derrota = row.find_all('td', {'class': 'dg-g'})
        era = row.find_all('td', {'class': 'dg-gs'})
        g = row.find_all('td', {'class': 'dg-inn'})
        gs = row.find_all('td', {'class': 'dg-tc'})
        sv = row.find_all('td', {'class': 'dg-po'})
        svo = row.find_all('td', {'class': 'dg-a'})
        dfip = row.find_all('td', {'class': 'dg-e'})
        dgh = row.find_all('td', {'class': 'dg-dp'})
        dgr = row.find_all('td', {'class': 'dg-sb'})
        dger = row.find_all('td', {'class': 'dg-cs'})
        dghr = row.find_all('td', {'class': 'dg-sbpct'})
        bb = row.find_all('td', {'class': 'dg-pb'})
        so = row.find_all('td', {'class': 'dg-c_wp'})
        dgavg = row.find_all('td', {'class': 'dg-fpct'})
        whip = row.find_all('td', {'class': 'dg-rf'})

        #f.write(rank[0].text + ',' + '"' + jugador[0].a.text + '"' + ',' + equipo[0].text + ',' + victoria[0].text + ',' + derrota[0].text + ',' + era[0].text + ',' + g[0].text + ',' + gs[0].text + ',' + sv[0].text + ',' + svo[0].text + ',' + dfip[0].text + ',' + dgh[0].text + ',' + dgr[0].text + ',' + dger[0].text + ',' + dghr[0].text + ',' + bb[0].text + ',' + so[0].text + ',' + dgavg[0].text + ',' + whip[0].text + '\n')

        insert.playerFielding(
            db,
            jugador[0].a.text,
            equipo[0].text,
            pos[0].text,
            rank[0].text,
            juegos[0].text,
            chances[0].text,
            putout[0].text,
            assists[0].text,
            errors[0].text,
            fpct[0].text,
        )

    fourthPage = browser.find_elements_by_xpath(
        '/html/body/div[2]/div/div[3]/div/div[1]/div[11]/fieldset/button[4]')
    fourthPage[0].click()

    time.sleep(3)

    html = browser.page_source
    webpageSoup = bs.BeautifulSoup(html, 'html.parser')

    fourthTable = webpageSoup.find_all('tr', {'tabindex': '0'})

    for row in fourthTable:
        rank = row.find_all('td', {'class': 'dg-rank'})
        jugador = row.find_all('td', {'class': 'dg-name_display_last_init'})
        equipo = row.find_all('td', {'class': 'dg-team_abbrev'})
        victoria = row.find_all('td', {'class': 'dg-position'})
        derrota = row.find_all('td', {'class': 'dg-g'})
        era = row.find_all('td', {'class': 'dg-gs'})
        g = row.find_all('td', {'class': 'dg-inn'})
        gs = row.find_all('td', {'class': 'dg-tc'})
        sv = row.find_all('td', {'class': 'dg-po'})
        svo = row.find_all('td', {'class': 'dg-a'})
        dfip = row.find_all('td', {'class': 'dg-e'})
        dgh = row.find_all('td', {'class': 'dg-dp'})
        dgr = row.find_all('td', {'class': 'dg-sb'})
        dger = row.find_all('td', {'class': 'dg-cs'})
        dghr = row.find_all('td', {'class': 'dg-sbpct'})
        bb = row.find_all('td', {'class': 'dg-pb'})
        so = row.find_all('td', {'class': 'dg-c_wp'})
        dgavg = row.find_all('td', {'class': 'dg-fpct'})
        whip = row.find_all('td', {'class': 'dg-rf'})

        #f.write(rank[0].text + ',' + '"' + jugador[0].a.text + '"' + ',' + equipo[0].text + ',' + victoria[0].text + ',' + derrota[0].text + ',' + era[0].text + ',' + g[0].text + ',' + gs[0].text + ',' + sv[0].text + ',' + svo[0].text + ',' + dfip[0].text + ',' + dgh[0].text + ',' + dgr[0].text + ',' + dger[0].text + ',' + dghr[0].text + ',' + bb[0].text + ',' + so[0].text + ',' + dgavg[0].text + ',' + whip[0].text + '\n')

        insert.playerFielding(
            db,
            jugador[0].a.text,
            equipo[0].text,
            pos[0].text,
            rank[0].text,
            juegos[0].text,
            chances[0].text,
            putout[0].text,
            assists[0].text,
            errors[0].text,
            fpct[0].text,
        )

    fifthPage = browser.find_elements_by_xpath(
        '/html/body/div[2]/div/div[3]/div/div[1]/div[11]/fieldset/button[4]')
    fifthPage[0].click()

    time.sleep(3)

    html = browser.page_source
    webpageSoup = bs.BeautifulSoup(html, 'html.parser')

    fifthTable = webpageSoup.find_all('tr', {'tabindex': '0'})

    for row in fifthTable:
        rank = row.find_all('td', {'class': 'dg-rank'})
        jugador = row.find_all('td', {'class': 'dg-name_display_last_init'})
        equipo = row.find_all('td', {'class': 'dg-team_abbrev'})
        victoria = row.find_all('td', {'class': 'dg-position'})
        derrota = row.find_all('td', {'class': 'dg-g'})
        era = row.find_all('td', {'class': 'dg-gs'})
        g = row.find_all('td', {'class': 'dg-inn'})
        gs = row.find_all('td', {'class': 'dg-tc'})
        sv = row.find_all('td', {'class': 'dg-po'})
        svo = row.find_all('td', {'class': 'dg-a'})
        dfip = row.find_all('td', {'class': 'dg-e'})
        dgh = row.find_all('td', {'class': 'dg-dp'})
        dgr = row.find_all('td', {'class': 'dg-sb'})
        dger = row.find_all('td', {'class': 'dg-cs'})
        dghr = row.find_all('td', {'class': 'dg-sbpct'})
        bb = row.find_all('td', {'class': 'dg-pb'})
        so = row.find_all('td', {'class': 'dg-c_wp'})
        dgavg = row.find_all('td', {'class': 'dg-fpct'})
        whip = row.find_all('td', {'class': 'dg-rf'})

        #f.write(rank[0].text + ',' + '"' + jugador[0].a.text + '"' + ',' + equipo[0].text + ',' + victoria[0].text + ',' + derrota[0].text + ',' + era[0].text + ',' + g[0].text + ',' + gs[0].text + ',' + sv[0].text + ',' + svo[0].text + ',' + dfip[0].text + ',' + dgh[0].text + ',' + dgr[0].text + ',' + dger[0].text + ',' + dghr[0].text + ',' + bb[0].text + ',' + so[0].text + ',' + dgavg[0].text + ',' + whip[0].text + '\n')

        insert.playerFielding(
            db,
            jugador[0].a.text,
            equipo[0].text,
            pos[0].text,
            rank[0].text,
            juegos[0].text,
            chances[0].text,
            putout[0].text,
            assists[0].text,
            errors[0].text,
            fpct[0].text,
        )

    #f.close()
    browser.close()
    db.close()


getPlayerHitting()
getPlayerPitching()
getPlayerFielding()