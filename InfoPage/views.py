from django.http import HttpResponse
from django.template import loader
from .models import student_name

# creates a view the user views

def index(request):
    latest_student_added = student_name.objects.order_by('-pub_date')[:5]
    
    template = loader.get_template('InfoPage/index.html')
    context = {
    'latest_student_added':
    latest_student_added,
    }
    return HttpResponse(template.render(context,request))

    
def user_detail(request, user_id):
	response = "This is the page for student # - %s. <br> We can also display the names of students corresponding to the user_id."
	return HttpResponse(response % user_id)
