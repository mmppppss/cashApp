import flet as ft
from views.base_view import BaseView
from core.theme import TEXT_PRIMARY, BACKGROUND

class ProfileView(BaseView):
    def build(self):
        return ft.Column(
            controls=[
                ft.Container(height=60),
                ft.Container(
                    content=ft.CircleAvatar(
                        foreground_image_src="https://i.pravatar.cc/150?img=12",
                        radius=50,
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(bottom=20),
                ),
                ft.Text("María Pérez", size=22, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY, text_align=ft.TextAlign.CENTER),
                ft.Text("maria@example.com", size=14, color="#757575", text_align=ft.TextAlign.CENTER),
                # Aquí irían más opciones
                ft.Container(height=200),
                ft.Container(height=80),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
