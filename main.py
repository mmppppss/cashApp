# main.py

import flet as ft
from core.view_manager import ViewManager
from views.home_view import HomeView
from views.profile_view import ProfileView
from views.register_view import RegisterView
from views.login_view import LoginView
from views.escaner_view import EscanerQRView
from views.confirmar_pago_view import ConfirmarPagoView
#from views.history_view import HistoryView  # crea esta si quieres

def main(page: ft.Page):

    views = {
        "home": HomeView,
        "profile": ProfileView,
        "register": RegisterView,
        "login": LoginView,
        "escaner": EscanerQRView,
        "confirmar_pago": ConfirmarPagoView
    }
    vm = ViewManager(page, views)
    vm.show("login")

ft.app(target=main, assets_dir="assets")
