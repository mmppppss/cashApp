import flet as ft
from views.base_view import BaseView
from core.theme import TEXT_PRIMARY, PRIMARY, BACKGROUND, TEXT_SECONDARY, BORDER_RADIUS, ERROR
from core.utils import validate_email, show_snack, validate_password, validate_phone, validate_pin
from .components.pin_input import PinInput

class RegisterView(BaseView):
    def build(self):
        # Campos de formulario

        self.pin_input = PinInput(self.page, length=4)
        self.name_field = ft.TextField(
            label="Nombre completo",
            width=300,
            text_size=14,
            border_radius=BORDER_RADIUS,
            filled=True,
            bgcolor=ft.Colors.with_opacity(0.05, TEXT_PRIMARY),
            border_color=ft.Colors.TRANSPARENT,
            color=TEXT_PRIMARY
        )

        self.email_field = ft.TextField(
            label="Correo electrónico",
            width=300,
            text_size=14,
            border_radius=BORDER_RADIUS,
            filled=True,
            bgcolor=ft.Colors.with_opacity(0.05, TEXT_PRIMARY),
            border_color=ft.Colors.TRANSPARENT,
            keyboard_type=ft.KeyboardType.EMAIL,
            color=TEXT_PRIMARY
        )

        self.phone_field = ft.TextField(
            label="Teléfono",
            width=300,
            text_size=14,
            border_radius=BORDER_RADIUS,
            filled=True,
            bgcolor=ft.Colors.with_opacity(0.05, TEXT_PRIMARY),
            border_color=ft.Colors.TRANSPARENT,
            keyboard_type=ft.KeyboardType.PHONE,
            color=TEXT_PRIMARY
        )

        self.password_field = ft.TextField(
            label="Contraseña",
            password=True,
            can_reveal_password=True,
            width=300,
            text_size=14,
            border_radius=BORDER_RADIUS,
            filled=True,
            bgcolor=ft.Colors.with_opacity(0.05, TEXT_PRIMARY),
            border_color=ft.Colors.TRANSPARENT,
            color=TEXT_PRIMARY
        )

        self.password_repeat_field = ft.TextField(
            label="Repetir Contraseña",
            password=True,
            can_reveal_password=True,
            width=300,
            text_size=14,
            border_radius=BORDER_RADIUS,
            filled=True,
            bgcolor=ft.Colors.with_opacity(0.05, TEXT_PRIMARY),
            border_color=ft.Colors.TRANSPARENT,
            color=TEXT_PRIMARY
        )
        
        def on_register(e):
            if not validate_email(self.email_field.value):
                self.email_field.focus()
                show_snack(self.page, "Correo Malformado", success=False)
                return
            if not validate_phone(self.phone_field.value):
                self.phone_field.focus()
                show_snack(self.page, "Numero de Telefono No Valido", success=False)
                return
            if self.password_field.value != self.password_repeat_field.value:

                self.password_repeat_field.focus()
                show_snack(self.page, "Las Contraseñas No Coinciden", success=False)
                return
            if not validate_password(self.password_field.value):
                self.password_field.focus()
                show_snack(self.page, "Contraseña No Segura", success=False)
                return

            if not validate_pin(self.pin_field.value):
                self.pin_field.focus()
                show_snack(self.page, "Pin de Acceso Rapido No Valido", success=False)
                return

            # Aquí iría la lógica de registro (por ahora solo UI)
            self.vm.set_logged(True)

        def on_login(e):
            self.vm.show("login")  # ejemplo: ir a home tras registro

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
            "Volver a Iniciar Sesion",
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

                # Logo
                ft.Container(
                    content=ft.Image(
                        src="wallet.svg",
                        width=70,
                        height=70,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(bottom=20),
                ),

                # Título
                ft.Text(
                    "Registro",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=TEXT_PRIMARY,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Crea tu cuenta para empezar",
                    size=14,
                    color=TEXT_SECONDARY,
                    text_align=ft.TextAlign.CENTER,
                ),

                # Formulario
                self.name_field,
                ft.Container(height=12),
                self.email_field,
                ft.Container(height=12),
                self.phone_field,

                ft.Container(height=12),
                self.password_field,
                
                ft.Container(height=12),
                self.password_repeat_field,
                
                ft.Container(height=12),
                ft.Text(
                    "Pin",
                    size=14,
                    color=TEXT_SECONDARY,
                    text_align=ft.TextAlign.CENTER,
                ),


                self.pin_input.build(),

                ft.Container(height=40),
                register_button,

                ft.Container(height=20),
                login_button,

                ft.Container(height=40),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            spacing=0,
        )
