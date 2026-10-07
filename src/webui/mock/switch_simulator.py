"""
Switch CLI & Protocol Mock Simulator.
Simulates switch behavior for local unit/integration tests and CI/CD pipelines
without requiring physical testbed equipment.
"""

import re
from typing import Dict, Any, Optional


class MockSwitchSimulator:
    """
    Mock Switch Engine that stores device state (IP, VLANs, Ports)
    and produces realistic CLI output for standard switch commands.
    """

    def __init__(self, model: str = "DGS-1210-10XS"):
        self.model = model
        self.state: Dict[str, Any] = {
            "system_name": "DGS-1210-52X/ME",
            "ip_mode": "Static",
            "ip_address": "192.168.1.1",
            "subnet_mask": "255.255.255.0",
            "default_gateway": "0.0.0.0",
            "vlans": {
                "1": {"name": "default", "type": "Static", "ports": "1-10"},
            },
            "ports": {
                f"eth{i}": {"state": "Enabled", "speed": "1000M", "duplex": "Full", "link": "Up" if i <= 4 else "Down"}
                for i in range(1, 11)
            },
        }

    def execute_command(self, cmd: str) -> str:
        """
        Parses a CLI command and returns simulated console output,
        updating internal state if it's a configuration command.
        """
        cmd = cmd.strip()

        # 1. Show commands
        if re.match(r"^show\s+ip\s+interface", cmd, re.IGNORECASE):
            return (
                f"\nInterface: System\n"
                f"  IP Address      : {self.state['ip_address']}\n"
                f"  Subnet Mask     : {self.state['subnet_mask']}\n"
                f"  Default Gateway : {self.state['default_gateway']}\n"
                f"  Config Mode     : {self.state['ip_mode']}\n"
                f"Switch# "
            )

        if re.match(r"^show\s+vlan", cmd, re.IGNORECASE):
            vlan_lines = []
            for vid, info in self.state["vlans"].items():
                vlan_lines.append(f"  {vid:<6} {info['name']:<15} {info['type']:<10} {info['ports']}")
            output_table = "\n".join(vlan_lines)
            return (
                f"\nVID    VLAN Name       Type       Ports\n"
                f"------ --------------- ---------- -------------------\n"
                f"{output_table}\n"
                f"Switch# "
            )

        if re.match(r"^show\s+switch", cmd, re.IGNORECASE) or re.match(r"^show\s+system", cmd, re.IGNORECASE):
            return (
                f"\nDevice Type       : {self.model}\n"
                f"System Name       : {self.state['system_name']}\n"
                f"Firmware Version  : 1.00.012\n"
                f"Hardware Version  : A1\n"
                f"MAC Address       : 00-11-22-33-44-55\n"
                f"Switch# "
            )

        # 2. Config commands
        if cmd.startswith("config ipif System ipaddress"):
            parts = cmd.split()
            if len(parts) >= 5:
                self.state["ip_address"] = parts[3]
                self.state["subnet_mask"] = parts[4]
                return "\nSuccess.\nSwitch# "

        if cmd.startswith("create vlan"):
            # e.g., create vlan vlan100 tag 100 or create vlan 100
            parts = cmd.split()
            if len(parts) >= 5 and parts[3].lower() == "tag":
                vname = parts[2]
                vid = parts[4]
                self.state["vlans"][vid] = {"name": vname, "type": "Static", "ports": "None"}
                return f"\nVLAN {vid} created successfully.\nSwitch# "
            elif len(parts) >= 3:
                vid = parts[2]
                self.state["vlans"][vid] = {"name": f"VLAN_{vid}", "type": "Static", "ports": "None"}
                return f"\nVLAN {vid} created successfully.\nSwitch# "


        if cmd == "save":
            return "\nSaving configuration to NVRAM... Done.\nSwitch# "

        # Default fallback
        return f"\nCommand executed: {cmd}\nSwitch# "
