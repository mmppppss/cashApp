import flet as ft
import requests  # <--- NECESARIO para hablar con el servidor
from views.base_view import BaseView
import core.data_store as store

class ConfirmarPagoView(BaseView):
    def __init__(self, page, vm):
        super().__init__(page, vm)
        
        # Leemos el dato del buzón
        self.qr_data = store.qr_data_leido
        # Variable para guardar la conexión a la API
        self.api = None
        
        self.usuario_field = ft.TextField(
            label="ID o Cuenta Destino", 
            width=300, 
            value=self.qr_data, 
            read_only=True
        )
        self.monto_field = ft.TextField(label="Monto a Transferir (Bs)", width=300)

    def confirmar_transferencia(self, e):
        usuario = self.usuario_field.value
        monto_str = self.monto_field.value

        # 1. Validación básica
        if not usuario or not monto_str:
            self.page.snack_bar = ft.SnackBar(ft.Text("Por favor completa los datos"))
            self.page.snack_bar.open = True
            self.page.update()
            return

        print(f"DEBUG: Iniciando transacción real -> Monto: {monto_str}, Destino: {usuario}")

        # 2. CONEXIÓN REAL CON EL SERVIDOR (BACKEND)
        try:
            # Preparamos los datos como los pidió Pedro
            # Nota: Convertimos a int y float porque el servidor espera números, no texto
            datos_pago = {
                "id_cuenta_destino": int(usuario),
                "monto": float(monto_str)
            }
            
            # Construimos la URL
            url = f"{self.api.url}/api/transferencias/"
            
            # Preparamos el encabezado con tu Credencial (Token)
            headers = {
                "Authorization": f"Bearer {self.api.jwt}",
                "Content-Type": "application/json"
            }
            
            # ¡ENVIAMOS EL DINERO! 🚀
            response = requests.post(url, json=datos_pago, headers=headers)
            
            # Verificamos si salió bien
            if response.status_code == 200 or response.status_code == 201:
                print("DEBUG: ¡Transacción Exitosa en Servidor!")
                
                self.page.snack_bar = ft.SnackBar(
                    ft.Text(f"¡Éxito! Transferiste {monto_str} Bs"),
                    bgcolor="green"
                )
                self.page.snack_bar.open = True
                self.page.update()
                
                # Volver al Home (Esto recargará el saldo automáticamente)
                self.vm.show("home")
                
            else:
                # Si el servidor dice que no (ej: Saldo insuficiente)
                print(f"ERROR SERVIDOR: {response.text}")
                self.page.snack_bar = ft.SnackBar(
                    ft.Text(f"Error: {response.text}"),
                    bgcolor="red"
                )
                self.page.snack_bar.open = True
                self.page.update()

        except Exception as ex:
            print(f"ERROR CRÍTICO: {ex}")
            self.page.snack_bar = ft.SnackBar(ft.Text("Error de conexión con el servidor"), bgcolor="red")
            self.page.snack_bar.open = True
            self.page.update()

    def cancelar_accion(self, e):
        self.vm.show("home")

    # Recibimos la API real de Pedro aquí
    def build(self, api=None):
        # Guardamos la API para usarla en el botón
        self.api = api
        
        return ft.Column(
            controls=[
                ft.Text("Confirmar Pago QR", size=30, weight="bold"),
                ft.Divider(),
                ft.Text(f"Cuenta Destino: {self.qr_data}", size=16, color="blue"),
                ft.Container(height=20),
                self.usuario_field,
                ft.Container(height=10),
                self.monto_field,
                ft.Container(height=30),
                ft.ElevatedButton(
                    "CONFIRMAR PAGO REAL", # Le cambié el nombre para que sepas que es el nuevo
                    bgcolor="green",
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