from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .models import GroupMember, Chats
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Roadmap, Videos, Books, Course
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .assisstent import ask # Import the function from assistant.py
# from django.http import HttpResponse

@csrf_protect
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Store the username in the session
            request.session['username'] = username
            print(request.session['username'])
            # Redirect to some page
            return redirect('home')
        else:
            # Handle invalid login
            pass
    return render(request, 'login.html')


@login_required
def home(request):
    search_query = request.GET.get('search', '')  # Get the search query from the request
    roadmaps = Roadmap.objects.filter(topic__icontains=search_query)
    videos = Videos.objects.filter(topic__icontains=search_query)
    books = Books.objects.filter(topic__icontains=search_query)
    courses = Course.objects.filter(topic__icontains=search_query)
    return render(request, 'home.html', {'roadmaps': roadmaps, 'videos': videos, 'books': books, 'courses': courses, 'search_query': search_query})

@login_required
def communities_view(request):
    # Get the current user's username from the session
    if request.method == 'POST':
        message = request.POST.get('textmessage')

    
    username = request.session.get('username')

    # Query the database to get all group names associated with the current user
    user_groups = GroupMember.objects.filter(username=username).values_list('groupname', flat=True)

    # Pass the user's group names to the template context
    return render(request, 'community.html', {'user_groups': user_groups})

@login_required
def get_chat_messages(request, groupname):
    # Fetch chat messages for the selected group
    chat_messages = Chats.objects.filter(groupname=groupname).values('username', 'text')
    return JsonResponse(list(chat_messages), safe=False)

@login_required
@require_POST
@csrf_exempt
def send_message(request):
    print("entered")
    if request.method == 'POST':
        message = request.POST.get('message')
        groupname = request.POST.get('groupname')
        print("got post")
        if(groupname):
            Chats.objects.create(groupname=groupname, username=request.user.username, text=message)
        print("sent msg to ast")
        # Generate bot's reply
        bot_reply = ask(message)  # Call the function from assistant.py
        print("got reply")
        # Prepare JSON response with user's message and bot's reply
        response_data = {
            'username': request.user.username,
            'text': message,
            'bot_reply': bot_reply  # Include the bot's reply in the response
        }
        print(bot_reply)
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'})

    
@login_required
def search(request):
    if request.method == 'GET' and 'search' in request.GET:
        search_query = request.GET['search']
        
        # Query the database for relevant data based on the search query
        roadmap_results = Roadmap.objects.filter(topic__icontains=search_query).values('topic', 'link')
        video_results = Videos.objects.filter(topic__icontains=search_query).values('topic', 'embededlink')
        book_results = Books.objects.filter(topic__icontains=search_query).values('topic', 'author', 'link')
        course_results = Course.objects.filter(topic__icontains=search_query).values('topic', 'author', 'link')
        
        # Prepare data to be sent back to the client
        data = {
            'roadmap': list(roadmap_results),
            'videos': list(video_results),
            'books': list(book_results),
            'courses': list(course_results),
        }

        return JsonResponse(data)
    else:
        # Handle invalid or missing search query
        return JsonResponse({'error': 'Invalid search query'})

@login_required 
def trending(request):
    return render(request, 'trending.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('/')  # Redirect to the root URL after logging out


