from django.shortcuts import render, redirect
from django.db.models import Q

from item.models import Category, Item
 
from .forms import SignupForm

from django.contrib import messages
from .forms import ContactForm

from django.contrib.auth import logout
from django.views.decorators.http import require_http_methods

# def logout_view(request):
#     logout(request)
#     messages.success(request, 'You have been successfully logged out.')
#     return redirect('core:index')

@require_http_methods(["GET", "POST"])  # Accept both methods
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('core:index')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            # Save to database
            form.save()
            
            # Success message
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            
            # Optional: Send email notification to admin
            # send_mail(
            #     subject=f"New Contact: {form.cleaned_data['subject']}",
            #     message=form.cleaned_data['message'],
            #     from_email=form.cleaned_data['email'],
            #     recipient_list=['admin@barcautdhub.com'],
            # )
            
            return redirect('core:contact')
        else:
            # Form has errors - will be displayed in template
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})


def search(request):
    query = request.GET.get('q', '')  # Get search query from URL
    items = Item.objects.none()  # Empty queryset initially
    
    if query:
        # Search in item name, description, and category name
        items = Item.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query),
            is_sold=False
        ).distinct()
    
    context = {
        'items': items,
        'query': query,
        'search_count': items.count()
    }
    
    return render(request, 'core/search.html', context)


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    
    # Batch items into groups of 3 for carousel
    batched_items = []
    items_list = list(items)  # Convert queryset to list
    for i in range(0, len(items_list), 3):
        batched_items.append(items_list[i:i+3])
    
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
        'batched_items': batched_items,
    })

def shop(request):
    items = Item.objects.filter(is_sold=False)
    
    # Debug: Print items to console
    for item in items:
        print(f"Item: {item.name}, ID: {item.id}, PK: {item.pk}")
    
    categories = Category.objects.all()
    
    return render(request, 'core/shop.html', {
        'items': items,
        'categories': categories,
    })



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form' : form
    })
       