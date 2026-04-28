import os
import time
import subprocess
import sys

def main():
    exe = os.path.join("cobol_engine", "hydra_core.exe")
    if not os.path.exists(exe):
        exe = os.path.join("cobol_engine", "hydra_core") # Linux fallback
        if not os.path.exists(exe):
            print("[!] Critical: Executable not found. Run build_hydra.bat first.")
            sys.exit(1)
            
    print("\033[1;34m[i] Initializing Hydra Core-Banking Engine...\033[0m")
    
    start_time = time.perf_counter()
    try:
        subprocess.run([exe], check=True)
    except subprocess.CalledProcessError as e:
        print(f"\033[1;31m[!] Hydra Engine crashed: {e}\033[0m")
        sys.exit(1)
    end_time = time.perf_counter()
    
    swift_file = os.path.join("data", "output", "swift_msgs.txt")
    audit_file = os.path.join("data", "output", "audit_report.txt")
    
    swift_count = 0
    if os.path.exists(swift_file):
        with open(swift_file, "r") as f:
            swift_count = len([line for line in f if line.strip()])
            
    audit_lines = []
    if os.path.exists(audit_file):
        with open(audit_file, "r") as f:
            audit_lines = [line.strip() for line in f if line.strip()]
            
    print(f"\033[1;36m{'='*65}\033[0m")
    print(f"\033[1;36m HYDRA CORE-BANKING SETTLEMENT & SWIFT GATEWAY DASHBOARD \033[0m")
    print(f"\033[1;36m{'='*65}\033[0m")
    print(f"\033[1;32m[+] Engine Exec Time: \033[0m {end_time - start_time:.4f} seconds")
    print(f"\033[1;32m[+] SWIFT Generated:  \033[0m {swift_count} MT103 messages")
    print(f"\033[1;32m[+] Accounts Settled: \033[0m {len(audit_lines)} accounts processed")
    print(f"\033[1;36m{'-'*65}\033[0m")
    print("\033[1;33mCOMPLIANCE AUDIT REPORT (PII MASKED)\033[0m")
    for line in audit_lines[:8]:
        print("  " + line)
    if len(audit_lines) > 8:
        print("  ... (truncated for dashboard view)")
    print(f"\033[1;36m{'='*65}\033[0m")

if __name__ == '__main__':
    main()
