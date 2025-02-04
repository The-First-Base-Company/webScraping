import bs4 as bs
import re
from bs4 import BeautifulSoup as soup
import selenium
from selenium import webdriver
import time
import pymysql
import insert


def getTeamHitting(host, user, password, database):
    db = pymysql.connect(host, user, password, database)
    print("getting team hitting stats ...")

    my_url = "http://mlb.mlb.com/stats/sortable_es.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Team+hitting&game_type='R'&season=2018&season_type=ANY&league_code='MLB'&sectionType=st&statType=hitting&page=1&ts=1569862744719&playerType=QUALIFIER&sportCode='mlb'&split=&team_id=&active_sw=&position=&page_type=SortablePlayer&sortOrder='asc'&sortColumn=avg&results=&perPage=50&timeframe=&last_x_days=&extended=0"

    browser = webdriver.Firefox()
    browser.get(my_url)

    html = browser.page_source
    webpageSoup = bs.BeautifulSoup(html, 'html.parser')

    table = webpageSoup.find_all('tr', {'tabindex': '0'})

    for row in table:
        rank = row.find_all('td', {'class': 'dg-rank'})
        team = row.find_all('td', {'class': 'dg-team_full'})
        league = row.find_all('td', {'class': 'dg-league'})
        g = row.find_all('td', {'class': 'dg-g'})
        ab = row.find_all('td', {'class': 'dg-ab'})
        r = row.find_all('td', {'class': 'dg-r'})
        h = row.find_all('td', {'class': 'dg-h'})
        dobles = row.find_all('td', {'class': 'dg-d'})
        triples = row.find_all('td', {'class': 'dg-t'})
        hr = row.find_all('td', {'class': 'dg-hr'})
        rbi = row.find_all('td', {'class': 'dg-rbi'})
        bb = row.find_all('td', {'class': 'dg-bb'})
        so = row.find_all('td', {'class': 'dg-so'})
        sb = row.find_all('td', {'class': 'dg-sb'})
        cs = row.find_all('td', {'class': 'dg-cs'})
        avg = row.find_all('td', {'class': 'dg-avg'})
        obp = row.find_all('td', {'class': 'dg-obp'})
        slg = row.find_all('td', {'class': 'dg-slg'})
        ops = row.find_all('td', {'class': 'dg-ops'})

        # f.write(rank[0].text + ',' + '"' + team[0].a.text + '"' + ',' + league[0].text + ',' + g[0].text + ',' + ab[0].text + ',' + r[0].text + ',' + h[0].text + ',' + g[0].text + ',' + dobles[0].text + ',' + triples[0].text + ',' + hr[0].text + ',' + rbi[0].text + ',' + bb[0].text + ',' + so[0].text + ',' + sb[0].text + ',' + cs[0].text + ',' + avg[0].text + ',' + obp[0].text + ',' + slg[0].text + ',' + ops[0].text + '\n')
        insert.teamHitting(
            db,
            team[0].text,
            league[0].text,
            rank[0].text,
            g[0].text,
            avg[0].text,
            ab[0].text,
            r[0].text,
            h[0].text,
            hr[0].text,
            rank[0].text,
        )
    #f.close()
    browser.close()
    db.close()


def getTeamPitching(host, user, password, database):
    db = pymysql.connect(host, user, password, database)
    print("getting team pitching stats ...")

    my_url = "http://mlb.mlb.com/stats/sortable_es.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Team+pitching&game_type='R'&season=2018&season_type=ANY&league_code='MLB'&sectionType=st&statType=pitching&page=1&ts=1569863704782&playerType=QUALIFIER&sportCode='mlb'&split=&team_id=&active_sw=&position=&page_type=SortablePlayer&sortOrder='asc'&sortColumn=avg&results=&perPage=50&timeframe=&last_x_days=&extended=0"

    browser = webdriver.Firefox()
    browser.get(my_url)

    html = browser.page_source
    webpageSoup = bs.BeautifulSoup(html, 'html.parser')

    table = webpageSoup.find_all('tr', {'tabindex': '0'})

    for row in table:
        rank = row.find_all('td', {'class': 'dg-rank'})
        team = row.find_all('td', {'class': 'dg-team_full'})
        league = row.find_all('td', {'class': 'dg-league'})
        w = row.find_all('td', {'class': 'dg-w'})
        l = row.find_all('td', {'class': 'dg-l'})
        era = row.find_all('td', {'class': 'dg-era'})
        g = row.find_all('td', {'class': 'dg-g'})
        gs = row.find_all('td', {'class': 'dg-gs'})
        sv = row.find_all('td', {'class': 'dg-sv'})
        svo = row.find_all('td', {'class': 'dg-svo'})
        ip = row.find_all('td', {'class': 'dg-ip'})
        h = row.find_all('td', {'class': 'dg-h'})
        r = row.find_all('td', {'class': 'dg-r'})
        er = row.find_all('td', {'class': 'dg-er'})
        hr = row.find_all('td', {'class': 'dg-hr'})
        bb = row.find_all('td', {'class': 'dg-bb'})
        so = row.find_all('td', {'class': 'dg-so'})
        avg = row.find_all('td', {'class': 'dg-avg'})
        whip = row.find_all('td', {'class': 'dg-whip'})

        # f.write(rank[0].text + ',' + '"' + team[0].a.text + '"' + ',' + league[0].text + ',' + w[0].text + ',' + l[0].text + ',' + era[0].text + ',' + g[0].text + ',' + gs[0].text + ',' + sv[0].text + ',' + svo[0].text + ',' + ip[0].text + ',' + h[0].text + ',' + r[0].text + ',' + er[0].text + ',' + hr[0].text + ',' + bb[0].text + ',' + so[0].text + ',' + avg[0].text + ',' + whip[0].text + '\n')
        insert.teamPitching(
            db,
            team[0].text,
            r[0].text,
            h[0].text,
            hr[0].text,
            avg[0].text,
            w[0].text,
            l[0].text,
            rank[0].text,
        )


