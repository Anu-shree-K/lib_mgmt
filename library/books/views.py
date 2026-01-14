# books/views.py
from django.shortcuts import render, redirect
from .models import Member, BookCategory
from .forms import MemberForm, CategoryForm  # create forms.py as explained

def home(request):
    # Counts for dashboard
    total_members = Member.objects.count()
    total_categories = BookCategory.objects.count()
    total_books = 0  # change to Book.objects.count() if Book model exists

    # Example recent activities
    recent_activities = [
        "Member John Doe added",
        "Category Fiction added",
        "Member Jane Smith added"
    ]

    context = {
        'total_members': total_members,
        'total_categories': total_categories,
        'total_books': total_books,
        'recent_activities': recent_activities,
    }

    return render(request, 'books/home.html', context)


def member_list(request):
    members = Member.objects.all()
    form = MemberForm()  # empty form for modal

    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')  # refresh page after adding

    context = {
        'members': members,
        'form': form,
    }
    return render(request, 'books/member_list.html', context)


def category_list(request):
    categories = BookCategory.objects.all()
    form = CategoryForm()  # empty form for modal

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # refresh page after adding

    context = {
        'categories': categories,
        'form': form,
    }
    return render(request, 'books/category_list.html', context)
