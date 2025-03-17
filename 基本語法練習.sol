// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;


// contract 具備物件導向特性
contract SimpleStorage {
    
    //unit 是一種無符號整數，預設是 uint256 同時最大可存256-bit 整數(範圍 0 ~ 2^256-1)
    
    uint storageData; // 宣告一個狀態變數 storageData，型別是 uint

    // 設定變數的值 function(宣告函式) public則是開放所有人存取的函數
    function set(uint x) public {
        
        storageData = x; // 將 x 的值存入 storageData，且存放在區塊鏈上(永久保存)
    
    } 
}