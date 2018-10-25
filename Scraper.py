from bs4 import BeautifulSoup
import requests, json, time, random


index = "http://web.mta.info/mta/aft/index/"
print("Get URLs!", index)


index_page = requests.get(index)

index_html = index_page.text

# now we are going to ask BS to parse the page
soup = BeautifulSoup(index_html, "html.parser")


artist_name = soup.find_all("h3")
url_container = soup.find_all("p", attrs={'class':'alinks'})

for urls in url_container:

	url = urls.find('a').attrs




	print(artist_name, url)




# json.dump(art_list_nga,open('art_list_nga.json','w'), ensure_ascii=False, indent=2)















