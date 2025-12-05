import flet as ft
from core.view_manager import ViewManager
from views.home_view import HomeView
from views.profile_view import ProfileView
from views.register_view import RegisterView
from views.login_view import LoginView
from views.escaner_view import EscanerQRView
# FUSIONADO: Importamos tanto tu vista como las de Pedro
from views.confirmar_pago_view import ConfirmarPagoView
from views.history_view import HistoryView
from api.wallet_api import WalletAPI

def main(page: ft.Page):
    # INICIALIZACIÓN DE API (Agregado por Pedro)
    api = WalletAPI()
    
    views = {
        "home": HomeView,
        "profile": ProfileView,
        "register": RegisterView,
        "login": LoginView,
        "escaner": EscanerQRView,
        # FUSIONADO: Agregamos ambas rutas al diccionario
        "confirmar_pago": ConfirmarPagoView,
        "history": HistoryView
    }
    
    # IMPORTANTE: Pedro cambió el ViewManager para recibir 'api'.
    # Mantenemos ese cambio para no romper el login.
    vm = ViewManager(page, views, api)
    vm.show("login")

ft.app(target=main, assets_dir="assets")