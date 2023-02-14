from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,DestroyAPIView,RetrieveUpdateAPIView
from .models import MenuTable,BookingTable
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import MenuTableSerializer,BookingTableSerializer,UserSerializer
from rest_framework.permissions import IsAdminUser,IsAuthenticated

def index(request):
    return render(request,'index.html')
class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuTable.objects.all()
    serializer_class = MenuTableSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuTable.objects.all()
    serializer_class = MenuTableSerializer

class BookingViewset(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BookingTable.objects.all()
    serializer_class = BookingTableSerializer

class BookingViewsetrud(RetrieveUpdateAPIView):
    queryset = BookingTable.objects.all()
    serializer_class = BookingTableSerializer
        

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 