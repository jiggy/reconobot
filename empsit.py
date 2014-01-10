import urllib2
import util
from bs4 import BeautifulSoup

bls_cfg = util.get_config("bls")
bls_url = bls_cfg['summary_table_url']

def get_empsit_data():
    empsit = urllib2.urlopen(bls_url)

    soup = BeautifulSoup(empsit.read())
    data_table = soup.find(id='cps_empsit_sum')

    highlights = {'Participation rate':{},
                  'Employment-population ratio':{},
                  'Unemployment rate':{}}
    for row in data_table.findAll('tr'):
        if row.th and row.th.text in highlights:
            cells = row.findAll('td')
            if len(cells) == 5:
                highlights[row.th.text] = {'year_ago' : cells[0].text,
                        'two_months_ago' : cells[1].text,
                        'last_month' : cells[2].text,
                        'this_month' : cells[3].text,
                        'change' : cells[4].text
                }

    empsit.close()
    return highlights

def generate_headline(data):
    headline = "BLS Report: "
    first = True
    for key in data.keys():
        val = data[key]['this_month']
        change = float(data[key]['change'])
        if change == 0:
            change = 'unchanged at'
        elif change > 0:
            change = "+" + str(change) + " to"
        else:
            change = str(change) + " to"
        if first == False:
            headline = headline + ", "
        headline = headline + " " + key + " " + change + " " + val
        first = False
    return headline