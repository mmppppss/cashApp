# main.py

import flet as ft
from core.view_manager import ViewManager
from views.home_view import HomeView
from views.profile_view import ProfileView
#from views.history_view import HistoryView  # crea esta si quieres

def main(page: ft.Page):
    views = {
        "home": HomeView,
        "profile": ProfileView,
        # "history": HistoryView,
    }
    vm = ViewManager(page, views)
    vm.show("home")

ft.app(target=main)
