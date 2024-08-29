from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
from api.models import History

class HistoryMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        # Check if the user is authenticated (optional)
        if request.user.is_authenticated:
            visiter = getattr(request.user, 'sitevisiter', None)
            # Save the history entry
            History.objects.create(
                visiter=visiter,
                action="Page Load",
                url=request.build_absolute_uri(),
                record_id=view_kwargs.get('pk', 0),  # Example of capturing a primary key if present
                description=f"Visited {request.path}",
                timestamp=timezone.now()
            )

