from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    #return HttpResponse("hello world! <html><head><title>hello world</title><style></style> </head>  <body><p>hi this is my first html program in django</p> <table       ><tr><td>name</td><td> age</td>  </tr><tr><td>akanoob</td><td>20</td></tr>     </table>        </body></html>   ")
    return render(request, 'home.html')