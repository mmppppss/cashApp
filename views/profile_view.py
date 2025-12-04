import flet as ft
from views.base_view import BaseView
from core.theme import TEXT_PRIMARY, BACKGROUND
from api.wallet_api import WalletAPI
class ProfileView(BaseView):
    def build(self, api: WalletAPI):
        user = api.get_user()
        return ft.Column(
            controls=[
                ft.Container(height=60),
                ft.Container(
                    content=ft.CircleAvatar(
                        foreground_image_src="https://www.shutterstock.com/image-vector/vector-male-face-avatar-logo-600nw-426321556.jpg",
                        radius=50,
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(bottom=20),
                ),
                ft.Text(user['nombre'], size=22, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY, text_align=ft.TextAlign.CENTER),
                ft.Text(user['email'], size=14, color="#757575", text_align=ft.TextAlign.CENTER),
                # Aquí irían más opciones
                ft.Container(height=200),
                ft.Container(height=80),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
