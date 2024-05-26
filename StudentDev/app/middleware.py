# app/middleware.py

from django.shortcuts import redirect

class GlobalErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        # Redirect to the root URL in case of any exceptions
        return redirect('/')
