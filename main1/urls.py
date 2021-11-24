from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),

    # authorization
    path('sauth', views.site_authorization),
    path('slogout', views.site_logout),

    # cart operations
    path('cart', views.cart_show),
    path('cartadd/<goodId>', views.cart_add),
    path('cartdelete/<goodId>', views.cart_delete),
    path('cartclear', views.cart_clear),
    path('makeorder', views.make_order),

    # goods view
    path('<gType>/<gCat>/<goodId>', views.show_good),
    path('<gType>/<gCat>/', views.index),
    path('<gType>', views.index),
]