import os
from time import time

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import DNAOverviewForm


class DNAView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        context = {}
        context["form"] = DNAOverviewForm()
        return render(request, self.template_name, context)

    def post(self, request):
        form = DNAOverviewForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]

            # rename file name via time format
            _, file_extension = os.path.splitext(image._name)
            cleaned_filename = f"{int(time())}{file_extension}"
            relative_path_filename = f"dna/overview/{cleaned_filename}"

            # save file into path
            default_storage.save(
                os.path.join(settings.MEDIA_ROOT, relative_path_filename),
                ContentFile(image.read()),
            )
        return HttpResponseRedirect("/uploads")