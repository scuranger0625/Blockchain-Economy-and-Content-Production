// scripts/deploy.js
const hre = require("hardhat");

async function main() {
  // 取得合約工廠
  const Token = await hre.ethers.getContractFactory("子貨幣範例"); // 替換成你的合約名稱

  // 部署合約
  const token = await Token.deploy();

  // 等待部署完成
  await token.waitForDeployment();

  console.log(`合約已部署至地址: ${await token.getAddress()}`);
}

// 執行主函數並捕獲錯誤
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
