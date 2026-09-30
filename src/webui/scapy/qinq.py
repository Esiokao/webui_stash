from scapy.all import Ether, Dot1Q, sendp

# 構造 Q-in-Q 封包
packet = (
    Ether(dst="ff:ff:ff:ff:ff:ff", src="00:11:22:33:44:55") /  # 乙太網頭部
    Dot1Q(vlan=100) /                                          # 外層 VLAN 標籤
    Dot1Q(vlan=200) /                                          # 內層 VLAN 標籤
    b"Hello, Q-in-Q!"                                          # 負載
)

# 顯示封包結構
packet.show()

# 發送封包（需要在支持 VLAN 的網卡和環境中測試）
sendp(packet, iface="eth1")  # 替換為你的網卡名稱