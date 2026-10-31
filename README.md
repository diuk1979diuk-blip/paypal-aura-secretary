Markdown


# AURA-Secretary: Autonomous AI & Inclusive PayPal Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PayPal API Sandbox](https://img.shields.io/badge/PayPal-Sandbox_v2-blue)](https://developer.paypal.com)

AURA-Secretary is an empathetic, autonomous AI assistant and spatial companion designed for the **PayPal AI Hackathon**. It merges automated financial management via the PayPal Sandbox API with a physical, multi-modal feedback architecture (light, micro-vapor, and tactile pulses) tailored for individuals with sensory accessibility needs.

---

## Key Features

- **Autonomous Agentic Commerce:** Executes and verifies micro-payments, order creations, and recurring flows using the PayPal Orders API (`/v2/checkout/orders`).
- **Inclusive Multi-Modal Interface:** Converts financial statuses and system actions into visual light patterns (WS2815 RGB) and ultrasonic micro-vapor pulses for visually and hearing-impaired users.
- **Operational & Financial Advisory:** Analyzes transactional context to provide real-time budget optimization and operational guidance.
- **Localized Edge Intelligence:** Runs agentic orchestration locally on NVIDIA Jetson Orin edge architecture for privacy and low-latency interaction.

---

## Project Structure

```text
paypal-aura-secretary/
├── LICENSE                 # MIT License file
├── README.md               # Project documentation
├── requirements.txt        # Dependencies
├── system_instructions.md  # Core AI System Prompt
└── src/
    ├── main.py             # Entry point / CLI Interface
    ├── agent_brain.py      # Decision engine & empathy feedback logic
    └── paypal_client.py    # PayPal Orders API Sandbox client
