import json
import os
from ..utils.crypto_seal import CryptoSeal

class Bunker:
    """
    The Bunker: Secure Data Vault
    Stores critical information with cryptographic integrity seals.
    """
    def __init__(self, location="bunker_logs"):
        self.location = location
        if not os.path.exists(self.location):
            os.makedirs(self.location)
        print(f"[BUNKER] System Initialized at {self.location}")

    def secure_log(self, filename: str, content: str):
        """Writes content to the bunker with a seal."""
        seal = CryptoSeal.generate_seal(content)
        data_packet = {
            "content": content,
            "seal": seal,
            "status": "SECURED"
        }
        
        filepath = os.path.join(self.location, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data_packet, f, indent=4)
        
        print(f"[BUNKER] Data secured in {filename}. Seal: {seal[:8]}...")

    def retrieve_log(self, filename: str) -> str:
        """Retrieves and verifies content from the bunker."""
        filepath = os.path.join(self.location, filename)
        if not os.path.exists(filepath):
            return "[ERROR] File not found in Bunker."
            
        with open(filepath, "r", encoding="utf-8") as f:
            data_packet = json.load(f)
            
        if CryptoSeal.verify_seal(data_packet["content"], data_packet["seal"]):
            return f"[VERIFIED] {data_packet['content']}"
        else:
            return "[WARNING] INTEGRITY COMPROMISED. DO NOT TRUST THIS DATA."
