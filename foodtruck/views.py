from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView

from .models import Truck
from .forms import TruckForm

# Create your views here.
class TruckListView(ListView):
    model = Truck
    context_object_name = 'truck_list'
    template_name = 'truck_lists.html'
    # form = TruckForm

    def get_context_data(self, **kwargs):
        context = super(TruckListView, self).get_context_data(**kwargs)
        # import pdb ; pdb.set_trace()
        # context['form'] = TruckForm()
        return context

class CreateTruckView(CreateView):
    model = Truck
    form_class = TruckForm
    template_name = 'truck_create.html'
    success_url = '/truck/list/'
    # initial= {'user': self.request.user.id}

    def get_initial(self):
        return {'user': self.request.user.id}

    def get_context_data(self, **kwargs):
        import pdb ; pdb.set_trace()
        context = super(CreateTruckView, self).get_context_data(**kwargs)
        # context['form']['user'] = self.get_initial()
        return context

    def form_valid(self, form, **kwargs):
        import pdb ; pdb.set_trace()
        # form.data['user'] = self.get_initial()
        return super(CreateTruckView, self).form_valid(form, **kwargs)

class TruckformView(View):
    form_class = TruckForm
    # initial: {'user': request.user}

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return form

    def post(self, request, *args, **kwargs):
        return form


class TruckFormView(FormView):
    template_name = 'contact.html'
    form_class = TruckForm
    success_url = '/thanks/'

    def form_valid(self, form, pk=None):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        if pk:
            instance
        return super(ContactView, self).form_valid(form)


def getLists(TruckListView):
    obj = Truck.objects.all()
    # import pdb ; pdb.set_trace()
    columns = ['SrNo', 'name', 'website', 'user', 'contact_no', 'emails']
    forms = TruckForm()
    # objSeralizer = FoodTruckSerializers(obj)
    return render(
        request,
        'truck_lists.html',
        {
            'columns': columns,
            'list': obj,
            'form': forms
        }
    )

@login_required(login_url='/accounts/login/')
def create(request):
    if request.method == 'POST':
        # import pdb ; pdb.set_trace()
        form = TruckForm(request.POST)
        if form.is_valid():
            truck = form.save(commit=False)
            truck.user = request.user
            truck.save()
        return redirect('/truck/trucklist/')
    else:
        return Http404("Sorry Bad Request.")

@login_required()
def update(request, pk):
    if request.method == 'POST':
        truck = Truck.objects.get(id=pk)
        if request.user == truck.user:
            form = TruckForm(request.POST)
            if form.is_valid():
                truck = form.save(commit=False)
    return None