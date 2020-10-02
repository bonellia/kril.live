from django.shortcuts import render
from ipware import get_client_ip
from django.http import HttpResponse
from django.core.files import File
from datetime import datetime

# Create your gbapp views here.

def index(request):
    content = """
    <!DOCTYPE html>
    <head><style> body {  background-color: black; } </style></head>
    <body><center>
    <iframe src="https://open.spotify.com/embed/playlist/1OYUllkJdqecWsseCO1fn4" width="480" height="720" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
    </center></body>
              
              """
    client_ip, is_routable = get_client_ip(request)
    now = datetime.now()
    dt_string = f'{ client_ip } @ { now.strftime("%d/%m/%Y %H:%M:%S") }\n'
    with open('log.txt', 'a') as f:
            myFile = File(f)
            myFile.write(dt_string)
    if client_ip is None:
        # Unable to get the client's IP address
        pass
    elif is_routable:
        pass
    else:
        pass
    return HttpResponse(content)

