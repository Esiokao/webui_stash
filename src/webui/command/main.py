# src/command/src/main.py

import asyncio

from webui.command.serial_env import SerialEnv

#
from webui.command.usecases.Login import run as run_login
from webui.command.usecases.Reset import run as run_reset
from webui.command.usecases.Reboot import run as run_reboot
from webui.command.usecases.Logout import run as run_logout
from webui.command.usecases.Vlan import run as run_vlan
from webui.command.usecases.PrivateVlan import run as run_private_vlan
from webui.command.usecases.VoiceVlan import run as run_voice_vlan 
from webui.command.usecases.QinQ import run as run_qingq
from webui.command.usecases.Dot1x import run as run_dot1x
from webui.command.usecases.Dot1v import run as run_dot1v
from webui.command.usecases.MacBaseAccessControl import run as run_mac_base_access_control
from webui.command.usecases.UserAccounts import run as run_user_accounts
from webui.command.usecases.ResetThenLogin import run as run_then_login


async def api_call_task(serial_env):
    """ 模擬持續的 API 調用 """
    if not serial_env.running:  # 如果串口已關閉，退出
        return
    run_reset(serial_env)  # 透過 API 發送命令
    

    print("📡 API sent: api_call_end")

async def async_main():
    serial_env = SerialEnv.SerialEnv(baudrate=115200, port="COM9", use_mock=False)

    # 在背景運行 user_input_loop
    input_task = asyncio.create_task(serial_env.user_input_loop())

    # 在背景運行 API 調用任務
    api_task = asyncio.create_task(api_call_task(serial_env))

    # 等待輸入任務完成（輸入 "exit" 時結束）
    await input_task

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
