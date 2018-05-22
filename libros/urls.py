from django.conf.urls import url
from libros.scaffolding import LibroCrudManager # or from views import BookCrudManager depending on where you've put it
book_crud = LibroCrudManager()
from . import views

app_name = 'libros'
urlpatterns = [
    url(r'^'+'$',views.index,name="index")
]



# [...] define your urlpatters here

urlpatterns += book_crud.get_url_patterns()