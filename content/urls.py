from content.views import gallery

urlpatterns = [
    path('', gallery, name='home'),
]
