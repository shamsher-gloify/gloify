from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserInfo
from .serializers import UserInfoSerializers
from gloify.celery import celery
from .tasks import celery_test_async


@api_view(['GET'])
def get_user(request):
    user = UserInfo.objects.all()
    user_ser = UserInfoSerializers(user, many=True)
    return Response(user_ser.data)


@api_view(["POST"])
def create_user(request):
    user_ser = UserInfoSerializers(data=request.data)
    if user_ser.is_valid():
        user_ser.save()
        return Response(user_ser.data, status=201)
    return Response(user_ser.errors, status=400)


@api_view(["PUT"])
def update_user(request, user_id):
    try:
        user = UserInfo.objects.get(pk = user_id)
    except UserInfo.DoesNotExist:
        return Response({'message': 'User Not Found'}, status=404)
    user_ser = UserInfoSerializers(user, data=request.data)
    if user_ser.is_valid():
        user_ser.save()
        return Response(user_ser.data, status=200)
    return Response(user_ser.errors, status=400)

@api_view(["DELETE"])
def delete_user(request, user_id):
    try:
        user = UserInfo.objects.get(pk = user_id)
    except UserInfo.DoesNotExist:
        return Response({'message': 'User Not Found'}, status=404)
    user.delete()
    return Response({'message': 'User deleted successful'})

     
@api_view(['POST'])
def test_celery(request):
    print(request)
    # Use this at the time when you are using microservice and assign task to other queue
    celery.send_task('celery_test', ['shamsher'])
    # User this at the time of using singe queue and calling internal
    celery_test_async.apply_async(['singh'])
    return Response({}, status=200)