import flet as ft
from views.base_view import BaseView
from core.theme import TEXT_PRIMARY, BACKGROUND
from api.wallet_api import WalletAPI

def transfer_item(item: dict, is_sent: bool):
    """Crea el control visual para un registro de transferencia."""
    
    # Determinar colores y signo basado en si fue ENVIADA o RECIBIDA
    color = ft.Colors.RED_600 if is_sent else ft.Colors.GREEN_600
    sign = "-" if is_sent else "+"
    
    # Obtener el nombre y email del usuario opuesto
    opuesto = item.get("usuario_opuesto", {})
    nombre_opuesto = opuesto.get("nombre", "Usuario Desconocido")
    email_opuesto = opuesto.get("email", "")

    return ft.Container(
        padding=ft.padding.symmetric(vertical=10),
        content=ft.Row(
            controls=[
                # Icono de la Transacción
                ft.Icon(
                    ft.Icons.ARROW_UPWARD_OUTLINED if is_sent else ft.Icons.ARROW_DOWNWARD_OUTLINED,
                    color=color,
                ),
                # Información del Usuario Opuesto y Fecha
                ft.Column(
                    controls=[
                        ft.Text(
                            f"{'Pago a' if is_sent else 'Recibido de'} {nombre_opuesto}",
                            size=16,
                            color=TEXT_PRIMARY,
                            weight=ft.FontWeight.W_500
                        ),
                        ft.Text(
                            email_opuesto,
                            size=12,
                            color=ft.Colors.WHITE70
                        ),
                        ft.Text(
                            item.get("fecha").split('T')[0] if item.get("fecha") else "Fecha desconocida",
                            size=11,
                            color=ft.Colors.GREY_600
                        )
                    ],
                    spacing=2,
                ),
                ft.VerticalDivider(),
                # Monto (Alineado a la derecha)
                ft.Text(
                    f"{sign} ${float(item.get('monto')):,.2f}", # Formato con 2 decimales
                    size=16,
                    color=color,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.RIGHT,
                    expand=True # Empuja el texto a la derecha
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )



class HistoryView(BaseView):
    def build(self, api: WalletAPI):
        # 1. Obtener el historial de transferencias
        # Si get_history() retorna None/False, usamos una lista vacía.
        history_data = api.get_history() or []
        
        if not history_data:
            return ft.Column(
                controls=[
                    ft.Container(height=60),
                    ft.Text("Historial de Transacciones", size=24, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                    ft.Container(height=20),
                    ft.Text("Aún no tienes transferencias registradas.", color="#757575"),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )

        # 2. Crear los controles de transferencia iterando sobre los datos
        transfer_controls = []
        for item in history_data:
            is_sent = item.get("tipo") == "ENVIADA"
            transfer_controls.append(transfer_item(item, is_sent))

        # 3. Construir la vista usando un ListView para la lista de controles
        return ft.Column(
            controls=[
                ft.Container(height=60),
                ft.Text("Historial de Transacciones", size=24, weight=ft.FontWeight.BOLD, color=TEXT_PRIMARY),
                ft.Divider(height=20, color="#252525"),
                
                ft.ListView(
                    controls=transfer_controls,
                    spacing=0, # Ajusta el espaciado entre items
                    auto_scroll=False,
                    expand=True,
                    padding=ft.padding.symmetric(horizontal=10)
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            expand=True,
        )
