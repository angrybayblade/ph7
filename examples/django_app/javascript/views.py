from django.shortcuts import render


def javascript(request):
    return render(
        request=request,
        template_name="javascript",
    )
