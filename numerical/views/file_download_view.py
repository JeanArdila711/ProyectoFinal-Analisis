import os
from django.http import FileResponse, Http404
from django.views import View
from django.conf import settings


class FileDownloadView(View):

    def get(self, request, *args, **kwargs):
        filename = kwargs.get('filename')
        
        if not filename:
            raise Http404("Archivo no especificado")
        
        # Buscar en diferentes ubicaciones posibles
        possible_paths = [
            os.path.join(settings.BASE_DIR, "static", "reports", filename),
            os.path.join(settings.BASE_DIR, "static", "img", "numerical_method", filename),
        ]
        
        # Si hay STATICFILES_DIRS configurado, también buscar ahí
        if hasattr(settings, 'STATICFILES_DIRS') and settings.STATICFILES_DIRS:
            for static_dir in settings.STATICFILES_DIRS:
                possible_paths.append(os.path.join(static_dir, "reports", filename))
        
        file_path = None
        for path in possible_paths:
            if os.path.exists(path):
                file_path = path
                break
        
        if not file_path or not os.path.exists(file_path):
            raise Http404(f"Archivo {filename} no encontrado")
        
        # Determinar el tipo de contenido basado en la extensión
        content_type = "application/pdf" if filename.endswith('.pdf') else "application/octet-stream"
        
        try:
            response = FileResponse(open(file_path, "rb"), content_type=content_type)
            response["Content-Disposition"] = f'attachment; filename="{filename}"'
            return response
        except Exception as e:
            raise Http404(f"Error al leer el archivo: {str(e)}")
