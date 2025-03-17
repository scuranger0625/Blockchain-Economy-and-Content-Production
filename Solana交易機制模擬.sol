// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// 宣告 PoH 合約名稱
contract ProofOfHistory {
    // 最新的 PoH 雜湊值
    bytes32 public latestHash;
    // 記錄所有交易的雜湊值
    mapping(uint256 => bytes32) public history;
    uint256 public transactionCount;

    event NewTransaction(uint256 indexed txId, address sender, uint256 timestamp, bytes32 pohHash);

    constructor() {
        // 設定初始 SEED
        latestHash = keccak256(abi.encodePacked(block.timestamp, msg.sender));
    }

    function submitTransaction(string memory txData) public {
        require(bytes(txData).length > 0, "Transaction data cannot be empty");

        uint256 timestamp = block.timestamp;

        // 計算新的 PoH 雜湊值 (H_i = Hash(H_i-1, T_i))
        bytes32 newHash = keccak256(abi.encodePacked(latestHash, txData, timestamp));

        // 存儲交易歷史
        history[transactionCount] = newHash;
        latestHash = newHash;
        transactionCount++;

        emit NewTransaction(transactionCount, msg.sender, timestamp, newHash);
    }

    function getTransactionHash(uint256 txId) public view returns (bytes32) {
        return history[txId];
    }
}
