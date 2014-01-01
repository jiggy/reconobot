import urllib2

def get_empsit_data():
    empsit = urllib2.urlopen('http://www.bls.gov/news.release/empsit.a.htm')
    print empsit.info()

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

print get_empsit_data()