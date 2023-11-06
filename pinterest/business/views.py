from django.shortcuts import render


def main_business_page_view(request):
    return render(request, "business/hub_page.html")
