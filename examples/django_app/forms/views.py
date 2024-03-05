from django.shortcuts import render


def forms(request):
    return render(
        request=request,
        template_name="forms",
    )
