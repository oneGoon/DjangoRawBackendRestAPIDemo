from django.http import JsonResponse
from django.views import View

class Book(View):
	def get(self,request):
		return JsonResponse('get ok', safe=False)
	def post(self,request):
		return JsonResponse('post ok', safe=False)
		