from django.http import HttpResponse
from .models import student_name

def index(request):
    latest_student_added = student_name.objects.order_by('-pub_date')[:5]
    output = ','.join([s.student_name for s in latest_student_added])
    return HttpResponse(output)
    
def user_detail(request, user_id):
	response = "This is the page for student # - %s. <br> We can also display the names of students corresponding to the user_id."
	return HttpResponse(response % user_id)