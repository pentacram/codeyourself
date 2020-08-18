from django.urls import path
from .views import *
from rest_framework.schemas import get_schema_view
#from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt import views as jwt_views


schema_view = get_swagger_view(title="Swagger Docs")


app_name = 'account'

urlpatterns = [
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('docs', schema_view),
    path('register', CreateUserView.as_view(), name='register'),
]