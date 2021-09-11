from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import mixins, viewsets
from .permissions import IsAdminUserOrReadOnly
from reviews.models import User, Category, Genre, Title
from .serializers import GetTokenSerializer, SignupSerializer, CategorySerializer, GenreSerializer, TitleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    lookup_field = 'slug'


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (IsAdminUserOrReadOnly,)



class CreateModelViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    pass


class SignupViewSet(CreateModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignupSerializer


class APIGetToken(APIView):
    def post(self, request):
        serializer = GetTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        try:
            user = User.objects.get(username=data['username'])
        except:
            return Response({'username': 'User not found'},
                            status=status.HTTP_404_NOT_FOUND)
        if data.get('confirmation_code') == user.confirmation_code:
            token = RefreshToken.for_user(user).access_token
            return Response({'token': str(token)}, status=status.HTTP_201_CREATED)
        return Response({'confirmation_code': 'Wrong confirmation code!'},
                        status=status.HTTP_400_BAD_REQUEST)
