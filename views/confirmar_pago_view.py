import flet as ft
from views.base_view import BaseView
import core.data_store as store 

class ConfirmarPagoView(BaseView):

    def __init__(self, page, vm):
        super().__init__(page, vm)
        
        # Leemos el dato del buzon global
        self.qr_data = store.qr_data_leido
        
        self.usuario_field = ft.TextField(
            label="ID o Cuenta Destino", 
            width=300, 
            value=self.qr_data,
            read_only=True
        )
        self.monto_field = ft.TextField(label="Monto a Transferir (Bs)", width=300)

    def confirmar_transferencia(self, e):
        usuario = self.usuario_field.value
        monto = self.monto_field.value

        if not usuario or not monto:
            self.page.snack_bar = ft.SnackBar(ft.Text("Por favor completa los datos"))
            self.page.snack_bar.open = True
            self.page.update()
            return

        print(f"DEBUG: Transfiriendo {monto} a {usuario}...")


        # aqui concexion a base de datos :)
        
        self.page.snack_bar = ft.SnackBar(ft.Text(f"Transferencia de {monto} Bs realizada con éxito"))
        self.page.snack_bar.open = True
        self.page.update()
        
        self.vm.show("home")

    def cancelar_accion(self, e):
        print("DEBUG: Cancelando...")
        self.vm.show("home")

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Confirmar Pago QR", size=30, weight="bold"),
                ft.Divider(),
                ft.Text(f"Referencia: {self.qr_data}", size=12, color="grey"),
                ft.Container(height=20),
                self.usuario_field,
                ft.Container(height=10),
                self.monto_field,
                ft.Container(height=30),
                ft.ElevatedButton(
                    "CONFIRMAR PAGO",
                    bgcolor="blue",
                    color="white",
                    width=250,
                    height=50,
                    on_click=self.confirmar_transferencia
                ),
                ft.Container(height=10),
                ft.OutlinedButton(
                    "Cancelar",
                    icon=ft.Icons.CANCEL,
                    on_click=self.cancelar_accion
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )