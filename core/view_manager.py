from api.wallet_api import WalletAPI
import flet as ft
from core.theme import BACKGROUND

class ViewManager:
    """
    Motor de vistas para apps móviles en Flet.
    Gestiona la navegación y la barra inferior.
    """

    def __init__(self, page: ft.Page, views_dict: dict, api:WalletAPI, logged=False):
        self.page = page
        self.views = views_dict  # {"home": HomeView, "profile": ProfileView, ...}
        self.current_view_key = "home"
        self.page.padding = 0
        self.page.bgcolor = BACKGROUND
        self.page.window_width = 360
        self.page.window_height = 640
        self.logged = logged
        self.api = api
    
    def set_logged(self, status: bool):
        """Cambia el estado de autenticación y actualiza la vista actual."""
        self.logged = status
        # Vuelve a mostrar la vista actual (ahora con/sin barra)
        self.show(self.current_view_key)

    def show(self, view_key: str):
        if view_key not in self.views:
            view_key = "home"

        self.current_view_key = view_key
        view_class = self.views[view_key]
        view_instance = view_class(self.page, self)

        # Limpiar y mostrar contenido + barra inferior
        self.page.controls.clear()
        self.page.add(
            ft.Column(
                controls=[
                    ft.SafeArea(
                        view_instance.build(self.api),
                        expand=True,
                        bottom=False
                    ),
                    self._build_bottom_bar()
                ],
                spacing=0,
                expand=True
            )
        )
        self.page.update()

    def _build_bottom_bar(self):
        if not self.logged:
            return ft.Container()


        # Define el orden y nombres de los íconos
        nav_items = [
            {"key": "home", "icon_active": ft.Icons.HOME, "icon_inactive": ft.Icons.HOME_OUTLINED, "label": "Inicio"},
            {"key": "profile", "icon_active": ft.Icons.PERSON, "icon_inactive": ft.Icons.PERSON_OUTLINE, "label": "Perfil"},
            {"key": "history", "icon_active": ft.Icons.HISTORY, "icon_inactive": ft.Icons.HISTORY_EDU_OUTLINED, "label": "Historial"},
        ]

        from core.theme import PRIMARY, TEXT_SECONDARY

        nav_controls = []
        for item in nav_items:
            is_active = item["key"] == self.current_view_key
            icon = item["icon_active"] if is_active else item["icon_inactive"]
            color = PRIMARY if is_active else TEXT_SECONDARY
            nav_controls.append(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Icon(icon, size=24, color=color),
                            ft.Text(item["label"], size=12, color=color),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=4,
                    ),
                    expand=True,
                    on_click=lambda e, key=item["key"]: self.show(key),
                )
            )

        return ft.Container(
            content=ft.Row(nav_controls, alignment=ft.MainAxisAlignment.SPACE_AROUND),
            height=70,
            bgcolor=BACKGROUND,
            padding=ft.padding.symmetric(horizontal=16),
            border=ft.border.only(top=ft.BorderSide(1, "#EEEEEE")),
            shadow=ft.BoxShadow(
                blur_radius=6,
                color=ft.Colors.with_opacity(0.1, "#000000"),
                spread_radius=0,
            ),
        )
