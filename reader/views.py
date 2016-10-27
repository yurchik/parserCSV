from django.shortcuts import render
from .models import Regions, Document
from .forms import DocumentForm
from django.conf import settings
from .tools.utils import Utils


def parse(request):
    if request.method == 'POST':
        Utils.clear_media()
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            region = Utils.put_all_to_db(settings.MEDIA_ROOT + '/' + newdoc.docfile.name)
            regions = Regions.objects.all()
            context = {
                'region': region,
                'regions': regions
            }
            return render(request, 'reader/diagram.html', context)
    else:
        form = DocumentForm()
    return render(request, 'reader/index.html', {'form': form})


def diagram(request):
    if request.method == 'POST':
        region = Regions.objects.get(pk=request.POST['region_id'])
        regions = Regions.objects.all()
        context = {
            'region': region,
            'regions': regions
        }
        return render(request, 'reader/diagram.html', context)
    else:
        form = DocumentForm()
    return render(request, 'reader/index.html', {'form': form})