from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    us_tx = request.GET['usertext']
    words = us_tx.split()
    number_of = len(words)
    rev_tx = us_tx[::-1]
    return render(request, 'reverse.html', {'usertext':us_tx, 'reveresetx':rev_tx, 'numberwords':number_of})
