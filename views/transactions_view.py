import flet as ft
from views.base_view import BaseView
from core.theme import *
from api.wallet_api import WalletAPI

class TransactionsView(BaseView):
    def build(self):
        txs = WalletAPI.get_transactions()
        list_view = ft.ListView(spacing=10, padding=10)

        for tx in txs:
            amount = tx["amount"]
            is_income = amount > 0
            color = SUCCESS if is_income else ERROR
            icon = ft.icons.ARROW_UPWARD if is_income else ft.icons.ARROW_DOWNWARD

            list_view.controls.append(
                ft.Card(
                    content=ft.Container(
                        ft.Row([
                            ft.Icon(icon, color=color),
                            ft.Column([
                                ft.Text(tx["description"], weight=ft.FontWeight.BOLD),
                                ft.Text("Hoy", size=12, color=TEXT_SECONDARY)
                            ], expand=True),
                            ft.Text(f"${abs(amount):.2f}", color=TEXT_SECONDARY),
                            ft.Text(f"${amount:.2f}", color=color, weight=ft.FontWeight.BOLD)
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        padding=15
                    )
                )
            )

        return ft.Column([
            ft.AppBar(title=ft.Text("Historial"), bgcolor=PRIMARY, color=BACKGROUND),
            list_view
        ], expand=True)
