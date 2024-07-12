import requests
import lxml.html

html = requests.get('https://store.steampowered.com/explore/new/')
doc = lxml.html.fromstring(html.content) # equivalent of getting soup

# the anchor tag of the game linking us to it's own page is encapsulated in the div with id of tab_newreleases_content. good bcos unique
new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]
# new_releases contain the whole div now, [0] because only one div contains the id of tab_newreleases_content
# // forward slashes tell lxml to "look everywhere in the document" / means to look in the direct children of the current element

titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
# . means that we are only interested in the children tab of new_releases
# filter based on class name instead of id this time
# /text() means we only want the text within the tag

prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')

tags_divs = new_releases.xpath('.//div[@class="tab_item_top_tags"]')
tags = []

for div in tags_divs:
    tags.append(div.text_content()) # a method in the lxml library

tags = [tag.split(', ') for tag in tags]

platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []

for game in platforms_div:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    # if we use prev method of @class="platform_img", we only get the <span> with solely just "platform_img" as class
    # if <span> has additional class, they won't be returned
    # hence we use contains instead
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    total_platforms.append(platforms)





