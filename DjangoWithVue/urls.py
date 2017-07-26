"""DjangoWithVue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import routers
from backend import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'snippets', views.SnippetViewSet)
# 因为我们使用了ViewSets，所以我们可以通过使用Router类来自动生成URL配置信息。当然，router需要注册自定义的ViewSet。

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^vue/$', TemplateView.as_view(template_name='index.html')),
    url(r'^backend/', include('backend.urls', namespace='backend')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 添加了默认的登录、登出视图在浏览API时候使用，如果想在浏览API时使用认证功能这是非常有用的。

    # url(r'^snippets/$', views.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),

    # url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)  # 使url配置生效，它可以通过一个简单清晰的方法去获取指定格式的数据。
# 但是需要注意的是，若url对应的view方法中，没有format=None这个参数，就会报错。所以这里暂时不演示了。
# 示例：http://example.com/api/items/4/.json
