from django.http import HttpResponse

def index(request):
    page = """<h1 style='color:red'>Welcome to my first page</h1>
    <a href=''>HOME</a>
    <a href='app1/'>APP1</a>"""
    return HttpResponse(page)