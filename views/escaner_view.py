import flet as ft
import cv2
from views.base_view import BaseView
import core.data_store as store  # Importamos el buzón

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
                # Guardamos el dato en el buzon global
                store.qr_data_leido = value
                
                cap.release()
                cv2.destroyAllWindows()
                self.vm.show("confirmar_pago")
                break

            cv2.imshow("Escanear QR (Presiona 'q' para salir)", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.resultado_txt.value = "Cancelado."
                self.resultado_txt.color = "red"
                self.resultado_txt.update()
                break

        if cap.isOpened():
            cap.release()
        cv2.destroyAllWindows()

    def build(self):
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