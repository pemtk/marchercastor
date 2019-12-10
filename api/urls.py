from django.conf.urls import url


from .views import CategoryView, ProductsView

urlpatterns = [
    url(r'^categories/(?P<pk>\d+)/$', CategoryView.as_view(), name='post-categories'),
    url(r'^products/(?P<pk>\d+)/$', ProductsView.as_view(), name='post-products'),
] 
