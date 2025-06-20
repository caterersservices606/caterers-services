from rest_framework.response import Response
from rest_framework import status, generics
from caterers.Utils.permissions import *
from .serializers import *

# --------------------    EventBookingViewSet    --------------------


class EventBookingViewSet(generics.GenericAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
       return EventBooking.objects.all()

    def post(self, request):
        for slot in request.data.get("time_slots", []):
            selected_items = slot.get("selected_items", {})
            converted_items = {
                key: [{"name": item} for item in value]
                for key, value in selected_items.items()
            }
            slot["selected_items"] = converted_items

            # Calculate extra_service_amount
            amount = sum(int(service.get("amount", 0)) for service in slot.get("extra_service", []))
            slot["extra_service_amount"] = str(amount)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "status": True,
            "message": "EventBooking created successfully",
            "data": serializer.data,
        }, status=status.HTTP_200_OK)

    def get(self, request, pk=None):
        if pk:
            event = get_object_or_404(EventBooking, pk=pk)
            serializer = self.get_serializer(event)
            return Response({
                "status": True,
                "message": "EventBooking retrieved",
                "data": serializer.data,
            }, status=status.HTTP_200_OK)

        queryset = self.get_queryset().filter(status__in=["confirm", "completed"])
        for booking in queryset:
            print(booking.time_slots, "booking")
            for extra in booking.time_slots:
                print(extra)
                extra["extra_service_amount"] = str(
                    sum(int(service.get("amount", 0)) for service in extra.get("extra_service", []))
                )
            booking.save()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": True,
            "message": "EventBooking list",
            "data": serializer.data,
        }, status=status.HTTP_200_OK)


class EventBookingGetViewSet(generics.GenericAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def put(self, request, pk=None):
        try:
            eventbooking = EventBooking.objects.get(pk=pk)
            # Partially update the instance with only provided fields
            serializer = EventSerializer(eventbooking, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {
                        "status": True,
                        "message": "EventBooking updated successfully",
                        "data": serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )
            return Response(
                {
                    "status": False,
                    "message": "Something went wrong",
                    "data": {},
                },
                status=status.HTTP_200_OK,
            )
        except EventBooking.DoesNotExist:
            return Response(
                {
                    "status": False,
                    "message": "EventBooking not found",
                    "data": {},
                },
                status=status.HTTP_200_OK,
            )

    def get(self, request, pk=None):
        try:
            eventbooking = EventBooking.objects.get(pk=pk)
            serializer = EventSerializer(eventbooking)
            return Response(
                {
                    "status": True,
                    "message": "EventBooking retrieved successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except EventBooking.DoesNotExist:
            return Response(
                {
                    "status": False,
                    "message": "EventBooking not found",
                    "data": {},
                },
                status=status.HTTP_200_OK,
            )

    def delete(self, request, pk=None):
        try:
            eventbooking = EventBooking.objects.get(pk=pk)
            eventbooking.delete()
            return Response(
                {
                    "status": True,
                    "message": "EventBooking deleted successfully",
                    "data": {},
                },
                status=status.HTTP_200_OK,
            )
        except EventBooking.DoesNotExist:
            return Response(
                {
                    "status": False,
                    "message": "EventBooking not found",
                    "data": {},
                },
                status=status.HTTP_200_OK,
            )


# --------------------    PendingEventBookingViewSet    --------------------
class PendingEventBookingViewSet(generics.GenericAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get(self, request):
        queryset = EventBooking.objects.all().filter(status="pending")
        serializer = EventSerializer(queryset, many=True)
        return Response(
            {
                "status": True,
                "message": "EventBooking list",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

class GetAllEvent(generics.GenericAPIView):
    def get(self,request):
        queryset = EventBooking.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(
            {
                "status": True,
                "message": "EventBooking list",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )