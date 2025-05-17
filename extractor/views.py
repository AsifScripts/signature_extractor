# extractor/views.py
from django.shortcuts import render
from .signature_extractor import extract_signatures

def index(request):
    if request.method == 'POST' and request.FILES.get('document'):
        uploaded_file = request.FILES['document']
        
        # Save file temporarily
        import os
        from django.conf import settings
        temp_path = os.path.join(settings.MEDIA_ROOT, 'uploaded_document.png')
        
        with open(temp_path, 'wb+') as dest:
            for chunk in uploaded_file.chunks():
                dest.write(chunk)

        # Run extraction
        result_path = extract_signatures(temp_path)
        
        return render(request, 'extractor/index.html', {'result_image': result_path})
        
    return render(request, 'extractor/index.html')
