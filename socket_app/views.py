from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def send_event(request):
    if request.method == "POST":
        channel_name = "user_1"
        channel_layer = get_channel_layer()

        # Send the event to the user's channel
        async_to_sync(channel_layer.group_send)(
            channel_name,
            {
                "type": "chat_message",
                "message": {
                    "event_name": 'event_1',
                    "data": 'hello',
                },
            },
        )

        return JsonResponse({"status": "success", "message": "Event sent successfully"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request"})
