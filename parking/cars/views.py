from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.forms.models import model_to_dict


from .models import Car, Slot
from .limit import Limit
from .decorators import rate_limit


@rate_limit
def home(request):
    slots = Slot.objects.all()
    slot_length = slots.count()
    return render(request, 'home.html', {"slots": slots, "slot_length": slot_length})


@rate_limit
def park(request, pk):
    slots = Slot.objects.filter(empty = True)
    if slots.exists():        
        car, created = Car.objects.get_or_create(pk = pk)
        if created:
            slot = slots.first()
            slot.empty = False
            slot.save()
            car.slot = slot
            car.save()
        car_dict = {"slot_number": car.slot.pk}
        return JsonResponse(car_dict)
    return JsonResponse({'status':'false','message':"Sorry, there is no parking slot!"}, status=500)


@rate_limit
def unpark(request, pk):
    slot = get_object_or_404(Slot, pk = pk)
    if not slot.empty:
        slot.empty = True
        slot.car.delete()
        slot.save()
        return JsonResponse({"message": "Now {}. slot is empty.".format(pk)})
    return JsonResponse({"message": "{}. slot is already empty.".format(pk)})

@rate_limit
def parking_info(request, pk):
    slot = get_object_or_404(Slot, pk = pk)
    if slot.empty:
        return JsonResponse({"slot_number": pk, "car_number": "There is no car here!"})
    return JsonResponse({"slot_number": pk, "car_number": slot.car.pk})
    
