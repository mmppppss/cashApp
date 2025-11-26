from views.home_view import HomeView
from views.transactions_view import TransactionsView
from views.add_transaction_view import AddTransactionView
from views.register_view import RegisterView
import flet as ft

class Router:
    @staticmethod
    def go(page: ft.Page, route: str):
        page.views.clear()
        view_instance = None

        if route == "/transactions":
            view_instance = TransactionsView(page)
        elif route == "/add":
            view_instance = AddTransactionView(page)
        elif route == "/register":
            view_instance = RegisterView(page)
        else:  # route == "/"
            view_instance = HomeView(page)

        # Añadir el resultado de build() dentro de una vista si es necesario
        page.views.append(ft.View(route=route, controls=[view_instance.build()]))
        page.update()
