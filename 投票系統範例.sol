// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

/// @title Voting system with delegation.
contract Ballot {
    // 這是一個新的結構類型 (struct)，代表一個選民
    struct Voter {
        uint weight; // 投票權重（被授權時會累加權重）
        bool voted; // 是否已經投票
        address delegate; // 受委託投票的對象
        uint vote; // 投票的提案索引（指向 proposals 陣列中的某個提案）
    }

    // 這是一個提案的結構類型 (struct)
    struct Proposal {
        bytes32 name; // 提案名稱（最多 32 個字節）
        uint voteCount; // 累積獲得的票數
    }

    address public chairperson; // 主持人（負責管理投票權）

    // 這個 mapping 會儲存每個地址對應的 Voter 結構
    mapping(address => Voter) public voters;

    // 動態陣列，存放所有提案
    Proposal[] public proposals;
}
