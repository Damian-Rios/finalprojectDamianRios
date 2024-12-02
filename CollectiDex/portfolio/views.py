from django.shortcuts import render

# View for the dashboard
def dashboard(request):
    return render(request, 'portfolio/dashboard.html')
