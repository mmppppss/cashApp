import flet as ft
from core.theme import TEXT_PRIMARY, PRIMARY

class PinInput:
    def __init__(self, page: ft.Page, length: int = 4):
        self.page = page
        self.length = length
        self.fields = []
        self._on_change_callback = None

        # Crear los campos
        for i in range(length):
            field = ft.TextField(
                width=60,
                height=60,
                text_align=ft.TextAlign.CENTER,
                text_size=24,
                border=ft.InputBorder.UNDERLINE,
                border_color=ft.Colors.GREY_400,
                focused_border_color=PRIMARY,
                input_filter=ft.NumbersOnlyInputFilter(),
                max_length=1,
                on_change=lambda e, idx=i: self._on_digit_change(e, idx),
                text_style=ft.TextStyle(color=TEXT_PRIMARY, weight=ft.FontWeight.BOLD),
                keyboard_type=ft.KeyboardType.NUMBER,
            )
            self.fields.append(field)

        self.container = ft.Row(
            controls=self.fields,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,
        )

    def _on_digit_change(self, e, index: int):
        value = e.control.value
        if value.isdigit():
            # Mover foco al siguiente campo
            if index < self.length - 1 and value != "":
                self.fields[index + 1].focus()
        elif value == "":
            # Si borra, mover foco al anterior (opcional)
            if index > 0:
                self.fields[index - 1].focus()

        # Llamar al callback si está definido
        if self._on_change_callback:
            self._on_change_callback(self.get_pin())

    def get_pin(self) -> str:
        return "".join(field.value for field in self.fields)

    def set_on_change(self, callback):
        """callback(pin: str)"""
        self._on_change_callback = callback

    def clear(self):
        for field in self.fields:
            field.value = ""
        self.fields[0].focus()
        self.page.update()

    def build(self) -> ft.Control:
        return self.container
