from requests import get
from bs4 import BeautifulSoup

class Constituency:
    
    def __init__(self):
        self.name = ''
        self.code = ''
        self.url = ''
        self.nation = ''
        self.turnout = 0
        #self.profile = ''
        self.candidates = []

class Candidate:
    
    def __init__(self):
        self.party_short_name = ''
        self.party_long_name = ''
        #self.party_colour = ''
        self.name = ''
        self.votes = 0
        self.votes_share_perc = 0
        self.votes_net = 0
        
print('|'.join(['constituency_name', 'constituency_nation', 'constituency_code', 'constituency_turnout', 'candidate_party_short_name', 'candidate_party_long_name', 'candidate_name', 'candidate_votes', 'candidate_votes_share', 'candidate_votes_net']))

constituencies_list_url = 'http://www.bbc.co.uk/news/politics/constituencies'
constituencies_list_html = get(constituencies_list_url).content
constituencies_list_dom = BeautifulSoup(constituencies_list_html)

constituency_az_tables = constituencies_list_dom.find_all('table', class_='az-table')

for constituency_az_table in constituency_az_tables:
    table_constituencies = constituency_az_table.tbody.find_all('tr')
    
    for constituency_row in table_constituencies:
        
        constituency = Constituency()
        
        constituency.url = constituency_row.th.a['href']
        constituency.name = constituency_row.th.a.string
        constituency.nation = constituency_row.td.string
        constituency.code = constituency.url[-9:]
        
        constituency_url = 'http://www.bbc.co.uk' + constituency.url
        constituency_html = get(constituency_url).content
        constituency_dom = BeautifulSoup(constituency_html)
        
        constituency.turnout = constituency_dom.find('div', class_='results-turnout__percentage').find('span', class_='results-turnout__value').string
        #constituency.profile = constituency_dom.find('div', class_='constituency-profile__text').contents
        
        #print(', '.join([constituency.name, constituency.nation, constituency.code, constituency.turnout]))
        
        parties = constituency_dom.find('div', class_='parties').find_all('div', class_='party')
        
        for party_row in parties:
            
            candidate = Candidate()
            
            candidate.party_short_name = list(party_row.find('div', class_='party__name').find('div', class_='party__name--short').strings)[1]
            candidate.party_long_name = party_row.find('div', class_='party__name').find('div', class_='party__name--long').string
            candidate.name = list(party_row.find('div', class_='party__name').find('div', class_='party__result--candidate').strings)[1]
            
            candidate.votes = list(party_row.ul.find('li', class_='party__result--votes').strings)[0]
            candidate.votes_share = list(party_row.ul.find('li', class_='party__result--votesshare').strings)[0]
            candidate.votes_net = list(party_row.ul.find('li', class_='party__result--votesnet').strings)[0]
            
            print('|'.join([constituency.name, constituency.nation, constituency.code, constituency.turnout, candidate.party_short_name, candidate.party_long_name, candidate.name, candidate.votes, candidate.votes_share, candidate.votes_net]))