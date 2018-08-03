import scrapy
from scrapy.crawler import CrawlerProcess
import json
from DatabaseConnection import DataBaseConnection

from siteInfo.ScrapperAgromall import ArgomallSpider
from siteInfo.ScrapperAnson import AnsonSpider
from siteInfo.ScrapperAbenson import AbensonSpider
from siteInfo.ScrapperWidgetcity import WidgetcitySpider
from siteInfo.ScrapperVillman import VillmanSpider
from siteInfo.ScrapperTakatack import TakatackSpider
from siteInfo.ScrapperShopee import ShopeeSpider
from siteInfo.ScrapperSavenearn import SavenearnSpider
from siteInfo.ScrapperPoundit import PounditSpider
from siteInfo.ScrapperOtcer import OtcerSpider
from siteInfo.ScrapperMemoxpress import MemoxpressSpider
from siteInfo.ScrapperLazada import LazadaSpider
from siteInfo.ScrapperKimstore import KimstoreSpider
from siteInfo.ScrapperGoods import GoodsSpider
from siteInfo.ScrapperGalleon import GalleonSpider
from siteInfo.ScrapperExpansys import ExpansysSpider
from siteInfo.ScrapperElnstore import ElnstoreSpider
from siteInfo.ScrapperBigmk import BigmkSpider
from siteInfo.ScrapperBigbenta import BigbentaSpider
from siteInfo.ScrapperAsianic import AsianicSpider
from siteInfo.ScrapperAdobomall import AdobomallSpider

# parse file with links
# with open('links.json') as file:
#     data = json.load(file)
db = DataBaseConnection();
data = db.getUrls();

# initialize empty arrays, which later
abenson = [];
argomall = [];
anson = [];
asianic = [];
bigbenta = [];
bigmk = [];
elnstore = [];
expansys = [];
galleon = [];
goods = [];
kimstore = [];
lazada = [];
memoxpress = [];
poundit = [];
savenearn = [];
takatack = [];
villman = [];
widgetcity = [];
otcer = [];

# sort links to different arrays
for link in data:
    # db.insertUrl(link['link'])
    if str(link['link']).find('abenson') >= 0:
        abenson.append(link['link'])
    elif str(link).find('argomall') >= 0:
        argomall.append(link)
    elif str(link).find('anson') >= 0:
        anson.append(link)
    elif str(link).find('asianic') >= 0:
        asianic.append(link)
    elif str(link).find('bigbenta') >= 0:
        bigbenta.append(link)
    elif str(link).find('bigmk') >= 0:
        bigmk.append(link)
    elif str(link).find('elnstore') >= 0:
        elnstore.append(link)
    elif str(link).find('expansys') >= 0:
        expansys.append(link)
    elif str(link).find('galleon') >= 0:
        galleon.append(link)
    elif str(link).find('goods') >= 0:
        goods.append(link)
    elif str(link).find('kimstore') >= 0:
        kimstore.append(link)
    elif str(link).find('lazada') >= 0:
        lazada.append(link)
    elif str(link).find('memoxpress') >= 0:
        memoxpress.append(link)
    elif str(link).find('poundit') >= 0:
        poundit.append(link)
    elif str(link).find('savenearn') >= 0:
        savenearn.append(link)
    elif str(link).find('takatack') >= 0:
        takatack.append(link)
    elif str(link).find('villman') >= 0:
        villman.append(link)
    elif str(link).find('widgetcity') >= 0:
        widgetcity.append(link)
    elif str(link).find('otcer') >= 0:
        otcer.append(link)

# run spiders and configure them
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(AbensonSpider, start_urls=abenson)
process.crawl(ArgomallSpider, start_urls=argomall)
process.crawl(AnsonSpider, start_urls=anson)
process.crawl(AsianicSpider, start_urls=asianic)
process.crawl(BigbentaSpider, start_urls=bigbenta)
process.crawl(BigmkSpider, start_urls=bigmk)
process.crawl(ElnstoreSpider, start_urls=elnstore)
process.crawl(ExpansysSpider, start_urls=expansys)
process.crawl(GalleonSpider, start_urls=galleon)
process.crawl(GoodsSpider, start_urls=goods)
process.crawl(KimstoreSpider, start_urls=kimstore)
process.crawl(MemoxpressSpider, start_urls=memoxpress)
process.crawl(PounditSpider, start_urls=poundit)
process.crawl(SavenearnSpider, start_urls=savenearn)
process.crawl(TakatackSpider, start_urls=takatack)
process.crawl(VillmanSpider, start_urls=villman)
process.crawl(WidgetcitySpider, start_urls=widgetcity)
process.crawl(LazadaSpider, start_urls=lazada)
process.crawl(OtcerSpider, start_urls=otcer)

process.start()