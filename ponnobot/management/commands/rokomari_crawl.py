from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from ponnobot.spiders.rokomari_spider import RokomariBookSpider


class Command(BaseCommand):
    help = "Release the PenguinBD Crawler"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(RokomariBookSpider)
        process.start()
