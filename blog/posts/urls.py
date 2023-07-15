from rest_framework.routers import SimpleRouter
from .views import PostViewSet, UserViewSet
from django.urls import path

# Routers work directly with viewsets to automatically generate URL patterns for us.
router = SimpleRouter()
router.register("", PostViewSet, basename="posts"),
router.register("users", UserViewSet, basename="users"),

urlpatterns = router.urls


# from django.urls import path
# from .views import PostList, PostDetail, UserDetail, UserList
# urlpatterns = [
#     path("users/", UserList.as_view()),
#     path("users/<int:pk>", UserDetail.as_view()),
#     path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
#     path("", PostList.as_view(), name="post_list"),
# ]
