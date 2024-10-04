from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to the home page!")

def oddfilter(request):
    # Odd/Even logic
    number = request.GET.get('number')  # Get the number from the request
    is_even = None
    even_performance = ""
    odd_performance = ""
    if number:
        number = int(number)
        is_even = number % 2 == 0
        even_performance = "The number is even." if is_even else ""
        odd_performance = "The number is odd." if not is_even else ""
    else:
        number = None

    # Name filtering logic
    start_char = request.GET.get('start_char', '').upper()  # Get the starting character and convert to uppercase
    names = ["Alice", "Amy", "Bob", "Barbie", "Charlie", "Chandru", "David", "Harry", "James", "Aadhi"]  # Example list of names
    filtered_names = [name for name in names if name.startswith(start_char)] if start_char else []

    context = {
        'number': number,
        'is_even': is_even,
        'even_performance': even_performance,
        'odd_performance': odd_performance,
        'filtered_names': filtered_names,
    }
    
    return render(request, 'oddfilter.html', context)