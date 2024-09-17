from django.contrib import admin

# Register your models here.

from .models import Post, Following, Auctions, Comments, Bids, Watchlist, Email

# Register your models here.
# Register each model with the Django admin site
admin.site.register(Post)
admin.site.register(Following)
admin.site.register(Auctions)
admin.site.register(Comments)
admin.site.register(Bids)
admin.site.register(Watchlist)
admin.site.register(Email)