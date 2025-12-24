import time
import random

class SignalFlare:
    """
    Signal Flare: Digital HAM Radio Transmitter
    Uses CQ protocols to establish contact.
    """
    
    def __init__(self, frequency=145.500, callsign="TB1XYZ"):
        self.frequency = frequency
        self.callsign = callsign

    def broadcast(self, message: str, repeats=3):
        """Broadcasts a CQ (General Call) message."""
        print(f"\n[TX] TUNING TO {self.frequency} MHz... SWR CHECK: OK.")
        print("="*50)
        
        # Initial CQ Call
        print(f" >> CQ CQ CQ DE {self.callsign} {self.callsign} {self.callsign}")
        print(f" >> QTH: CLASSIFIED | QRG: {self.frequency} MHz")
        print("-" * 30)
        
        for i in range(repeats):
            print(f" >> TX ({i+1}/{repeats}): {message.upper()}")
            time.sleep(0.5) 
            
        print("-" * 30)
        print(f" >> {self.callsign} STANDING BY FOR QUE.") 
        print(f" >> QRZ?")
        print("="*50 + "\n")

    def listen(self, duration=2):
        print(f"[RX] LISTENING ON {self.frequency} MHz...")
        time.sleep(duration)
        noise = random.choice(["Static Hiss...", "Clear Signal...", "Faint CW tones..."])
        print(f"[RX] {noise}")
