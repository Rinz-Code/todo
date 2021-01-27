from django.shortcuts import render,redirect


from .forms import NameForm



def viewtasks(request):
    if "tasks"  not in request.session:
        request.session["tasks"] = []
    template_name = 'base/view.html'
    tasks = request.session["tasks"]
    taskss = enumerate(tasks)
    context = {"tasks": taskss}
    return render(request,template_name,context)

def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            task = form.cleaned_data['task']
            # redirect to a new URL:
            if task:
                request.session["tasks"] += [task]
            return redirect('viewtasks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'base/add.html', {'form': form})
# Create your views here.


