from django.contrib.syndication.views import Feed
from django.urls import reverse
from portfolio.models import Product


class LatestEntriesFeed(Feed):
    title = "blog newest"
    link = "light/rss/feed"
    description = "best blog"

    def items(self):
        return Product.objects.filter(status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.info[:100]  + item.more_info[:100]
