from django.http import HttpResponse
from django.shortcuts import render
import json
from django import forms

from .models import User, Post, Following
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def network(request):
    print('network')
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            if len(data.get('message', '')) > 1000:
                return JsonResponse({"error": "Too many characters"}, status=403)
            new_post = Post(message=data['message'], author=request.user)
            new_post.save()
            return JsonResponse({"success": True}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    posts = Post.objects.filter(recipients=None)
    posts = posts.order_by("-postdate").all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'current_page': 'network',
               'current_forum_page': 'allposts',
                "page_obj": page_obj,
                }
    
    return render (request,"network.html", context)

@csrf_exempt
def profile_view(request, username):
    # Get the profile owner (the user whose profile is being viewed)
    post_author = get_object_or_404(User, username=username)

     # Fetch posts and followers/following counts
    posts = Post.objects.filter(author=post_author).order_by("-postdate")
    follower = Following.objects.filter(followedId=post_author).count()
    follows = Following.objects.filter(followerId=post_author).count()

    if request.user != username:
        is_following = Following.objects.filter(followerId=request.user, followedId=get_object_or_404(User, username=username) ).exists()

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if request.method == 'POST' and request.user.username == post_author.username:
        postedform = UserCharacForm(request.POST)
        if postedform.is_valid():
            # Process the data in form.cleaned_data
            bench_press_max = postedform.cleaned_data['bench_press_max']
            squat_max = postedform.cleaned_data['squat_max']
            deadlift_max = postedform.cleaned_data['deadlift_max']
            age = postedform.cleaned_data['age']
            height = postedform.cleaned_data['height']
            weight = postedform.cleaned_data['weight']
            wristC = postedform.cleaned_data['wristC']
            ankleC = postedform.cleaned_data['ankleC']
            bodyFat = postedform.cleaned_data['bodyFat']
            pseudonyme = postedform.cleaned_data['pseudonyme']
            
            user = request.user
            user.benchMax = bench_press_max
            user.squatMax = squat_max
            user.deadLiftMax = deadlift_max
            user.age = age
            user.height = height
            user.weight = weight
            user.wristC = wristC
            user.ankleC = ankleC
            user.bodyFat = bodyFat
            user.username = pseudonyme

            # Save the updated user object to the database
            user.save()

    initial_data = {
            'bench_press_max': request.user.benchMax,
            'squat_max': request.user.squatMax,
            'deadlift_max': request.user.deadLiftMax,
            'age': request.user.age,
            'height': request.user.height,
            'weight': request.user.weight,
            'wristC': request.user.wristC,
            'ankleC': request.user.ankleC,
            'bodyFat': request.user.bodyFat,
            'pseudonyme': request.user.username,
        }
    form = UserCharacForm(initial=initial_data)

    # Pagination for posts
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "profile.html",{
        "already_following": is_following,
        "clicked_username": username,
        "page_obj": page_obj,
        "follower": follower,
        "follows": follows,
        'form': form
        })

class UserCharacForm(forms.Form):
      error_messages={
            'required': 'This field is mandatory.',
            'min_value': 'Enter a value greater than or equal to 0.',
            'max_value': 'Enter a value less than or equal to 500.',
      }
      bench_press_max = forms.IntegerField(label="Bench Press Max (kg)",initial=100,min_value=0,max_value=500,error_messages=error_messages)
      squat_max = forms.IntegerField(label="Squat Max (kg)",initial=100, min_value=0,max_value=500)
      deadlift_max = forms.IntegerField(label="Deadlift Max (kg)",initial=100, min_value=0,max_value=500)
      age = forms.IntegerField(label="Age",initial=30, min_value=0,max_value=120)
      height = forms.IntegerField(label="Height (cm)",initial=175, min_value=55,max_value=200)
      weight = forms.IntegerField(label="Weight (kg)",initial=0,min_value=0,max_value=100)
      wristC = forms.IntegerField(label="wrist (cm)",initial=0,min_value=0,max_value=60)
      ankleC = forms.IntegerField(label="ankle (cm)",initial=0,min_value=0,max_value=60)
      bodyFat = forms.IntegerField(label="bodyfat (%)",initial=0,min_value=0,max_value=60)
      pseudonyme = forms.CharField(required = True, initial="me", label="Pseudonyme of the user")

@login_required
def like(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    data = json.loads(request.body) 
    post_id = int(data.get('post_id'))
  
    post = get_object_or_404(Post, id=post_id) 

    user = request.user

    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)

    post.save()

    return JsonResponse({
            "likes": post.likes.count()
        })

@login_required
def following(request): 
    user = request.user
    listOfFollows = Following.objects.filter(followerId=user).values_list('followedId', flat=True)
    posts = Post.objects.filter(author__in=listOfFollows)
    posts = posts.order_by("-postdate")

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'current_page': 'network',
               'current_forum_page': 'following',
                "page_obj": page_obj
                }
    
    return render (request,"network.html", context)


