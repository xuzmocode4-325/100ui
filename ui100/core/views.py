from django.views.generic import TemplateView

streetwear_essentials = [
    'caps', 'oversized tees', 'sweatpants', 'sweatshirt', 'hoodie',
    'slides', 'socks', 'boxer shorts'
]

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


class SocialView(TemplateView):
    template_name = "core/social-share.html"


class FlashView(TemplateView):
    template_name = "core/flash-message.html"


class CommerceView(TemplateView):
    template_name = "core/commerce.html"


class ChatView(TemplateView):
    template_name = "core/chat.html"


class CountDownView(TemplateView):
    template_name = "core/countdown.html"







