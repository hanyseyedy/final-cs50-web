from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing, Comment

def index(request):
    allCategories = Category.objects.all()
    return render(request, "final/index.html", {
        "categories" : allCategories
    })

def listing(request, id):
    listingMore = Listing.objects.get(pk=id)
    isinwatchlist = request.user in listingMore.watchlist.all()
    allComment = Comment.objects.filter(listing=listingMore)
    isOwner = request.user.username == listingMore.owner.username
    return render(request, "final/listing.html", {
        "listing": listingMore,
        "isinwatchlist": isinwatchlist,
        "allcomments": allComment,
        "isowner": isOwner
    })

def addComment(request, id):
    currentUser = request.user
    listingData = Listing.objects.get(pk=id)
    message = request.POST['addComment']
    newComment = Comment(
        author = currentUser,
        listing = listingData,
        message = message
    )
    newComment.save()
    return HttpResponseRedirect(reverse("listing",args=(id, )))

def displayCategory(request):
    if request.method == "POST":
        categoryForm = request.POST['category']
        category = Category.objects.get(categoryName=categoryForm)
        allCategories = Category.objects.all()
        return render(request, "final/index.html", {
            "categories" : allCategories
        })

def createListing(request):
    if request.method == "GET":
        allCategories = Category.objects.all()
        return render(request, "final/createnew.html", {
            "categories" : allCategories
        })
    else:
        title = request.POST["title"]
        description = request.POST["description"]
        imageurl = request.POST["imageurl"]
        price = request.POST["price"]
        category = request.POST["category"]
        curentuser = request.user
        categoryDate = Category.objects.get(categoryName=category)
        bid = Bid(bid=int(price), user=curentuser)
        bid.save()

        newListing = Listing(
            title = title,
            description = description,
            ImageUrl = imageurl,
            price = bid,
            category = categoryDate,
            owner = curentuser
        )
        newListing.save()
        return HttpResponseRedirect(reverse(index))

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
            return render(request, "final/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "final/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
