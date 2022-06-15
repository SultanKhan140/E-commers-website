import imghdr
from .serializers import*
from django.http import HttpResponse, JsonResponse
from rest_framework .parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, filters
import os
# Create your views here.


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = JSONParser().pares(request)
        serializer = Userserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def check_login(request, email):
    try:
        user = User.objects.filter(email=email)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Userserializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_user(request, id):
    try:
        user = User.objects.filter(id=id)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = Userserializer(user)
        return JsonResponse(serializer.data)


@csrf_exempt
def product_list(request, id):
    if request.method == 'GET':
        product = Product.objects.all().order_by('create_at').reverse()
        serializer = Userserializer(product, many=True)
        return JsonResponse(serializer.data, sefe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Productserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def product_by_id(request, pk):
    try:
        product = User.objects.get(id=id)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Userserializer(product)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JsonResponse().parse(request)
        serializer = ProductImgserializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=201)


@csrf_exempt
def product_seller(request, storeId):
    try:
        product = Product.objects.filter(storeId=storeId)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def productImg_list(request):
    if request.method == 'GET':
        productImgs = ProductImg.objects.all()
        serializer = ProductImgserializer(productImgs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductImgserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def productImg_product_id(request, productId):
    try:
        productImg = Product.objects.filter(productId=productId)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductImgserializer(productImg, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def productImg_by_id(request, id):
    try:
        productImg = ProductImg.objects.filter(id=id)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductImgserializer(productImg)
        return JsonResponse(serializer.data)
    elif request.method == 'DELETE':
        productImg.delete()
        return HttpResponse(status=201)


@csrf_exempt
def product_by_category(request, category):
    try:
        product = ProductImg.objects.filter(category=category)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def cart_list(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Cartserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def cart_by_user_id(request, userId):
    try:
        cart = Cart.objects.filter(userId=userId)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Cartserializer(cart, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JsonResponse().parse(request)
        serializer = Cartserializer(cart, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=201)


@csrf_exempt
def cart_item_list(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CartItemserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def cartItem_by_id(request, pk):
    try:
        cartItem = Cart.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CartItemserializer(cartItem, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JsonResponse().parse(request)
        serializer = CartItemserializer(cartItem, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        cartItem.delete()
        return HttpResponse(status=201)


@csrf_exempt
def cartitem_by_cart_id(request, cartId):
    try:
        cartItem = Cart.objects.filter(cartId=cartId)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CartItemserializer(cartItem, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def cartItem_by_cart_id(request, cartId):
    try:
        cartItem = Cart.objects.filter(cartId=cartId)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CartItemserializer(cartItem, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def cartitem_detect_same_product(request, cartId, productId):
    try:
        cartItem = Cart.objects.filter(
            cartId=cartId).filter(productId=productId)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CartItemserializer(cartItem, many=True)
        return JsonResponse(serializer.data, safe=False)


class search_product(generics.ListAPIView):
    search_feilds = ('title', 'description', 'category')
    filter_backends = (filters.SearchFilter)
    queryset = Product.objects.all()
    serializer_class = Productserializer


@csrf_exempt
def create_store(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Storeserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def get_store(request, userId):
    try:
        store = Store.objects.filter(userId=userId)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Storeserializer(store, many=True)
        return JsonResponse(serializer.data, safe=False)


class upload_file(generics.CreateAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadserializer


def delete_file(request, filename):
    if request.method == "GET":
        ext = filename.split(".")[-1]
        filenamenoExt = filename.replace(f"{ext}", "")
        fileDir = "%s/%s.%s" % ("img", filenamenoExt, ext)
        if os.path.isfile((f'{imghdr}/{filename}')):
            os.remove(fileDir)
            return HttpResponse(f'{filename} delete')
        return HttpResponse("file not found")


def filter_range_price(request, minprice, maxprice):
    try:
        product = Product.objects.filter(price__range=(minprice, maxprice))
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_min_price(request, minprice):
    try:
        product = Product.objects.filter(price__gte=minprice)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_max_price(request, maxprice):
    try:
        product = Product.objects.filter(price__lte=maxprice)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_rating(request, rating):
    try:
        product = Product.objects.filter(rating__gte=rating)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_condition(request, condition):
    try:
        product = Product.objects.filter(condition=condition)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_price_and_rating(request, minprice, maxprice, rating):
    try:
        product = Product.objects.filter(
            price_range=(minprice, maxprice)).filter(rating__gte=rating)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_price_and_condition(request, rating, condition):
    try:
        product = Product.objects.filter(
            rating__gte=rating).filter(condition=condition)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_all(request, minprice, maxprice, rating, condition):
    try:
        product = Product.objects.filter(
            price_range=(minprice, maxprice)).filter(
            rating__gte=rating).filter(condition=condition)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Productserializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_cart_item_by_cart_id(request, cartId):
    try:
        cartItem = CartItem.objects.filter(cartId=cartId).prefetch_related(
            'ProductId').order_by('create_at')
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Productserializer(cartItem, many=True)
        return JsonResponse(serializer.data, safe=False)
