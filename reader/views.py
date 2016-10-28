from django.shortcuts import render, get_object_or_404, redirect
from .models import Regions, Document
from .forms import DocumentForm
from django.conf import settings
from .tools.utils import Utils


# Main page with field file upload
def index(request):
    form = DocumentForm()
    return render(request, 'reader/index.html', {'form': form})


# Only parse csv file and add it to DB
def parse(request):
    if request.method == 'POST':
        Utils.clear_media()
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            Utils.put_all_to_db(settings.MEDIA_ROOT + '/' + newdoc.docfile.name)
        return redirect('/diagram')
    return redirect('/index')


# Get all data for build chart
# If first load page, choose all regions and display first
# After choosing from select element display that one
def diagram(request):

    regions = Regions.objects.all()
    if regions.count() == 0:
        return redirect('/index')
    region = regions[0]
    if request.method == 'POST':
        region = get_object_or_404(Regions, pk=request.POST['region_id'])
    context = {
        'region': region,
        'regions': regions
    }
    return render(request, 'reader/diagram.html', context)
