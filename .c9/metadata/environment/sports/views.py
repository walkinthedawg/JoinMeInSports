{"filter":false,"title":"views.py","tooltip":"/sports/views.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":10,"column":40},"action":"insert","lines":["from django.shortcuts import render","from django.http import HttpResponse","","# Create your views here.","def index(request):","    \"\"\" A view to display the index page \"\"\"","    return render(request, 'index.html')","    ","def about(request):","    \"\"\" A view to display the index page \"\"\"","    return render(request, 'about.html')"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":40},"end":{"row":10,"column":40},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1563657726958,"hash":"d14a65ed12b6ec36a5e8ec39b317eb519dbbeb18"}