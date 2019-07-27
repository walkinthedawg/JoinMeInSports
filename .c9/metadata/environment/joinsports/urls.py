{"filter":false,"title":"urls.py","tooltip":"/joinsports/urls.py","undoManager":{"mark":31,"position":31,"stack":[[{"start":{"row":21,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":22,"column":0},"end":{"row":23,"column":0},"action":"insert","lines":["",""]},{"start":{"row":23,"column":0},"end":{"row":24,"column":0},"action":"insert","lines":["",""]},{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["",""]},{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["",""]},{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":27,"column":0},"end":{"row":51,"column":1},"action":"insert","lines":["\"\"\"joinsports URL Configuration","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url, include","from django.contrib import admin","from sports import views","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^sports/', include('sports.urls')),","    url(r'^', include('sports.urls')),","    url(r'^index', include('sports.urls')),","    url(r'^about', include('sports.urls')),","]"],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":20,"column":1},"action":"remove","lines":["\"\"\"joinsports URL Configuration","","The `urlpatterns` list routes URLs to views. For more information please see:","    https://docs.djangoproject.com/en/1.11/topics/http/urls/","Examples:","Function views","    1. Add an import:  from my_app import views","    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')","Class-based views","    1. Add an import:  from other_app.views import Home","    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')","Including another URLconf","    1. Import the include() function: from django.conf.urls import url, include","    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))","\"\"\"","from django.conf.urls import url","from django.contrib import admin","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","]"],"id":4}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":5},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":24},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":32},"action":"insert","lines":["from .settings import MEDIA_ROOT"],"id":7}],[{"start":{"row":25,"column":1},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["",""]},{"start":{"row":27,"column":0},"end":{"row":28,"column":0},"action":"insert","lines":["",""]},{"start":{"row":28,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":29,"column":0},"end":{"row":40,"column":1},"action":"insert","lines":["from django.conf.urls import url, include","from django.contrib import admin","from django.views.generic import RedirectView","from django.views.static import serve","from .settings import MEDIA_ROOT","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', RedirectView.as_view(url='posts/')),","    url(r'^posts/', include('posts.urls')),","    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})","]"],"id":9}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":41},"action":"remove","lines":["from django.conf.urls import url, include"],"id":10}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":32},"action":"remove","lines":["from django.contrib import admin"],"id":11}],[{"start":{"row":31,"column":0},"end":{"row":32,"column":37},"action":"remove","lines":["from django.views.generic import RedirectView","from django.views.static import serve"],"id":12}],[{"start":{"row":16,"column":24},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":13}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":37},"action":"insert","lines":["from django.views.generic import RedirectView","from django.views.static import serve"],"id":14}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":32},"action":"remove","lines":["from .settings import MEDIA_ROOT"],"id":15}],[{"start":{"row":26,"column":43},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":27,"column":4},"end":{"row":30,"column":1},"action":"insert","lines":["url(r'^$', RedirectView.as_view(url='posts/')),","    url(r'^posts/', include('posts.urls')),","    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})","]"],"id":17}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":["]"],"id":18},{"start":{"row":29,"column":70},"end":{"row":30,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":27,"column":41},"end":{"row":27,"column":44},"action":"remove","lines":["pos"],"id":19},{"start":{"row":27,"column":41},"end":{"row":27,"column":42},"action":"insert","lines":["s"]},{"start":{"row":27,"column":42},"end":{"row":27,"column":43},"action":"insert","lines":["p"]},{"start":{"row":27,"column":43},"end":{"row":27,"column":44},"action":"insert","lines":["o"]},{"start":{"row":27,"column":44},"end":{"row":27,"column":45},"action":"insert","lines":["r"]}],[{"start":{"row":28,"column":3},"end":{"row":28,"column":43},"action":"remove","lines":[" url(r'^posts/', include('posts.urls')),"],"id":20},{"start":{"row":28,"column":2},"end":{"row":28,"column":3},"action":"remove","lines":[" "]},{"start":{"row":28,"column":1},"end":{"row":28,"column":2},"action":"remove","lines":[" "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"remove","lines":[" "]},{"start":{"row":27,"column":52},"end":{"row":28,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":34,"column":0},"end":{"row":41,"column":43},"action":"remove","lines":["","","","","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', RedirectView.as_view(url='posts/')),","    url(r'^posts/', include('posts.urls')),"],"id":21}],[{"start":{"row":34,"column":0},"end":{"row":35,"column":7},"action":"remove","lines":["","    url"],"id":22}],[{"start":{"row":33,"column":0},"end":{"row":35,"column":1},"action":"remove","lines":["","(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})","]"],"id":23},{"start":{"row":32,"column":0},"end":{"row":33,"column":0},"action":"remove","lines":["",""]},{"start":{"row":31,"column":0},"end":{"row":32,"column":0},"action":"remove","lines":["",""]},{"start":{"row":30,"column":0},"end":{"row":31,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":29,"column":1},"end":{"row":30,"column":0},"action":"remove","lines":["",""],"id":24}],[{"start":{"row":18,"column":37},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":25},{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"insert","lines":["f"]}],[{"start":{"row":19,"column":1},"end":{"row":19,"column":2},"action":"insert","lines":["r"],"id":26},{"start":{"row":19,"column":2},"end":{"row":19,"column":3},"action":"insert","lines":["o"]},{"start":{"row":19,"column":3},"end":{"row":19,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":[" "],"id":27},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["d"]},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["j"]},{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":["a"]},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":["n"]}],[{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["g"],"id":28},{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":["o"]},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["."]},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["v"]}],[{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":["i"],"id":29},{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["e"]},{"start":{"row":19,"column":15},"end":{"row":19,"column":16},"action":"insert","lines":["w"]},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"insert","lines":[" "],"id":30},{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":["i"]},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"insert","lines":["m"]},{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":["p"]}],[{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"insert","lines":["o"],"id":31},{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"insert","lines":["r"]},{"start":{"row":19,"column":23},"end":{"row":19,"column":24},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"insert","lines":[" "],"id":32},{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"insert","lines":["s"]},{"start":{"row":19,"column":26},"end":{"row":19,"column":27},"action":"insert","lines":["t"]},{"start":{"row":19,"column":27},"end":{"row":19,"column":28},"action":"insert","lines":["a"]},{"start":{"row":19,"column":28},"end":{"row":19,"column":29},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":29},"end":{"row":19,"column":30},"action":"insert","lines":["i"],"id":33},{"start":{"row":19,"column":30},"end":{"row":19,"column":31},"action":"insert","lines":["c"]}]]},"ace":{"folds":[],"scrolltop":38,"scrollleft":0,"selection":{"start":{"row":16,"column":24},"end":{"row":16,"column":24},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1564183458431,"hash":"77fe8847bffe6b3ac8e2fcb6ac497d35f3820269"}