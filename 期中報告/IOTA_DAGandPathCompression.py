class DAG:
    def __init__(self, n):
        """
        初始化 DAG（Tangle），建立 n 個交易節點。
        :param n: DAG 中的初始交易數量
        """
        self.n = n
        self.parent = [i for i in range(n)]  # 初始化父節點
        self.rank = [1] * n  # 設定所有節點的權重（默認為 1）
        self.tips = set(range(n))  # 初始化 Tip 集合，初始為所有節點

    def find(self, x):
        """
        使用 Path Compression 查找 x 的根節點。
        :param x: 要查找的交易節點
        :return: x 的根節點
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路徑壓縮
        return self.parent[x]

    def union(self, x, y):
        """
        合併兩個交易的根節點
        :param x: 交易 x
        :param y: 交易 y
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def attach_transaction(self, parent1, parent2, new_tx):
        """
        將新交易附加到 DAG 中。
        :param parent1: 父交易 1
        :param parent2: 父交易 2
        :param new_tx: 新交易的 ID
        """
        if parent1 in self.tips:
            self.tips.remove(parent1)
        if parent2 in self.tips:
            self.tips.remove(parent2)

        self.union(parent1, new_tx)
        self.union(parent2, new_tx)
        self.tips.add(new_tx)  # 將新交易設為 Tip

    def validate_transaction(self, tx):
        """
        驗證交易是否合法（檢查父交易的有效性）。
        :param tx: 要驗證的交易
        :return: True or False
        """
        parent_tx = self.find(tx)
        return parent_tx == tx

    def check_double_spending(self, tx1, tx2):
        """
        檢測雙花（Double-Spending）。
        :param tx1: 交易 1
        :param tx2: 交易 2
        :return: True（有雙花）或 False（無雙花）
        """
        return self.find(tx1) == self.find(tx2)

    def get_tips(self):
        """
        獲取所有有效的 Tip。
        :return: Tip 集合
        """
        tips = []
        for i in range(self.n):
            if self.find(i) == i and i in self.tips:
                tips.append(i)
        return tips

    def print_dag(self):
        """
        列印 DAG 的父子結構。
        """
        print("交易 ID  ->  父交易")
        for i in range(self.n):
            print(f"{i}  ->  {self.parent[i]}")

    def update_weight(self, tx):
        """
        更新交易的權重（Cumulative Weight）。
        :param tx: 交易節點
        """
        root = self.find(tx)
        self.rank[root] += 1  # 提升根節點的權重

# 初始化 DAG，創建 10 筆交易
dag = DAG(10)

# 附加新交易：0 和 1 作為父交易，生成交易 2
dag.attach_transaction(0, 1, 2)
dag.attach_transaction(2, 3, 4)
dag.attach_transaction(4, 5, 6)
dag.attach_transaction(6, 7, 8)

# 取得目前 DAG 的 Tip
print("目前的 Tips：", dag.get_tips())  # 應該顯示 [8]
dag.print_dag()

# 驗證交易是否有效
print("驗證交易 4：", dag.validate_transaction(4))  # True
print("驗證交易 9：", dag.validate_transaction(9))  # False

# 檢測是否有雙花
print("檢測雙花（6 和 7）：", dag.check_double_spending(6, 7))  # False
print("檢測雙花（5 和 8）：", dag.check_double_spending(5, 8))  # True

# 附加新的交易並更新 DAG
dag.attach_transaction(8, 5, 9)

# 再次檢查 Tips
print("更新後的 Tips：", dag.get_tips())

# 再次檢查雙花
print("檢測雙花（5 和 9）：", dag.check_double_spending(5, 9))  # True
