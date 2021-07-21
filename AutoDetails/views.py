from django.shortcuts import render
from .forms import VehicleForm, EngineForm

def vehicleform(request):
	v_form = VehicleForm(request.POST or None)
	e_form = EngineForm(request.POST or None)
	if v_form.is_valid() and e_form.is_valid():
		v_form.save()
		e_form.save()

	context = {'v_form': v_form, 'e_form': e_form}
	return render(request, "index.html", context)