#  f.close()
    browser.close()
    db.close()


def getTeamFielding(host, user, password, database):
    db = pymysql.connect(host, user, password, database)
    print("getting team pitching stats ...")

    my_url = "http://mlb.mlb.com/stats/sortable_es.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Team+fielding&game_type='R'&season=2018&season_type=ANY&league_code='MLB'&sectionType=st&statType=fielding&page=1&ts=1569864611630&playerType=QUALIFIER&sportCode='mlb'&split=&team_id=&active_sw=&position=&page_type=SortablePlayer&sortOrder='desc'&sortColumn=fpct&results=&perPage=50&timeframe=&last_x_days=&extended=0"

    browser = webdriver.Firefox()
    browser.get(my_url)

    html = browser.page_source
    webpageSoup = bs.BeautifulSoup(html, 'html.parser')

    table = webpageSoup.find_all('tr', {'tabindex': '0'})

    for row in table:
        rank = row.find_all('td', {'class': 'dg-rank'})
        team = row.find_all('td', {'class': 'dg-team_full'})
        league = row.find_all('td', {'class': 'dg-league'})
        g = row.find_all('td', {'class': 'dg-g'})
        gs = row.find_all('td', {'class': 'dg-gs'})
        inn = row.find_all('td', {'class': 'dg-inn'})
        tc = row.find_all('td', {'class': 'dg-tc'})
        po = row.find_all('td', {'class': 'dg-po'})
        a = row.find_all('td', {'class': 'dg-a'})
        e = row.find_all('td', {'class': 'dg-e'})
        dp = row.find_all('td', {'class': 'dg-dp'})
        sb = row.find_all('td', {'class': 'dg-sb'})
        cs = row.find_all('td', {'class': 'dg-cs'})
        sbpct = row.find_all('td', {'class': 'dg-sbpct'})
        pb = row.find_all('td', {'class': 'dg-pb'})
        c_wp = row.find_all('td', {'class': 'dg-c_wp'})
        fpct = row.find_all('td', {'class': 'dg-fpct'})
        der = row.find_all('td', {'class': 'dg-der'})

        #f.write(rank[0].text + ',' + '"' + team[0].a.text + '"' + ',' + league[0].text + ',' + g[0].text + ',' + gs[0].text + ',' + inn[0].text + ',' + tc[0].text + ',' + po[0].text + ',' + a[0].text + ',' + e[0].text + ',' + dp[0].text + ',' + sb[0].text + ',' + cs[0].text + ',' + sbpct[0].text + ',' + pb[0].text + ',' + c_wp[0].text + ',' + fpct[0].text + ',' + der[0].text + '\n')
        insert.teamFielding(
            db,
            team[0].text,
            tc[0].text,
            po[0].text,
            a[0].text,
            e[0].text,
            fpct[0].text,
            rank[0].text,
        )

    browser.close()
    db.close()

def getTeamInfo(host, user, password, database):
    db = pymysql.connect(host, user, password, database)
    print("getting teams ...")

    my_url = "https://www.mlb.com/team"

    browser = webdriver.Firefox()
    browser.get(my_url)

    html = browser.page_source
    webpageSoup = bs.BeautifulSoup(html, 'html.parser')

    photos = webpageSoup.find_all('div', {'class': 'p-image__image'})
    info = webpageSoup.find_all('div', {'class': 'p-wysiwyg'})
    names = webpageSoup.findAll('div', {'class': 'u-text-h4'})
    j = 0

    for i in photos:

        name = names[j].text.strip()
        logo = photos[j].img["data-srcset"]
        logo = logo[logo.find("568w") + 5 : logo.find("320w")]

        website = info[j].p.text
        website = website[website.find("Phone:") + 21: website.find(".com") + 4]

        estadio = str(info[j].p)
        estadio = estadio.replace("<br/>", "/")
        estadio = estadio[3: estadio.find("/")]

        insert.teamInfo(db, logo, website, estadio, name);
        j += 1

    browser.close()

def getStats(host, user, password, database):
    #getTeamHitting(host, user, password, database)
    #getTeamPitching(host, user, password, database)
    #getTeamFielding(host, user, password, database)
    getTeamInfo(host, user, password, database)