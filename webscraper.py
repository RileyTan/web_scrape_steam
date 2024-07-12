import requests
import lxml.html

html = requests.get('https://store.steampowered.com/explore/new/')
doc = lxml.html.fromstring(html.content) # equivalent of getting soup

new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]


<a href="https://store.steampowered.com/app/1928540/Horticular/?snr=1_239_new__145" class="tab_item   app_impression_tracked" data-ds-appid="1928540" data-ds-itemkey="App_1928540" data-ds-tagids="[1654,597,4726,4305,10235,22602,599]" data-ds-crtrids="[42986487]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:1928540,&quot;params&quot;:{&quot;bDisableHover&quot;:false},&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )">
		<div class="tab_item_cap">
			<img class="tab_item_cap_img" src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1928540/capsule_184x69.jpg?t=1720719091" alt="Horticular">
		</div>
				<div class="discount_block tab_item_discount" data-price-final="1665" data-bundlediscount="0" data-discount="10" role="link" aria-label="10% off. S$18.50 normally, discounted to S$16.65"><div class="discount_pct">-10%</div><div class="discount_prices"><div class="discount_original_price">S$18.50</div><div class="discount_final_price">S$16.65</div></div></div>		<div class="tab_item_content">
			<div class="tab_item_name">Horticular</div>
			<div class="tab_item_details">
				<span class="platform_img win"></span><span class="platform_img linux"></span>				<div class="tab_item_top_tags"><span class="top_tag">Relaxing</span><span class="top_tag">, Casual</span><span class="top_tag">, Cute</span><span class="top_tag">, Colorful</span></div>
			</div>
		</div>
		<div style="clear: both;"></div>
	</a>



