from src.core.bunker import Bunker
from src.comms.flare import SignalFlare
from src.utils.crypto_seal import CryptoSeal

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Kiyamet-Hatti: Digital HAM Station")
    parser.add_argument("--tx", type=str, help="Transmit a specific message (Text Mode)")
    parser.add_argument("--rx", action="store_true", help="Listen mode (Receive)")
    args = parser.parse_args()

    print("""
    ██╗  ██╗██╗██╗   ██╗ █████╗ ███╗   ███╗███████╗████████╗
    ██║ ██╔╝██║╚██╗ ██╔╝██╔══██╗████╗ ████║██╔════╝╚══██╔══╝
    █████╔╝ ██║ ╚████╔╝ ███████║██╔████╔██║█████╗     ██║   
    ██╔═██╗ ██║  ╚██╔╝  ██╔══██║██║╚██╔╝██║██╔══╝     ██║   
    ██║  ██╗██║   ██║   ██║  ██║██║ ╚═╝ ██║███████╗   ██║   
    ╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═╝   
    
          --- H C T T I :  D I G I T A L   H A M   R A D I O ---
    """)
    
    # Initialize Core Systems
    bunker = Bunker()
    flare = SignalFlare(frequency=145.500, callsign="KIYAMET-HATTI")

    if args.rx:
        print("\n[MODE] RX ONLY")
        flare.listen(duration=5)
        return

    if args.tx:
        message = args.tx
        print(f"\n[MODE] TX MANUAL MESSAGE: '{message}'")
        bunker.secure_log("manual_tx.json", message)
        flare.broadcast(message)
        return

    # Default Simulation Mode
    print("\n[STATION] STANDBY. MONITORING 145.500 MHz.")
    print("[STATION] SQUELCH: OPEN.")
    print("[STATION] INCOMING TRAFFIC DETECTED...")
    
    # 1. Secure Critical Data (Logging the QSO)
    critical_intel = "QSO WITH UNKNOWN STATION | RST 599 | QTH: UNKNOWN"
    bunker.secure_log("station_log_001.json", critical_intel)
    
    # 2. Verify Integrity (QSL Check)
    retrieved = bunker.retrieve_log("station_log_001.json")
    print(f"[QSL CHECK] {retrieved}")
    
    # 3. Broadcast Reply (TX)
    flare.listen(duration=1) # Listen before talk!
    flare.broadcast("QSL RECEIVED. STATION OPERATIONAL. 73.")

if __name__ == "__main__":
    main()
