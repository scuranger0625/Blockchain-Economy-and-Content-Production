import requests
import urllib3

print("🧪 測試輸出：我正在執行這份程式")
urllib3.disable_warnings()

try:
    print("🚀 開始請求 IOTA 測試網 via IP（節點 2）...")

    response = requests.get(
        "https://38.242.219.189/api/v1/info",
        headers={"Host": "api.testnet.shimmer.network"},
        verify=False
    )

    print("✅ 使用 IP 請求成功！IOTA 測試網節點資訊：")
    print(response.json())

except Exception as e:
    print("❌ 請求失敗，錯誤訊息：", e)
