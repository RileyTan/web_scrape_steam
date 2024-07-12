import requests
import lxml.html

html = requests.get('https://store.steampowered.com/explore/new/')
doc = lxml.html.fromstring(html.content) # equivalent of getting soup

# get list of divs in the HTML page with 
new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]



