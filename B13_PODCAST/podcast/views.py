from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files.storage import default_storage
from .models import Episode, Podcast

@csrf_exempt
def upload_audio(request):
    if request.method == 'POST':
        uploaded_files = []
        
        for file in request.FILES.getlist('files'):
            # Save to Supabase storage
            file_path = f"episodes/{file.name}"
            saved_path = default_storage.save(file_path, file)
            
            # Create episode record
            episode = Episode.objects.create(
                title=file.name.split('.')[0],
                audio_file=file_path,
                duration=0,  # You'll calculate this later
                podcast=Podcast.objects.first()  # Assign to first podcast for demo
            )
            
            uploaded_files.append({
                'name': file.name,
                'url': default_storage.url(saved_path)
            })
        
        return JsonResponse({'success': True, 'files': uploaded_files})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)