import flet as ft
from flet_camera import Camera
import asyncio
from views.base_view import BaseView
from core.theme import *

class CameraView(BaseView):
    def __init__(self, vm):
        super().__init__(vm)
        self.camera = None
        self.is_camera_initialized = False
        
    def build(self):
        return ft.Container(
            expand=True,
            bgcolor=BACKGROUND,
            content=ft.Column(
                controls=[
                    # Header
                    ft.Container(
                        height=60,
                        bgcolor=PRIMARY,
                        content=ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.ARROW_BACK,
                                    icon_color=BACKGROUND,
                                    on_click=lambda _: self.vm.show("home"),
                                ),
                                ft.Text(
                                    "Escanear QR",
                                    size=20,
                                    weight=ft.FontWeight.W_600,
                                    color=BACKGROUND,
                                    expand=True,
                                ),
                                ft.Container(width=48),  # Espacio para balance
                            ],
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=ft.padding.only(left=8, right=16),
                    ),
                    
                    # Instrucciones
                    ft.Container(
                        padding=ft.padding.all(24),
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "Escanea el código QR para transferencia",
                                    size=18,
                                    weight=ft.FontWeight.W_600,
                                    color=TEXT_PRIMARY,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                ft.Container(height=8),
                                ft.Text(
                                    "Apunta la cámara al código QR del destinatario",
                                    size=14,
                                    color=TEXT_SECONDARY,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ),
                    
                    # Contenedor de la cámara
                    ft.Container(
                        expand=True,
                        margin=ft.margin.symmetric(horizontal=24),
                        border_radius=20,
                        border=ft.border.all(2, PRIMARY),
                        alignment=ft.alignment.center,
                        content=self._build_camera_container(),
                    ),
                    
                    # Controles de cámara
                    ft.Container(
                        height=120,
                        content=ft.Column(
                            controls=[
                                ft.Container(height=16),
                                self._build_camera_controls(),
                                ft.Container(height=16),
                                self._build_manual_option(),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ),
                ],
                spacing=0,
            ),
        )
    
    def _build_camera_container(self):
        """Construye el contenedor de la cámara"""
        self.camera_container = ft.Container(
            width=300,
            height=400,
            alignment=ft.alignment.center,
            content=ft.Column(
                controls=[
                    ft.Icon(ft.Icons.CAMERA_ALT, size=64, color=PRIMARY_LIGHT),
                    ft.Text("Iniciando cámara...", size=16, color=TEXT_SECONDARY),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=16,
            ),
        )
        return self.camera_container
    
    def _build_camera_controls(self):
        """Construye los botones de control de cámara"""
        return ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.FLASH_ON,
                    icon_color=TEXT_SECONDARY,
                    icon_size=28,
                    on_click=self._toggle_flash,
                ),
                ft.Container(
                    width=80,
                    height=80,
                    border_radius=40,
                    border=ft.border.all(4, PRIMARY),
                    alignment=ft.alignment.center,
                    content=ft.IconButton(
                        icon=ft.Icons.CAMERA,
                        icon_color=PRIMARY,
                        icon_size=40,
                        on_click=self._capture_qr,
                    ),
                ),
                ft.IconButton(
                    icon=ft.Icons.CAMERA_FRONT,
                    icon_color=TEXT_SECONDARY,
                    icon_size=28,
                    on_click=self._switch_camera,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            width=300,
        )
    
    def _build_manual_option(self):
        """Opción para ingresar manualmente"""
        return ft.TextButton(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.KEYBOARD, size=20, color=PRIMARY),
                    ft.Text("Ingresar código manualmente", color=PRIMARY, size=16),
                ],
                spacing=8,
            ),
            on_click=lambda _: self._show_manual_input(),
        )
    
    async def _initialize_camera(self):
        """Inicializa la cámara después de que la vista esté cargada"""
        await asyncio.sleep(0.5)  # Pequeña espera para que la UI cargue
        
        try:
            # Crear instancia de la cámara
            self.camera = Camera(
                enable_audio=False,
                facing_mode="environment",  # Cámara trasera
                resolution=(640, 480),
            )
            
            # Actualizar el contenedor con la cámara
            self.camera_container.content = self.camera
            
            # Inicializar la cámara
            await self.camera.initialize_async()
            
            # Actualizar la UI
            await self.vm.page.update_async()
            self.is_camera_initialized = True
            
        except Exception as e:
            print(f"Error al inicializar cámara: {e}")
            self._show_error("No se pudo acceder a la cámara")
    
    async def _capture_qr(self, e):
        """Captura una imagen para escanear QR"""
        if not self.camera or not self.is_camera_initialized:
            self._show_error("Cámara no disponible")
            return
        
        try:
            # Mostrar indicador de carga
            self._show_loading()
            
            # Capturar imagen
            image_data = await self.camera.take_photo_async()
            
            # Aquí normalmente procesarías el QR
            # Por ahora simulamos un resultado
            await asyncio.sleep(1)  # Simular procesamiento
            
            # Simular datos de QR escaneado
            qr_data = {
                "nombre": "Juan Pérez",
                "cuenta": "1234-5678-9012-3456",
                "banco": "Banco Ejemplo",
                "monto": "100.00",
                "imagen": image_data,
            }
            
            # Navegar a vista de previsualización
            self.vm.show("preview", qr_data)
            
        except Exception as e:
            print(f"Error al capturar: {e}")
            self._show_error("Error al escanear el código")
        finally:
            self._hide_loading()
    
    def _toggle_flash(self, e):
        """Alternar flash (simulado)"""
        # En una implementación real, usarías los controles de la cámara
        self._show_message("Flash no disponible en esta versión")
    
    def _switch_camera(self, e):
        """Cambiar entre cámaras frontal/trasera"""
        self._show_message("Cambio de cámara no disponible en esta versión")
    
    def _show_manual_input(self):
        """Mostrar diálogo para entrada manual"""
        def close_dialog(e):
            dialog.open = False
            self.vm.page.update()
        
        def submit_manual(e):
            # Procesar entrada manual
            cuenta = cuenta_field.value
            if cuenta:
                qr_data = {
                    "nombre": "Ingreso Manual",
                    "cuenta": cuenta,
                    "banco": "Manual",
                    "monto": "",
                    "imagen": None,
                }
                self.vm.show("preview", qr_data)
            close_dialog(e)
        
        cuenta_field = ft.TextField(
            label="Número de cuenta",
            hint_text="Ej: 1234-5678-9012-3456",
            border_color=PRIMARY,
            width=300,
        )
        
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Ingresar cuenta manualmente"),
            content=ft.Column(
                controls=[
                    cuenta_field,
                    ft.Container(height=16),
                    ft.Text(
                        "Ingresa el número de cuenta del destinatario",
                        size=12,
                        color=TEXT_SECONDARY,
                    ),
                ],
                tight=True,
                height=120,
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dialog),
                ft.ElevatedButton(
                    "Continuar",
                    on_click=submit_manual,
                    style=ft.ButtonStyle(bgcolor=PRIMARY, color=BACKGROUND),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.vm.page.dialog = dialog
        dialog.open = True
        self.vm.page.update()
    
    def _show_loading(self):
        """Mostrar indicador de carga"""
        self.camera_container.content = ft.Column(
            controls=[
                ft.ProgressRing(color=PRIMARY, width=40, height=40),
                ft.Text("Escanando...", size=16, color=TEXT_SECONDARY),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=16,
        )
        self.vm.page.update()
    
    def _hide_loading(self):
        """Ocultar indicador de carga"""
        if self.camera and self.is_camera_initialized:
            self.camera_container.content = self.camera
            self.vm.page.update()
    
    def _show_error(self, message):
        """Mostrar mensaje de error"""
        snackbar = ft.SnackBar(
            content=ft.Text(message, color=BACKGROUND),
            bgcolor=ERROR,
            duration=3000,
        )
        self.vm.page.snack_bar = snackbar
        snackbar.open = True
        self.vm.page.update()
    
    def _show_message(self, message):
        """Mostrar mensaje informativo"""
        snackbar = ft.SnackBar(
            content=ft.Text(message, color=TEXT_PRIMARY),
            bgcolor=BACKGROUND,
            border=ft.border.all(1, PRIMARY_LIGHT),
            duration=2000,
        )
        self.vm.page.snack_bar = snackbar
        snackbar.open = True
        self.vm.page.update()
    
    def dispose(self):
        """Limpiar recursos de la cámara"""
        if self.camera:
            try:
                # La librería debería tener método para liberar recursos
                pass
            except:
                pass
