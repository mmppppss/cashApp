# main.py

import flet as ft
from core.view_manager import ViewManager
from views.home_view import HomeView
from views.profile_view import ProfileView
from views.register_view import RegisterView

#from views.history_view import HistoryView  # crea esta si quieres

def main(page: ft.Page):

    views = {
        "home": HomeView,
        "profile": ProfileView,
        "register": RegisterView
        # "history": HistoryView,
    }
    vm = ViewManager(page, views)
    vm.show("register")

ft.app(target=main)
