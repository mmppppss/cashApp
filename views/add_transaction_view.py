import flet as ft
from views.base_view import BaseView
from core.theme import *

class AddTransactionView(BaseView):
    def build(self):
        self.desc = ft.TextField(label="Descripción", width=300)
        self.amount = ft.TextField(label="Monto", width=150, keyboard_type=ft.KeyboardType.NUMBER)
        self.tx_type = ft.Dropdown(
            width=150,
            options=[
                ft.dropdown.Option("ingreso", "Ingreso"),
                ft.dropdown.Option("gasto", "Gasto")
            ],
            value="ingreso"
        )

        def on_save(e):
            if not self.desc.value.strip():
                self.show_snack("Ingresa una descripción", success=False)
                return
            try:
                float(self.amount.value)
            except ValueError:
                self.show_snack("Monto inválido", success=False)
                return
            # Aquí iría: API.add_transaction(...)
            self.show_snack("✅ Transacción creada")
            self.navigate_to("/")

        return ft.Column([
            ft.AppBar(title=ft.Text("Nueva transacción"), bgcolor=PRIMARY, color=BACKGROUND),
            ft.Container(height=20),
            self.desc,
            ft.Row([self.amount, self.tx_type], spacing=15),
            ft.Container(height=30),
            ft.ElevatedButton("Guardar", on_click=on_save, width=200, bgcolor=PRIMARY, color=BACKGROUND)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.ADAPTIVE)
