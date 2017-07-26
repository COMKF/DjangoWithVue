from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, renderers
# 许多常见的操作都封装在了类ViewSets中。使用ViewSets可以保持view代码的简洁以及逻辑的清晰。
from backend.permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer, GroupSerializer
from rest_framework import generics


# ModelViewSet有读和写的功能，ReadOnlyModelViewSet提供了“只读”方法。
class UserViewSet(viewsets.ModelViewSet):
    """
    查看、编辑用户的界面
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    查看、编辑组的界面
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class JSONResponse(HttpResponse):
    """
    用于返回JSON数据.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# 为了能简单的在客户端进行POST操作而使用了csrf_exempt，正常情况下你不应该这么做，REST framework提供了更安全的做法。
# @csrf_exempt
# def snippet_list(request):
#     """
#     展示所有snippets,或创建新的snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():  # SnippetSerializer从父类继承了is_valid方法
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     修改或删除一个snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)


# 使用rest_framework组件来改写上面的views.
# rest_framework提供了2种装饰器来编写视图：基于函数视图的@api_view，基于类视图的APIView。美化了视图。
# 这里先使用@api_view。
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     # responses支持多种返回格式，利用这点我们可以通过在URL中添加格式后缀的方法来获取单一数据类型。
#     """
#     展示或创建snippets.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         # rest_framework提供了一个类型为TemplateResponse的Response对象，它返回类型由数据决定。
#         # 由此，我们不用再进行数据类型转换了，简化了代码。
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         # request.data简化了JSON数据的处理
#         # rest_framework的 request 和 response ，解决了数据类型转换的处理，以后都不需要手动进行类型转换了。
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # rest_framework为每个状态码都提供了更明显的标志，比如status模块中的HTTP_400_BAD_REQUEST。
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     """
#     修改或删除一个snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.views import APIView

# 使用APIView编写（基于类）
# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# 类视图的一大优点就是可以方便的重用代码，目前我们使用了很多相似的代码来进行增删改查操作，
# 这些常见的操作已经被封装在了rest_framework的mixins类中。让我们使用mixins再次修改上面的views.py。
from rest_framework import mixins

# class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# 继续简化
from rest_framework import permissions
#
#
# class SnippetList(generics.ListCreateAPIView):
#     # 这行代码就是权限认证代码，只有认证用户才能创建、修改、删除。未认证用户没有这些权限。
#     # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     # 引入自定义的权限认证。
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     # 新增perform_create方法，获得一个新的字段'owner',值是request中的用户信息。
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     # 这行代码就是权限认证代码，只有认证用户才能创建、修改、删除。未认证用户没有这些权限。
#     # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     # 引入自定义的权限认证。
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# 使用ModelViewSet
from rest_framework.decorators import detail_route


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # 使用detail_route装饰器可创建自定义动作，这个装饰器可以用于任何不符合标准create/update/delete的动作。
    # 使用@detail_route装饰的用户自定义动作默认相应GET请求，如果需要响应POST操作需要指定methods参数。
    # 默认情况下，自定义动作对应的URL取决于它们的函数名，也可以通过给装饰器传递url_path参数来进行修改。
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
