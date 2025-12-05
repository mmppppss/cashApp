# views/home_view.py

import flet as ft
from api.wallet_api import WalletAPI
from views.base_view import BaseView
from core.theme import *

class HomeView(BaseView):
    def build(self, api: WalletAPI):
        user = api.get_user()

        return ft.Column(
            controls=[
                ft.Container(height=40),
                ft.Container(
                    content=ft.Text(f"Hola, {user['nombre']}", size=20, weight=ft.FontWeight.W_500, color=TEXT_PRIMARY),
                    padding=ft.padding.only(left=24),
                    alignment=ft.alignment.center_left,
                ),
                ft.Container(
                    content=ft.Text(f"{user['monto']} Bs.", size=36, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                    padding=ft.padding.only(left=24, top=8),
                    alignment=ft.alignment.center_left,
                ),
                ft.Container(
                    bgcolor=PRIMARY_LIGHT,
                    padding=16,
                    margin=ft.margin.only(left=24, right=24, top=20, bottom=30),
                    border_radius=20,
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.WALLET, color=PRIMARY, size=28),
                            ft.Text("Disponible para gastar", color=TEXT_SECONDARY, size=14),
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),


                ft.Container(
                    content=ft.ElevatedButton(
                        on_click=lambda _: self.vm.show("escaner"),
                        
                        content=ft.Row([
                            ft.Icon(ft.Icons.QR_CODE, size=28, color=BACKGROUND),
                            ft.Text("Transferencia Rápida", size=18, weight=ft.FontWeight.W_600, color=BACKGROUND),
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=12),
                        width=300,
                        height=64,
                        style=ft.ButtonStyle(bgcolor=PRIMARY, shape=ft.RoundedRectangleBorder(radius=20)),
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(bottom=20),
                ),
                ft.Container(height=80),  # espacio para barra inferior
            ],
            spacing=0,
            expand=True,
        )
