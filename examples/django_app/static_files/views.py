from django.shortcuts import render


def static_files(request):
    return render(
        request=request,
        template_name="static_files",
    )
