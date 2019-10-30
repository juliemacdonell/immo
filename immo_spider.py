import scrapy



BASE_URL = 'https://www.immobilienscout24.de/Suche/Wohnung-Miete/Umkreissuche'


def create_search_url(search_criterion):
    # simple






class QuotesSpider(scrapy.Spider):
    name = "immoscout"
    start_urls = [
            'https://www.immobilienscout24.de/Suche/S-2/Wohnung-Miete/Umkreissuche/Stuttgart/70569/-64516/2093406/-/-/5/1,50-/-/EURO--850,00',
            'https://www.immobilienscout24.de/Suche/S-2/Wohnung-Miete/Fahrzeitsuche/Stuttgart/70569/-64516/2093406/-/-/30/2,00-/-/EURO--850,00'
            ]
    def parse(self, response):
        for quote in response.css('a.result-list-entry__brand-title-container::attr(href)').extract():
            yield {
                "href": quote
                    }

