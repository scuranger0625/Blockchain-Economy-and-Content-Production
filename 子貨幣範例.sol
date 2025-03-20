// SPDX-License-Identifier:GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

// Coin是這個智能合約的名稱
contract Coin {
    // 關鍵字 “public” 自動為 public 的變數生成一個 getter 函數 允許外部查詢某個地址的餘額。
    // 接受其他合約的存取
    address public minter;  // address 是一個特殊的內建變數 存放ETH地址
    
    // mapping是Solidity中一種特殊的資料結構，用來儲存鍵值對 像雜湊或字典
    mapping (address => uint) public balances; // 儲存地址與餘額的映射

    // event 是 Solidity 中的關鍵字，用來定義事件。事件是合約和外部世界的通信方式
    // 當事件被觸發時，訊息會被記錄在區塊鏈上，並且可以被瀏覽器等工具探測到。
    // address from: 付款人地址, address to: 收款人地址, uint amount: 發送數量
    event Sent(address from, address to, uint amount);

    // constructor 是一個特殊的函數，只有在合約部署時執行一次
    constructor() {
        minter = msg.sender; // msg.sender 是呼叫合約的人的地址
    }

    function mint(address receiver, uint amount) public {
        
        // require 是 Solidity 中的一個函數，用來檢查條件是否滿足，如果不滿足則拋出異常
        // 如果滿足條件，則繼續執行下面的程式碼
        require(msg.sender == minter);
        require(amount < 1e60); // 1e60 = 10^60
        balances[receiver] += amount; // 增加接收者的餘額
    }
    function send(address receiver, uint amount) public {
        require(amount <= balances[msg.sender], "Insufficient balance.");
        balances[msg.sender] -= amount; // 減少發送者的餘額
        balances[receiver] += amount; // 增加接收者的餘額
        emit Sent(msg.sender, receiver, amount); // 觸發 Sent 事件
    }
}
