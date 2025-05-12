// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

contract LocalExample {
    uint public storageData; // 狀態變數
    // 僅存在於函式內部，在函式執行完畢後就會被釋放。
    function set(uint x) public {
        uint localVariable = x * 2; // 區域變數，僅在此函式內有效
        storageData = localVariable;
    }
}
