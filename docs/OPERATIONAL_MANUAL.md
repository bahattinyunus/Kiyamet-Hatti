# Kiyamet-Hatti: Operational Manual

## 1.0 General Overview
This manual outlines the standard operating procedures (SOP) for the Kiyamet-Hatti Digital Survival Protocol. It is intended for authorized personnel (The Architect and designated survivors).

## 2.0 System Modes

### 2.1 IDLE (DEFCON 5)
- **Status**: Monitoring.
- **Action**: Periodic heartbeat checks.
- **Power Consumption**: Minimal.

### 2.2 ACTIVE (DEFCON 1)
- **Status**: Engaged.
- **Action**: 
    1.  **Lockdown**: All write access to non-critical sectors is revoked.
    2.  **Snapshot**: `Bunker` creates an immediate snapshot of `last_transmission.json`.
    3.  **Broadcast**: `SignalFlare` begins continuous loop transmission on 440Hz.

## 3.0 Troubleshooting

### 3.1 "Integrity Compromised"
If `Bunker.retrieve_log()` returns a warning:
1.  Isolate the data node.
2.  Do NOT attempt to decrypt without a secondary key.
3.  Initiate `purge_corrupted()` (To be implemented).

### 3.2 "Signal Blocked"
If `SignalFlare` fails to broadcast:
1.  Switch to fallback frequency (880Hz).
2.  Check physical layer connections.

## 4.0 Maintenance
- Run `crypto_seal.py` tests weekly.
- verifying the physical integrity of the storage medium.

> "Trust the seal. Doubt the signal."
