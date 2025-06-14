
import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_director_name(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    infobox = soup.find('table', class_='infobox ib-tv vevent')
    if infobox:
        for row in infobox.find_all('tr'):
            if row.th and 'Created by' in row.th.text:
                return row.td.text.strip()
    return "Director not found"


movie_urls = [
    'https://en.wikipedia.org/wiki/Stargate_SG-1',
    'https://en.wikipedia.org/wiki/Miami_Vice',
    'https://en.wikipedia.org/wiki/Buffy_the_Vampire_Slayer',
    'https://en.wikipedia.org/wiki/Sabrina_the_Teenage_Witch_(1996_TV_series)',
    'https://en.wikipedia.org/wiki/Space:_Above_and_Beyond',
    'https://en.wikipedia.org/wiki/Deadline_Gallipoli',
    'https://en.wikipedia.org/wiki/Lilyhammer',
    'https://en.wikipedia.org/wiki/The_A-Team',
    'https://en.wikipedia.org/wiki/Hannibal_(TV_series)',
    'https://en.wikipedia.org/wiki/Daredevil_(TV_series)',
    'https://en.wikipedia.org/wiki/Bewitched',
    'https://en.wikipedia.org/wiki/Constantine_(TV_series)',
    'https://en.wikipedia.org/wiki/Life_(American_TV_series)',
    'https://en.wikipedia.org/wiki/Sleepy_Hollow_(TV_series)',
    'https://en.wikipedia.org/wiki/Last_Man_Standing_(American_TV_series)',
    'https://en.wikipedia.org/wiki/The_Missing_(British_TV_series)',
    'https://en.wikipedia.org/wiki/Rules_of_Engagement_(TV_series)',
    'https://en.wikipedia.org/wiki/Sex_and_the_City',
    'https://en.wikipedia.org/wiki/Anger_Management_(TV_series)',
    'https://en.wikipedia.org/wiki/Unforgotten',
    'https://en.wikipedia.org/wiki/A_Touch_of_Frost',
    'https://en.wikipedia.org/wiki/Twisted_(TV_series)',
    'https://en.wikipedia.org/wiki/Defiance_(TV_series)',
    'https://en.wikipedia.org/wiki/Outlander_(TV_series)',
    'https://en.wikipedia.org/wiki/The_Returned_(French_TV_series)',
    'https://en.wikipedia.org/wiki/McHale%27s_Navy',
    'https://en.wikipedia.org/wiki/Arthur_(TV_series)',
    'https://en.wikipedia.org/wiki/3rd_Rock_from_the_Sun',
    'https://en.wikipedia.org/wiki/Rush_Hour_(American_TV_series)',
    'https://en.wikipedia.org/wiki/Hit_the_Floor_(TV_series)',
    'https://en.wikipedia.org/wiki/Luther_(TV_series)',
    'https://en.wikipedia.org/wiki/Friday_Night_Lights_(TV_series)',
    'https://en.wikipedia.org/wiki/The_Family_(2016_TV_series)',
    'https://en.wikipedia.org/wiki/Entourage_(American_TV_series)',
    'https://en.wikipedia.org/wiki/Trapped_(Icelandic_TV_series)',
    'https://en.wikipedia.org/wiki/12_Monkeys_(TV_series)',
    'https://en.wikipedia.org/wiki/Limitless_(TV_series)',
    'https://en.wikipedia.org/wiki/The_Honeymooners',
    'https://en.wikipedia.org/wiki/It%27s_Always_Sunny_in_Philadelphia',
    'https://en.wikipedia.org/wiki/Shaun_the_Sheep',
    'https://en.wikipedia.org/wiki/The_Powerpuff_Girls',
    'https://en.wikipedia.org/wiki/Rogue_(TV_series)',
    'https://en.wikipedia.org/wiki/Meet_the_Browns_(TV_series)',
    'https://en.wikipedia.org/wiki/Fired_Up_(TV_series)',
    'https://en.wikipedia.org/wiki/Perception_(TV_series)',
    'https://en.wikipedia.org/wiki/Jersey_Shore_(TV_series)',
    'https://en.wikipedia.org/wiki/The_O.C.',
    'https://en.wikipedia.org/wiki/Unforgettable_(American_TV_series)',
    'https://en.wikipedia.org/wiki/Carlos_(miniseries)',
    'https://en.wikipedia.org/wiki/The_Messengers_(TV_series)',
    'https://en.wikipedia.org/wiki/Scream_(TV_series)',
    'https://en.wikipedia.org/wiki/The_Dead_Zone_(TV_series)',
    'https://en.wikipedia.org/wiki/The_Company_(miniseries)',
    'https://en.wikipedia.org/wiki/Ghost_Hunters_(TV_series)',
    'https://en.wikipedia.org/wiki/Dekalog',
    'https://en.wikipedia.org/wiki/The_Border_(2014_TV_series)',
    'https://en.wikipedia.org/wiki/Spartacus_(TV_series)',
    'https://en.wikipedia.org/wiki/Lovesick_(TV_series)',
    'https://en.wikipedia.org/wiki/Bones_(TV_series)',
    'https://en.wikipedia.org/wiki/The_Bold_and_the_Beautiful',
    'https://en.wikipedia.org/wiki/Star_Wars:_The_Clone_Wars_(2008_TV_series)',
    'https://en.wikipedia.org/wiki/The_Player_(2015_TV_series)',
    'https://en.wikipedia.org/wiki/Preacher_(TV_series)',
    'https://en.wikipedia.org/wiki/Wuthering_Heights_(2009_TV_serial)',
    'https://en.wikipedia.org/wiki/Fargo_(TV_series)',
    'https://en.wikipedia.org/wiki/Nikita_(TV_series)',
    'https://en.wikipedia.org/wiki/Dark_Angel_(American_TV_series)',
    'https://en.wikipedia.org/wiki/Gomorrah_(TV_series)',
    'https://en.wikipedia.org/wiki/War_%26_Peace_(2016_TV_series)',
    'https://en.wikipedia.org/wiki/Veronica_Mars',
    'https://en.wikipedia.org/wiki/Emma_(2009_TV_serial)',
    'https://en.wikipedia.org/wiki/The_Inbetweeners',
    'https://en.wikipedia.org/wiki/Saving_Grace_(TV_series)',
    'https://en.wikipedia.org/wiki/Psych',
    'https://en.wikipedia.org/wiki/Secrets_and_Lies_(American_TV_series)',
    'https://en.wikipedia.org/wiki/Anne_of_Green_Gables_(1985_film)',
    'https://en.wikipedia.org/wiki/Animal_Kingdom_(TV_series)',
    'https://en.wikipedia.org/wiki/Sonny_with_a_Chance',
    'https://en.wikipedia.org/wiki/M*A*S*H_(TV_series)',
    'https://en.wikipedia.org/wiki/Empire_(2015_TV_series)',
    'https://en.wikipedia.org/wiki/The_Secret_(TV_series)',
    'https://en.wikipedia.org/wiki/Robot_Chicken',
    'https://en.wikipedia.org/wiki/Creature_(miniseries)',
    'https://en.wikipedia.org/wiki/BrainDead',
    'https://en.wikipedia.org/wiki/The_Grand_(TV_series)',
    'https://en.wikipedia.org/wiki/In_the_Heat_of_the_Night_(TV_series)',
    'https://en.wikipedia.org/wiki/Strangers_with_Candy',
    'https://en.wikipedia.org/wiki/Get_Real_(American_TV_series)',
    'https://en.wikipedia.org/wiki/Eureka_(2006_TV_series)',
    'https://en.wikipedia.org/wiki/Wings_(1990_TV_series)',
    'https://en.wikipedia.org/wiki/The_Streets_of_San_Francisco',
    'https://en.wikipedia.org/wiki/The_Girlfriend_Experience_(TV_series)',
    'https://en.wikipedia.org/wiki/Wolf_Creek_(TV_series)',
    'https://en.wikipedia.org/wiki/Jesse_(TV_series)',
    'https://en.wikipedia.org/wiki/Heroes_(American_TV_series)',
    'https://en.wikipedia.org/wiki/Home_Movies_(TV_series)',
    'https://en.wikipedia.org/wiki/Revolution_(TV_series)',
    'https://en.wikipedia.org/wiki/Happy_Valley_(TV_series)',
    'https://en.wikipedia.org/wiki/The_Following'
]

movie_data = []

for url in movie_urls:
    director_name = get_director_name(url)
    movie_data.append({'URL': url, 'Director': director_name})

# Convert to pandas DataFrame
df = pd.DataFrame(movie_data)

# Save to Excel file
df.to_excel('directors.xlsx', index=False)

print("Data saved to 'directors.xlsx'")


