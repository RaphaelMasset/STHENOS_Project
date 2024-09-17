from django.db import models
from STHENOS_Index.models import User  # Import User from app1

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="message_author")
    postdate = models.DateTimeField(auto_now_add=True) 
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    isArchived = models.BooleanField(default=False)

    subject = models.CharField(max_length=255, blank=True)
    read = models.BooleanField(default=False)
    recipients = models.ManyToManyField(User, related_name="posts_received", blank=True)
    
    def __str__(self):
        return f"{self.id}- {self.author} Posted: {self.message}"
    
    def serialize(self):

        return {
            "id": self.id,
            "sender": self.author.username,  # Ensure this returns the sender's username
            #"sender_email": self.author.email,  # Optional: Include sender's email if needed
            "recipients": [user.username for user in self.recipients.all()],
            #"recipients_emails": [user.email for user in self.recipients.all()], 
            "subject": self.subject,
            "body": self.message,
            "postdate": self.postdate.isoformat(),
            "read": self.read,
            "isArchived": self.isArchived
        }
    

class Following(models.Model):
    id = models.AutoField(primary_key=True)
    followedId = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="followed")
    followerId = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="follower")
    
    def __str__(self):
        return f"{self.id}: {self.followedId} is followed by {self.followerId}"

class Auctions(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    userName = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="auction_author")
    description = models.CharField(max_length=500)
    sprice = models.IntegerField()
    picture = models.CharField(max_length=500)
    categories = models.CharField(max_length=50)
    #auctionTime = models.DateField()
    def __str__(self):
        return f"{self.Id}: {self.name} - Price: {self.sprice} - Description: {self.description}"

class Comments(models.Model):
    commentId = models.AutoField(primary_key=True)
    auctionId = models.ForeignKey(Auctions, on_delete=models.CASCADE, related_name="Avis") 
    userName = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="comment_author")
    comment = models.CharField(max_length=500)
    commentTime = models.DateField()
    def __str__(self):
        return f"{self.commentId} - Auction: {self.auctionId} by {self.userName}"

class Bids(models.Model):
    bidsId = models.AutoField(primary_key=True)
    auctionId = models.ForeignKey(Auctions, on_delete=models.CASCADE) 
    userName = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="bid_author")
    bid = models.IntegerField()

class Watchlist(models.Model):
    userName = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="waList_author")
    auctionId = models.ForeignKey(Auctions, on_delete=models.CASCADE) 

class Email(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="emails")
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="emails_sent")
    recipients = models.ManyToManyField(User, related_name="emails_received")
    subject = models.CharField(max_length=255)
    
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    isArchived = models.BooleanField(default=False)

    def serialize(self):
        user_profile = User.objects.get(username=self.author)
        localized_timestamp = user_profile.get_localized_timestamp(self.timestamp)
        return {
            "id": self.id,
            "sender": self.author.username,  # Ensure this returns the sender's username
            "sender_email": self.author.email,  # Optional: Include sender's email if needed
            "recipients": [user.username for user in self.recipients.all()],
            "recipients_emails": [user.email for user in self.recipients.all()], 
            "subject": self.subject,
            "body": self.body,
            "timestamp": localized_timestamp.strftime("%b %d %Y, %I:%M %p"),
            "read": self.read,
            "isArchived": self.isArchived
        }
    