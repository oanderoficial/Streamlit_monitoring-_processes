import streamlit as st
import psutil
import os

st.title("Monitoramento de Processos")

# Informações do sistema
os_info = {
    "Sistema Operacional": os.system("systeminfo"),
}
st.write(os_info)

# Listar processos
processes = [p.info for p in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_full_info', 'memory_info'])]
st.write("Processos em execução:")
st.write(processes)
