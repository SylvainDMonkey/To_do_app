from django.shortcuts import get_object_or_404, render, reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo

from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    context = {"todo_items": todo_items}
    return render(request, 'liste/index.html', context)

@csrf_exempt
def add_todo(request):
  current_date = timezone.now()
  content = request.POST["content"]
  created_obj = Todo.objects.create(added_date=current_date, text=content)
  return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
  Todo.objects.get(id=todo_id).delete()
  return HttpResponseRedirect("/")

@csrf_exempt
def detail_todo(request, todo_id):
    todo_items = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'liste/modification.html', {'todo_items': todo_items})

@csrf_exempt
def modify_todo(request, todo_id):
    current_date = timezone.now()
    nouveau_text = request.POST['text']
    current_obj.text = nouveau_text
    current_obj.added_date = current_date
    current_obj.save()
    
    return HttpResponseRedirect("/")



# class ListeListView(ListView):
#     model = Todo
#     template_name = "liste/index.html"
#     context_object_name = 'a_faire'
#     ordering = ['-added_date']
#     paginate_by = 20

# class ListeDetailView(DetailView):
#     model = Todo
#     template_name = "liste/modification.html"
    
# class ListeCreateView(CreateView):
#     model = Todo
#     fields = ['text', 'added_date']
#     template_name = "liste/index.html"
    
#     def form_valid(self, form):
#         return super().form_valid(form)
    
# class ListeUpdateView(UpdateView):
#     model = Todo
#     fields = ['text', 'added_date']
#     template_name = "liste/index.html"
    
    
#     def form_valid(self, form):
#         return super().form_valid(form)
    
# class ListeDeleteView(DeleteView):
#     model = Todo
#     success_url = '/'

# def ajout_liste(request):
    
#     #Récupérer l'objet de la requête
#     a_faire = request.POST.get('text')
    
#     #Récupérer l'objet de la requête et la mettre en BDD
#     nouvelle_tache = Todo.objects.create(text=a_faire, added_date=timezone.now())
#     #print(a_faire)
    
#     return HttpResponseRedirect("/")

# def detail(request, todo_id):
    
#     todo = get_object_or_404(Todo, pk=todo_id)

#     return render(request, 'liste/modification.html', {'todo':todo})
            
    

# def modifier_ajout(request, todo_id):
    
#     modif = get_object_or_404(Todo, pk=todo_id)
#     modif.save()
    
#     return render(request, 'liste/index.html', {'modif':modif})

# def supprimer_ajout(request, todo_id):
    
#     Todo.objects.get(id=todo_id).delete()
    
#     return HttpResponseRedirect("/")
    