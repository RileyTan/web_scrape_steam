import requests
import lxml.html

html = requests.get('https://store.steampowered.com/explore/new/')
doc = lxml.html.fromstring(html.content) # equivalent of getting soup

# the anchor tag of the game linking us to it's own page is encapsulated in the div with id of tab_newreleases_content. good bcos unique
new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]




