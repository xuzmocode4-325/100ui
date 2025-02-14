from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "core/home.html"


class PatmentView(TemplateView):
    template_name = "core/home.html"


class HeroView(TemplateView):
    template_name = "core/hero.html"


class CalculatorView(TemplateView):
    template_name = "core/calculator.html"


class ProfileView(TemplateView):
    template_name = "core/profile.html"


class SettingsView(TemplateView):
    template_name = "core/settings.html"


class NotFoundView(TemplateView):
    template_name = "core/404.html"


class MusicView(TemplateView):
    template_name = "core/music-ui.html"

