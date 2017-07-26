__author__ = 'YMH'

# 将model序列化。
from django.contrib.auth.models import User, Group # 这是Django自带的两个model
from rest_framework import serializers
from .models import Snippet


# 使用HyperlinkedModelSerializer来建立超链接关系。（终极大杀器）
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # 当需要为用户添加认证与权限时（以snippets为例，数据结构见model），需要手动添加配置，关联User与snippets
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    # 改进
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)


    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'snippets')  # 定义显示在页面上的字段
#       这里也是一样，需要添加配置字段snippets


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


# class SnippetSerializer(serializers.Serializer):
#     # 定义了序列化/反序列化的字段，这样的话，model类、python数据类型和JSON数据类型可以非常方便的转换。
#     pk = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(default='python')
#     style = serializers.ChoiceField(default='friendly')
#
#     # creat()和update()方法则定义了当我们调用serializer.save()时如何来创建或修改一个实例。
#     # 可以使用ModelSerializer类来节省时间，后续也会介绍，这里先显式的定义serializer。
#     def create(self, validated_data):
#         """
#         如果数据合法就创建并返回一个snippet实例
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         如果数据合法就更新并返回一个存在的snippet实例
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


# ModelSerializer 自动检测字段，简单的定义了create()和update()方法。
# class SnippetSerializer(serializers.ModelSerializer):
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # 这里也可以用CharField(read_only=True)来替代它，指明这是一个只读字段。也就是说，snippets创建之后，owner就不能变了。\

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'owner','title', 'code', 'linenos', 'language', 'style')