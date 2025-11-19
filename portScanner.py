#!/usr/bin/env python3
import socket

def scan_port(host, port, timeout=0.5):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        result = s.connect_ex((host, port))
        if result == 0:
            return True
        else:
            return False
    except Exception:
        return False
    finally:
        s.close()

def main():
    host = input("Inserisci l'host o IP da scansionare: ").strip()
    start_port = int(input("Porta iniziale: "))
    end_port = int(input("Porta finale (inclusa): "))

    print(f"\n[*] Scansione di {host} dalla porta {start_port} alla {end_port}...\n")

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"[+] Porta {port}/tcp APERTA")

    print("\n[+] Scansione completata.")

if __name__ == "__main__":
    main()
