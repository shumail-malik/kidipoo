from django.shortcuts import render, redirect
from .forms import AddNumbersForm

def add_numbers(request):
    result = None

    if request.method == 'POST':
        form = AddNumbersForm(request.POST)
        if form.is_valid():
            numbers = form.save(commit=False)  # Don't save to the database yet
            result = numbers.num1 + numbers.num2
            return redirect('result/' + str(result))
    else:
        form = AddNumbersForm()
    
    return render(request, 'calculator/add_numbers.html', {'form': form})

def result_page(request, result):
	return render(request, 'calculator/result.html', {'result': result})	
