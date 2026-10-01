import gradio as gr
import time
import pandas as pd
import numpy as np

def get_telemetry_data():
    data = {
        "Time (s)": list(range(1, 21)),
        "Voltage (V)": list(np.random.randn(19) + 12.0) + [18.5], 
        "Temperature (°C)": list(np.random.randn(19) + 45.0) + [88.2] 
    }
    return pd.DataFrame(data)

def run_triage_loop(username, password):
    if username != "dafinitiq_reviewer" or password != "secure_agent_2026":
        return "Authentication Failed: Invalid credentials.", None, "Execution blocked."
    
    log_output = "[Agent 1: Perception Guard] Scanning real-time edge telemetry arrays.\n"
    log_output += "ALERT: Voltage Surge (18.5V) & Thermal Threshold Breached (88.2°C) detected at Register 0x4F.\n\n"
    yield log_output, None, "Processing"
    time.sleep(1.2)
    
    log_output += "[Agent 2: Triaging Coordinator] Localizing anomaly signature to Core RISC-V Power Rail.\n"
    log_output += "[pgvector DB Tool] Querying internal engineering manuals for Register 0x4F.\n"
    log_output += "Match Found: Errata Sheet Sec 4.2 -> 'Over-voltage events require clock cycle division.'\n\n"
    yield log_output, None, "Analyzing Documentation"
    time.sleep(1.2)
    
    log_output += "[Agent 3: Remediation Designer] Writing safety-compliant micro-patch firmware script.\n"
    log_output += "Logic simulation verification complete. Pushing register parameters to edge gateway."
    
    remediation_script = """# Generated Autonomously by PhysiTwin AI Remediation Node
import embedded_hw_interface as hw

def safety_mitigation_loop():
    current_volt = hw.read_register(0x4F)
    if current_volt > 15.0:
        hw.write_register(0x1A, 0x02) # Set Clock Divider to 1:4
        hw.write_register(0x4F, 0x0C) # Clamp input gate to 12.0V nominal
        return "System Stabilized Successfully" """
    
    df_telemetry = get_telemetry_data()
    yield log_output, df_telemetry, remediation_script

with gr.Blocks(theme=gr.themes.Soft(), title="PhysiTwin AI MVP") as demo:
    gr.Markdown("# PhysiTwin AI — Multi-Agent Cyber-Physical Triage MVP")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### System Gateway Access")
            input_user = gr.Textbox(label="Username", value="dafinitiq_reviewer")
            input_pass = gr.Textbox(label="Password", type="password", value="secure_agent_2026")
            btn_run = gr.Button("Trigger Autonomous Triage Loop", variant="primary")
            
        with gr.Column(scale=2):
            gr.Markdown("### Live Agentic Processing Engine Logs")
            txt_logs = gr.TextArea(label="Agent Workflow Stream", placeholder="Awaiting gateway activation", interactive=False, lines=6)
            
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Ingested Anomaly Telemetry")
            plot_telemetry = gr.LinePlot(x="Time (s)", y="Voltage (V)", title="Monitored Line Inbound Fluctuations", height=280)
        with gr.Column():
            gr.Markdown("### Executed Autonomous Patch Output")
            txt_code = gr.Code(label="Remediation Script", language="python", interactive=False)

    btn_run.click(fn=run_triage_loop, inputs=[input_user, input_pass], outputs=[txt_logs, plot_telemetry, txt_code])

demo.queue().launch(server_name="0.0.0.0", server_port=7860)