@login_required
def follow(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    target_follow = json.loads(request.body)

    concerned_user = get_object_or_404(User, username=target_follow) 

    user = request.user

    following_relationship = Following.objects.filter(followerId=user, followedId=concerned_user).first()
    if following_relationship:
        following_relationship.delete()
        followstatus = "unfollow"
    else:
        Following.objects.create(followerId=user, followedId=concerned_user)
        followstatus = "follow"

    nbfollowers = Following.objects.filter(followedId=concerned_user).count()

    print(target_follow,nbfollowers)

    return JsonResponse({
            "nbfollowers": nbfollowers,
            "followstatus": followstatus
        })

@login_required
def edit(request):
    # Composing a new post must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    data = json.loads(request.body)
    post_id = int(data.get("postId"))
    new_text = data.get("newText")

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    if post.author != request.user:
        return JsonResponse({"error": "You can't edit someone else's post."}, status=403)
    
    post.message = new_text
    post.save()
    return JsonResponse({
            "newtext": post.message
        })

@login_required
def archive(request):
    # Composing a new post must be via POST
    if request.method == "POST":
        data = json.loads(request.body)

        post_id = int(data.get("postId"))
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post not found."}, status=404)
        post.isArchived = not post.isArchived
        post.save()

        return JsonResponse({
                "isArchived": post.isArchived
            })
        
    else : 
        posts = Post.objects.filter(isArchived=True)
        posts = posts.order_by("-postdate").all()
        
        # Paginate the combined list
        paginator = Paginator(posts, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'current_page': 'network',
                    'current_forum_page': 'archive',
                    "page_obj": page_obj,
                    }
        
        return render (request,"network.html", context)

@login_required
def mailbox(request, mailbox):

    # Filter emails returned based on mailbox
    if mailbox == "inbox":
        posts = Post.objects.filter(
            recipients=request.user, isArchived=False
        )
    elif mailbox == "sent":
        posts = Post.objects.filter(
            author=request.user
        )
    elif mailbox == "archive":
        posts = Post.objects.filter(
            recipients=request.user, isArchived=True
        )
    else:
        return JsonResponse({"error": "Invalid mailbox."}, status=400)
    
    
    # Return emails in reverse chronologial order
    posts = posts.order_by("-postdate")
    return JsonResponse([post.serialize() for post in posts], safe=False)


@csrf_exempt
@login_required
def compose(request):
    print('compose')
    # Composing a new email must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    # Check recipient emails
    data = json.loads(request.body)
    emails = [email.strip() for email in data.get("recipients").split(",")]
    if emails == [""]:
        return JsonResponse({
            "error": "At least one recipient required."
        }, status=400)

    # Convert email addresses to users
    recipients = []
    for email in emails:
        try:
            user = User.objects.get(Q(email=email) | Q(username=email))
            recipients.append(user)
        except User.DoesNotExist:
            return JsonResponse({
                "error": f"User with email {email} does not exist."
            }, status=400)

    # Get contents of email
    subject = data.get("subject", "")
    body = data.get("body", "")

    post = Post(
        author=request.user,
        subject=subject,
        message=body,
        read=user == request.user
    )
    post.save()
    for recipient in recipients:
        post.recipients.add(recipient)
    post.save()

    return JsonResponse({"message": "Message sent successfully."}, status=201)



#The following code is for futur devlopment, unused right now
'''
@csrf_exempt
@login_required
def post(request):
    # Composing a new post must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    # Parse the JSON data
    data = json.loads(request.body)
    
    if len(data) > 300:
        return JsonResponse({"error": "Too many characters"}, status=403)
    
    # Create and save the new post
    new_post = Post(message=data, author=request.user)
    new_post.save()
    print(data,"written by:",request.user)
    
    return redirect('index')

@csrf_exempt
@login_required
def edit(request):
    # Composing a new post must be via POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    data = json.loads(request.body)
    post_id = int(data.get("postId", 'error'))
    new_text = data.get("newText", "error")

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    if post.author != request.user:
        return JsonResponse({"error": "You can't edit someone else's post."}, status=403)
    
    post.message = new_text
    post.save()
    return JsonResponse({
            "newtext": post.message
        })



@csrf_exempt
@login_required
def follow(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    target_follow = json.loads(request.body)

    concerned_user = get_object_or_404(User, username=target_follow) 

    user = request.user

    following_relationship = Following.objects.filter(followerId=user, followedId=concerned_user).first()
    if following_relationship:
        following_relationship.delete()
    else:
        Following.objects.create(followerId=user, followedId=concerned_user)

    nbfollowers = Following.objects.filter(followedId=concerned_user).count()

    return JsonResponse({
            "nbfollowers": nbfollowers
        })




def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
'''