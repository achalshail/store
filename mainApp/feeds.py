from django.contrib.syndication.views import Feed
from mainApp.models import Entry
from django.urls import reverse

class LatestEntries(Feed):
    title = "Facebook NewsFeed"
    link = "/entry/"
    description = "The latest facebook posts."

    def items(self):
        return Entry.objects.all()
    
    def item_title(self, item):
        return item.first_description
		
    def item_description(self, item):
        return item.second_description
    
    def item_link(self, item):
        return reverse('entry', kwargs = {'id':item.id})