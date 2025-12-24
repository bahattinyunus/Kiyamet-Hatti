import hashlib
import json
from datetime import datetime

class CryptoSeal:
    """
    Kiyamet-Hatti Integrity Module
    Ensures data has not been tampered with during the chaos.
    """
    
    @staticmethod
    def generate_seal(data: str) -> str:
        """Generates a SHA-256 seal for the given data."""
        timestamp = datetime.now().isoformat()
        payload = f"{data}|{timestamp}"
        seal = hashlib.sha256(payload.encode()).hexdigest()
        return f"{seal}::{timestamp}"

    @staticmethod
    def verify_seal(data: str, seal_string: str) -> bool:
        """Verifies if the data matches the seal."""
        try:
            stored_hash, timestamp = seal_string.split("::")
            payload = f"{data}|{timestamp}"
            calculated_hash = hashlib.sha256(payload.encode()).hexdigest()
            return stored_hash == calculated_hash
        except ValueError:
            return False
