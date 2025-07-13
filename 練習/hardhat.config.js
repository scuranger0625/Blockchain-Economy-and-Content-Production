require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.28",
  paths: {
    sources: "./contracts",
    artifacts: "./artifacts",
    scripts: "./scripts", // ✅ 新增這一行
  },
  networks: {
    localhost: {
      url: "http://127.0.0.1:8545" // 本地 Hardhat 網絡
    }
  }
};
