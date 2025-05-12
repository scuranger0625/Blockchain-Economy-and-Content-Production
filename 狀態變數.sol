// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

contract SimpleStorage {
    uint public storageData; // 狀態變數，儲存在區塊鏈上

    function set(uint x) public {
        storageData = x;
    }

    function get() public view returns (uint) {
        return storageData;
    }
}
