from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from ponnobot.spiders.startech_spider import StarTechBDSpider


class Command(BaseCommand):
    help = "Release the Startech Crawler"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(StarTechBDSpider)
        process.start()
