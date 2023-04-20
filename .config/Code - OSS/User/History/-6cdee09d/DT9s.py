from django.http import HttpResponse


def welcome(request):
    return HttpResponse('''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>Trombinoscoop</title>
        </head>
        <body>
            <p>Bienvenue sur Trombinoscoop!</p>
        </body>
    </html> 
    ''')