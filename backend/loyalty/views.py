from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Coupon, Loyalty
from .serializers import CouponsSerializer, LoyaltySerializer
from rest_framework.decorators import action
from rest_framework import viewsets
import logging
from django.http.response import HttpResponse


Logger = logging.getLogger("main")


class LoyaltyViewSet(viewsets.ModelViewSet):
    queryset = Loyalty.objects.all()
    serializer_class = LoyaltySerializer

    @action(methods=["get"], detail=True)
    def get(self, request, pk=None):
        loyalty = Loyalty.objects.get(pk=pk)
        return Response({"loyalty": loyalty.loyalty})


def login_view(request):
    Logger.info("Получен")
    return HttpResponse("<h1>Hello</h1>")


class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponsSerializer

    @action(methods=["get"], detail=True)
    def get(self, request, pk=None):
        coupon = coupon.objects.get(pk=pk)
        return Response({"coupon": coupon.coupon})


def login_view(request):
    Logger.info("Получен")
    return HttpResponse("<h1>Hello</h1>")
