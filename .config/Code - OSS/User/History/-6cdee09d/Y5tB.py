from django.http import HttpResponse


def welcome(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html>
        <head>
        </head>
        <body>
            <p>Bienvenue sur Trombinoscoop!</p>
        </body>
    </html> 
    ''')