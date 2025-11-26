# main.py

import flet as ft
from core.view_manager import ViewManager
from views.home_view import HomeView
from views.profile_view import ProfileView
from views.register_view import RegisterView
from views.login_view import LoginView
#from views.history_view import HistoryView  # crea esta si quieres

def main(page: ft.Page):

    views = {
        "home": HomeView,
        "profile": ProfileView,
        "register": RegisterView,
        "login": LoginView
    }
    vm = ViewManager(page, views)
    vm.show("login")

ft.app(target=main, assets_dir="assets")
