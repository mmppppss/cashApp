# views/base_view.py

import flet as ft

class BaseView:
    def __init__(self, page: ft.Page, view_manager):
        self.page = page
        self.vm = view_manager  # permite llamar vm.show("otra_vista")

    def build(self) -> ft.Control:
        raise NotImplementedError("Subclases deben implementar build()")
