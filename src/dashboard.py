import streamlit as st
import psutil
import time
import matplotlib.pyplot as plt

st.set_page_config(page_title="System Dashboard", page_icon="💻", layout="wide")
st.title("💻 Fancy Real-Time System Dashboard")

# Sidebar controls
refresh_rate = st.sidebar.slider("Refresh rate (seconds)", 1, 10, 2)

# Layout
col1, col2, col3, col4 = st.columns(4)

# Metrics
cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent
net = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

col1.metric("CPU Usage", f"{cpu}%")
col2.metric("RAM Usage", f"{ram}%")
col3.metric("Disk Usage", f"{disk}%")
col4.metric("Network I/O", f"{net/1024/1024:.2f} MB")

# Realtime chart
st.subheader("📊 CPU Usage Over Time")
cpu_data = []

chart = st.line_chart([])

for _ in range(30):  # 30 updates
    cpu_data.append(psutil.cpu_percent(interval=1))
    chart.line_chart(cpu_data)
    time.sleep(refresh_rate)

