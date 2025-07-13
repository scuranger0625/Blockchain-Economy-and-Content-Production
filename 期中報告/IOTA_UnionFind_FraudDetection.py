from pyspark.sql import SparkSession
import pandas as pd

# 建立 Spark Session
spark = SparkSession.builder.appName("IOTA_Fraud_UnionFind").getOrCreate()

# 模擬交易資料 (Sender ➝ Receiver)
transactions = [
    ("A", "B"),   # A 是黑名單帳戶
    ("B", "C"),
    ("C", "D"),
    ("X", "Y"),
    ("Y", "Z"),
    ("Z", "E"),
    ("Q", "R"),
    ("R", "S"),
    ("S", "D"),   # 嘗試與 D 合併資金鏈
]

# 轉為 Spark DataFrame
df = spark.createDataFrame(transactions, ["sender", "receiver"])

# 轉為 Pandas 模擬 Union-Find（適用小規模）
df_pd = df.toPandas()

# 初始化 Union-Find 結構
parent = {}

def find(x):
    if x not in parent:
        parent[x] = x
    if parent[x] != x:
        parent[x] = find(parent[x])  # 路徑壓縮
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x

# 建立資金群關聯
for sender, receiver in df_pd.itertuples(index=False):
    union(sender, receiver)

# 假設 A 是黑名單帳戶
blacklist_root = find("A")

# 找出所有與黑名單帳戶 A 在同群的帳戶
high_risk_accounts = [acc for acc in parent if find(acc) == blacklist_root]

# 顯示為表格
result_df = pd.DataFrame(high_risk_accounts, columns=["High_Risk_Accounts"])
print("\n⚠️  與黑名單帳戶 A 屬於同一資金鏈的高風險帳戶：\n")
print(result_df.to_string(index=False))
