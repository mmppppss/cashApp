from typing import List, Dict, Any, Optional
import requests
import json


class WalletAPI:
    """respuestas de una API llamadas HTTP."""

    def __init__(self) -> None:
        self.url = "http://localhost:3000"
        self.jwt = None
        self.user = None
        self.history: Optional[List] = None

    def get_user(self):

        data = {
            "nombre": self.user.get("name"),
            "email": self.user.get("email"),
            "monto": self.user.get("cuenta").get('monto')
        }
        return data

    def get_history(self) -> Optional[List]:
        """
        Realiza una solicitud GET al endpoint de historial de transferencias,
        guarda el historial en self.history y lo retorna.
        """
        if not self.jwt:
            print("Error: Se requiere autenticación (token JWT) para acceder al historial.")
            return None

        url = f"{self.url}/api/transferencias/historial"
        
        headers = {
            "Authorization": f"Bearer {self.jwt}", # Usar el token guardado
            "Content-Type": "application/json"
        }

        try:
            # 1. Realizar la solicitud GET
            response = requests.get(url, headers=headers)
            response.raise_for_status() 
            
            # 2. Obtener la respuesta JSON
            history_data = response.json()
            
            # 3. Guardar el historial en la variable de instancia
            self.history = history_data
            
            print(f"Historial de transferencias cargado con éxito. ({len(self.history)} registros)")
            return self.history

        except requests.exceptions.HTTPError as errh:
            print(f"Error HTTP al obtener historial: {errh}")
            try:
                # Intenta obtener el mensaje de error de la API
                error_data = response.json()
                print("Mensaje de la API:", error_data.get('message'))
            except json.JSONDecodeError:
                pass
            return None
        
        except requests.exceptions.RequestException as err:
            print(f"Error de conexión al obtener historial: {err}")
            return None


    def login(self, email, contraseña: None, pin: None) -> bool:
        route = f"{self.url}/api/auth/login"
        payload = {
            "email": email,
        }
        if contraseña:
            payload["password"] = contraseña
        elif pin:
            payload["pin"] = pin
        else:
            return False
        # {"error": "Credenciales incompletas"}

        try:
            response = requests.post(route, json=payload)

            response.raise_for_status()

            data = response.json()
            self.jwt = data.get("token")
            self.user = data.get("user")
            return True

        except requests.exceptions.HTTPError as errh:
            try:
                print(response.json())
                return False
            except json.JSONDecodeError:
                print({"error": f"HTTP Error {response.status_code}: {response.text}"})
                return False

        except requests.exceptions.RequestException as err:
            print(f"Error de conexión: {err}")
            return False
