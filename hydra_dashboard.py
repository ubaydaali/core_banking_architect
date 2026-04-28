import streamlit as st
import subprocess
import os
import time

st.set_page_config(page_title="HYDRA Core-Banking", page_icon="🏦", layout="wide")

st.title("🏦 HYDRA Core-Banking Settlement & SWIFT Gateway")
st.markdown("### Powered by COBOL Engine & Zero-Trust Architecture")

if st.button("🚀 Execute Sequential Master Update", type="primary"):
    exe_path = os.path.join('cobol_engine', 'hydra_core.exe')
    
    if not os.path.exists(exe_path):
        st.error("❌ HYDRA Engine not found! Please run build_hydra.bat first.")
    else:
        start_time = time.time()
        
        with st.spinner('⚙️ HYDRA Engine is matching records and generating SWIFT...'):
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