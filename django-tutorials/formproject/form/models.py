from django.db import models

class register(models.Model):
    firstName = models.CharField(max_length=255, null = True)
    lastName = models.CharField(max_length = 255, null = True)
    email = models.EmailField(max_length=255, null = True)
    telephone = models.CharField(max_length=10, null=True)


class hostel(models.Model):
    hostelName = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    manager= models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    rooms = models.IntegerField()

    def __str__(self):
        return self.hostelName


#  from rest_framework import status
#     from rest_framework.decorators import api_view
#     from rest_framework.response import Response

#     @api_view(['GET'])
#     def getStats(request):
#         print('--------STARTING Stats----------')
    
#         # Take some GET variable
#         version = request.GET.get('version')
    
#         # Get some data
#         with open('static/data.json') as f:
#             data = json.load(f)
    
#         # Filter the data
#         if version is not None:
#             data = list(filter(lambda x: x['version'] == version, data))
#             print("FILTERED DATA", len(data))
    
#         # Perform some operations on the data
#         data = calculateStats(data)
    
#         # Return an HTTP response
#         return Response(json.dumps(data, status=status.HTTP_200_OK)

