from api.wallet_api import WalletAPI
import flet as ft
from views.base_view import BaseView
from core.theme import TEXT_PRIMARY, PRIMARY, BACKGROUND, TEXT_SECONDARY, BORDER_RADIUS
from core.utils import show_snack, validate_pin

from .components.pin_input import PinInput

class LoginView(BaseView):
    def build(self, api: WalletAPI):

        self.pin_input = PinInput(self.page, length=4)
        self.phone_field = ft.TextField(
            label="Usuario, correo, telefono",
            width=300,
            text_size=14,
            border_radius=BORDER_RADIUS,
            filled=True,
            bgcolor=ft.Colors.with_opacity(0.05, TEXT_PRIMARY),
            border_color=ft.Colors.TRANSPARENT,
            keyboard_type=ft.KeyboardType.PHONE,
            color=TEXT_PRIMARY
        )

        def on_register(e):
            self.vm.show("register") 

        def on_login(e):
            mail = self.phone_field.value
            pin = self.pin_input.get_pin()
            if not validate_pin(self.pin_input.get_pin()):
                self.pin_input.clear()
                show_snack(self.page, "Pin de Acceso Rapido No Valido", success=False)
                return
            logged = api.login(mail, None, pin)
            if logged:
               self.vm.set_logged(True)
               self.vm.show("home")
            else:
                show_snack(self.page, "Error en las credenciales")


        register_button = ft.ElevatedButton(
            "Crear cuenta",
            width=300,
            height=50,
            style=ft.ButtonStyle(
                bgcolor=PRIMARY,
                color=BACKGROUND,
                shape=ft.RoundedRectangleBorder(radius=BORDER_RADIUS),
            ),
            on_click=on_register,
        )

        login_button = ft.ElevatedButton(
            "Iniciar Sesion",
            width=300,
            height=50,
            style=ft.ButtonStyle(
                bgcolor=PRIMARY,
                color=BACKGROUND,
                shape=ft.RoundedRectangleBorder(radius=BORDER_RADIUS),
            ),
            on_click=on_login,
        )
        return ft.Column(
            controls=[
                ft.Container(height=60),

                # Logo
                ft.Container(
                    content=ft.Image(
                        src="wallet.svg",
                        width=100,
                        height=100,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(bottom=20),
                ),

                # Título
                ft.Text(
                    "Iniciar Sesion",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=TEXT_PRIMARY,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Ingrese sus credenciales",
                    size=14,
                    color=TEXT_SECONDARY,
                    text_align=ft.TextAlign.CENTER,
                ),

                # Formulario
                ft.Container(height=12),
                self.phone_field,
                
                ft.Container(height=12),

                ft.Text(
                    "Pin",
                    size=14,
                    color=TEXT_SECONDARY,
                    text_align=ft.TextAlign.CENTER,
                ),

                self.pin_input.build(),
                
                ft.Container(height=40),
                login_button,
                ft.Container(height=40),
                register_button,

                ft.Container(height=40),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            spacing=0,
        )
