from typing import List, Dict, Any

class WalletAPI:
    """Simula respuestas de una API real. En el futuro, aquí irán llamadas HTTP."""

    @staticmethod
    def get_balance() -> float:
        # Simula respuesta de /api/balance
        return 1250.75

    @staticmethod
    def get_transactions() -> List[Dict[str, Any]]:
        return [
            {"id": "1", "description": "Transferencia recibida", "amount": 500.00, "type": "ingreso"},
            {"id": "2", "description": "Compra en supermercado", "amount": -120.50, "type": "gasto"},
            {"id": "3", "description": "Pago freelance", "amount": 800.00, "type": "ingreso"},
            {"id": "4", "description": "Suscripción app", "amount": -12.99, "type": "gasto"},
        ]

    @staticmethod
    def add_transaction(description: str, amount: float) -> bool:
        # Simula éxito
        return True
