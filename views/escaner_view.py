import flet as ft
import cv2
import json  
from views.base_view import BaseView
import core.data_store as store
from api.wallet_api import WalletAPI

class EscanerQRView(BaseView):
    def __init__(self, page, vm):
        super().__init__(page, vm)
        self.resultado_txt = ft.Text("Presiona el botón para empezar", size=16)

    def escanear(self, e):
        cap = cv2.VideoCapture(0)
        self.resultado_txt.value = "Cámara abierta..."
        self.resultado_txt.update()

        while True:
            ret, frame = cap.read()
            if not ret: break

            detector = cv2.QRCodeDetector()
            value, pts, qr_code = detector.detectAndDecode(frame)

            if value:
                print(f"DEBUG: Dato crudo: {value}")
                id_cuenta = value # Valor por defecto (si fuera texto plano)
                
                try:
                    # Intentamos leer la estructura 
                    datos = json.loads(value)
                    if "cuenta" in datos:
                        id_cuenta = str(datos["cuenta"])
                        print(f"DEBUG: ID Cuenta extraído del JSON: {id_cuenta}")
                except json.JSONDecodeError:
                    print("DEBUG: QR sin JSON, usando texto plano")
                
                # Guardamos en el buzón (Tu lógica)
                store.qr_data_leido = id_cuenta
                
                cap.release()
                cv2.destroyAllWindows()
                
                # Navegamos
                self.vm.show("confirmar_pago")
                break
                # -----------------------------------------------------

            cv2.imshow("Escanear QR ('q' para salir)", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.resultado_txt.value = "Cancelado."
                self.resultado_txt.color = "red"
                self.resultado_txt.update()
                break

        if cap.isOpened():
            cap.release()
        cv2.destroyAllWindows()

    # build recibe  api
    def build(self, api: WalletAPI = None):
        return ft.Column(
            controls=[
                ft.Text("Escáner de Pagos", size=30, weight="bold"),
                ft.Divider(),
                ft.Container(height=20),
                ft.ElevatedButton(
                    "ABRIR CÁMARA",
                    icon=ft.Icons.QR_CODE_SCANNER,
                    bgcolor="blue",
                    color="white",
                    height=50,
                    width=250,
                    on_click=self.escanear
                ),
                ft.Container(height=20),
                self.resultado_txt,
                ft.Container(height=50),
                ft.OutlinedButton(
                    "Volver al Inicio",
                    icon=ft.Icons.ARROW_BACK,
                    on_click=lambda _: self.vm.show("home")
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )