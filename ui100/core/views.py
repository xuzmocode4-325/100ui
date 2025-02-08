from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "core/home.html"


class PatmentView(TemplateView):
    template_name = "core/home.html"


class HeroView(TemplateView):
    template_name = "core/hero.html"