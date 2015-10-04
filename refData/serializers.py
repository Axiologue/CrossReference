from rest_framework import serializers

from refData.models import Article, Tag, Product, EthicsCategory, EthicsSubCategory, Company, TagType

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title','url','notes','added_by')

class TagTypeSerializer(serializers.ModelSerializer):
    subcategory = serializers.StringRelatedField()

    class Meta:
        model = TagType
        fields = ('name','subcategory','id')

class TagTypeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagType
        fields = ('name','subcategory','id')

class TagSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    tag_type = TagTypeSerializer()

    class Meta:
        model = Tag
        fields = ('tag_type','value','excerpt','company','product','id','added_by')

class TagChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag_type','value','excerpt','company','product','article','id','added_by')

class TagsByArticle(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = ('title','url','tags','id','notes','added_by')

class ProductSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('company','name','division','category','price')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name','id')

class EthicsSubSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tag_types = TagTypeSerializer(read_only=True,many=True)

    class Meta:
        model = EthicsSubCategory
        fields = ('name','id','category','tag_types')
