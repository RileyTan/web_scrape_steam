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

# <span class="platform_img win"></span>
# <span class="platform_img linux"></span>
# platforms_div has children in the form of <span> which don't contain text.
# instead we need to extract the platforms embedded within the class
for game in platforms_div:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    # if we use prev method of @class="platform_img", we only get the <span> with solely just "platform_img" as class
    # if <span> has additional class, they won't be returned
    # hence we use contains instead
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    # .get() method lets us extract the attributes of any tag which returns a string like "platform_img linux"
    # we split the string based on the whitespace
    # the last element in a list that is returned after split has an index of -1
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    # hmd_separator is not a platform, just a vertical separator bar
    # <span class="platform_img group_separator"></span>
    total_platforms.append(platforms)

# turn this into a JSON reponse, so that we can easily turn this into a web-based API/use in some other project
output = []
for info in zip(titles, prices, tags, total_platforms):
    resp = {}
    resp['title'] = info[0]
    resp['prices'] = info[1]
    resp['tags'] = info[2]
    resp['total_platforms'] = info[3]
    output.append(resp)

print(output)


