from django.http import HttpResponse


def firsturl(request):
    return HttpResponse ('oh my goodness!!!')

def secondurl(request):
    return HttpResponse ('bam bam bam!!')

# Create your views here.
