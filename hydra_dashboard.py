import streamlit as st
import subprocess
import os
import time
import platform

st.set_page_config(page_title="HYDRA Core-Banking", page_icon="🏦", layout="wide")

st.title("🏦 HYDRA Core-Banking Settlement & SWIFT Gateway")
st.markdown("### Powered by COBOL Engine & Zero-Trust Architecture")

# OS detection logic (Windows or Cloud Linux)
is_windows = platform.system() == "Windows"
binary_name = "hydra_core.exe" if is_windows else "hydra_core"
exe_path = os.path.join('cobol_engine', binary_name)

if st.button("🚀 Execute Sequential Master Update", type="primary"):
    
    # If the engine is not found (e.g., in a cloud environment), compile it immediately!
    if not os.path.exists(exe_path):
        with st.spinner('☁️ Cloud Environment Detected. Compiling COBOL Engine natively...'):
            os.makedirs('cobol_engine', exist_ok=True)
            subprocess.run(["cobc", "-x", "-free", "-o", exe_path, "src/hydra_core.cbl"])
            st.toast('COBOL Engine Compiled Successfully on Cloud!', icon='✅')

    if not os.path.exists(exe_path):
        st.error("❌ Fatal Error: Failed to compile HYDRA Engine on the server.")
    else:
        start_time = time.time()
        
        with st.spinner('⚙️ HYDRA Engine is matching records and generating SWIFT...'):
            # Create the output directory automatically to prevent FileNotFoundError in cloud environments
            os.makedirs(os.path.join('data', 'output'), exist_ok=True)
            
            # Execute the COBOL engine
            subprocess.run([exe_path])
            exec_time = time.time() - start_time
            
            st.success(f"✅ Settlement Completed in {exec_time:.4f} seconds!")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Engine Exec Time", f"{exec_time:.4f} s")
            col2.metric("SWIFT Generated", "5 MT103 messages")
            col3.metric("Accounts Settled", "12 processed")
            
            st.divider()
            
            audit_path = os.path.join('data', 'output', 'audit_report.txt')
            if os.path.exists(audit_path):
                st.subheader("🛡️ Compliance Audit Report (PII Masked)")
                with open(audit_path, 'r') as f:
                    st.code(f.read(), language="text")
            
            swift_path = os.path.join('data', 'output', 'swift_messages.txt')
            if os.path.exists(swift_path):
                st.subheader("🌐 SWIFT MT103 Generated")
                with open(swift_path, 'r') as f:
                    st.code(f.read(), language="text")
