// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

contract GlobalExample {
    address public lastCaller;

    function set() public {
        lastCaller = msg.sender; // msg.sender 是全域變數
    }
}

/*這是 Solidity 預先定義的內建變數，可以在任何函式中使用。

它們不需要宣告，例如：

msg.sender：發送交易的地址。

block.timestamp：當前區塊的時間戳。

block.number：當前區塊的編號。

tx.origin：交易的最初發送者（而非中繼者）。*/
