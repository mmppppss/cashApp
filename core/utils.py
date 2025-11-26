import re
import flet as ft
from core.theme import SUCCESS, ERROR, PRIMARY  # opcional, para colores consistentes

def validate_email(email: str) -> bool:
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.fullmatch(regex, email))
def validate_password(password: str) -> bool:
    regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    return bool(re.fullmatch(regex, password))
def validate_name(name: str) -> bool:
    regex = r'^[A-Za-z\s]+$'
    return bool(re.fullmatch(regex, name))
def validate_phone(phone: str) -> bool:
    regex = r'^\d{8}$'
    return bool(re.fullmatch(regex, phone))
def validate_pin(pin: str) -> bool:
    regex = r'^\d{4}$'
    return bool(re.fullmatch(regex, pin))

def show_snack(page: ft.Page, message: str, success: bool = True):
    bgcolor = SUCCESS if success else ERROR
    snack = ft.SnackBar(
        content=ft.Text(message, color="#FFFFFF"),
        bgcolor=bgcolor,
        duration=3000,
    )
    
    page.overlay.clear()       
    page.overlay.append(snack)
    snack.open = True        
    page.update()           
