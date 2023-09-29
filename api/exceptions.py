# exceptions.py

from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    # Call the default DRF exception handler
    response = exception_handler(exc, context)

    # Customize the response if needed, e.g., format errors as JSON
    if response is not None:
        response.data = {
            'error': response.data
        }
        # You can further customize the response here

    return response
