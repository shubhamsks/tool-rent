from rest_framework.response import Response
from allauth.account.views import ConfirmEmailView
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from dj_rest_auth.registration.serializers import VerifyEmailSerializer
from rest_framework.permissions import AllowAny
from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSelfOrReadOnly, IsSelf
from .models import User
from .seriailizers import ProfileSerializer
from tools.serializers import ToolSerializer
from transactions.serializers import TransactionSerializer


class VerifyEmailView(APIView, ConfirmEmailView):
    permission_classes = (AllowAny,)
    allowed_methods = ('GET', 'OPTIONS', 'HEAD')

    @staticmethod
    def get_serializer(*args, **kwargs):
        return VerifyEmailSerializer(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        key = kwargs['key']
        data = {
            'key': key
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        return Response({'detail': _('ok'), 'message': _('Confirmed')}, status=status.HTTP_200_OK)


class DetailUpdateProfileView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, IsSelfOrReadOnly)
    queryset = User.objects.all().select_related('wallet')
    lookup_field = 'username'
    serializer_class = ProfileSerializer


class UserTools(ListAPIView):
    serializer_class = ToolSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return user.tool_set.all().prefetch_related('images')


class UserTransactions(ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, IsSelf)

    def get_queryset(self):
        user = self.request.user
        tr = self.request.GET.get('tr')
        if tr == 'b':
            queryset = user.tools_bought.all().select_related('buyer', 'seller')
        else:
            queryset = user.tools_sold.all().select_related('buyer', 'seller')
        return queryset
