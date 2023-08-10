from django.shortcuts import render
from django.db.utils import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models
# Create your views here.
@api_view(['GET'])
def wishlist(request,emailid:str):
    #base/insta/email
    try:
        a=models.WishList.objects.all()
        b=models.WishList(email_id=emailid).save()
        return Response({
            'detail':'Information saved'
        },status=status.HTTP_201_CREATED)
    except IntegrityError:  #"UNIQUE constraint failed: api_wishlist.email_id":
        return Response({
            'Exception':'Not Unique'
        },status=status.HTTP_406_NOT_ACCEPTABLE)
    except Exception as e:
        return Response({
            'Exception':str(e),
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
