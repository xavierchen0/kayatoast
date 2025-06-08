/* global MetaMaskOnboarding, ethers */

const XRPL = {
  chainId: "0x161c28",                         // 1 449 000  (hex string!)
  chainName: "XRPL-EVM Testnet",
  rpcUrls: ["https://rpc.testnet.xrplevm.org"],
  nativeCurrency: { name: "XRP", symbol: "axlWXRP", decimals: 18 },
  blockExplorerUrls: ["https://explorer.testnet.xrplevm.org"],
};

const WXRP         = "0x6aA92e7916b138cBD02A2D0DE57794c8c260b7C1";
// const GATEWAY     = "0x1fabf6a1bf6b3f6b9f54e9a8b67955d2e3dd60f6";
const GATEWAY     = "0xe432150cce91c13a887f7d836923d5597add8e31";
const GAS_SERVICE  = "0xbe406f0189a0b4cf3a05c286473d23791dd44cc6";
// const DEST_CHAIN   = "xrpl-evm-test-1";
const DEST_CHAIN   = "xrpl-evm-testnet";
const DEST_ADDR = "0xbb44ba14922438922ba9b48ee86f07ecc4520eb7";           /* TODO */

/* minimal ABIs */
const wxrpAbi    = ["function approve(address,uint256) external returns (bool)"];
const gatewayAbi = ["function sendToken(string,string,string,uint256) external"];
const gasSvcAbi  = [
  "function payGasForContractCallWithToken(address,string,string,bytes,string,uint256,address) external payable",
];

function waitFor(id, cb) {
  const el = document.getElementById(id);
  el ? cb(el) : setTimeout(() => waitFor(id, cb), 100);
}

async function switchOrAddChain() {
  try {
    await ethereum.request({
      method: "wallet_switchEthereumChain",
      params: [{ chainId: XRPL.chainId }],
    });
  } catch (e) {
    if (e.code === 4902) {
      await ethereum.request({
        method: "wallet_addEthereumChain",
        params: [XRPL],
      });
    } else {
      throw e;
    }
  }
}

async function connectAndPledge(btn) {
  btn.disabled = true;

  try {
    /* a) connect wallet + set chain */
    btn.innerText = "Connecting…";
    await switchOrAddChain();
    const [account] = await ethereum.request({ method: "eth_requestAccounts" });

    /* b) read amount */
    const amount = ethers.utils.parseUnits("1", 18);

    /* c) guard against placeholder addresses */
    if (/^0xYOUR/i.test(GATEWAY) || /^0xDEST/i.test(DEST_ADDR)) {
      throw new Error("Replace the TODO contract addresses in metamask.js");
    }

    /* d) set up signer + contracts */
    const signer  = new ethers.providers.Web3Provider(window.ethereum).getSigner();
    const wxrp    = new ethers.Contract(WXRP,        wxrpAbi,   signer);
    const gateway = new ethers.Contract(GATEWAY,     gatewayAbi,signer);
    const gasSvc  = new ethers.Contract(GAS_SERVICE, gasSvcAbi, signer);

    /* e) approve gateway */
    btn.innerText = "Approving…";
    await (await wxrp.approve(GATEWAY, amount)).wait();


    /* g) bridge via Axelar */
    btn.innerText = "Bridging…";
    await (await gateway.sendToken(DEST_CHAIN, DEST_ADDR, "WXRP", amount)).wait();

    btn.innerText = "Pledged!";
  } catch (e) {
    console.error(e);
    alert(e.message ?? "Transaction failed");
    btn.innerText = "Connect & Pledge";
  } finally {
    btn.disabled = false;
  }
}

window.addEventListener("DOMContentLoaded", () => {
  waitFor("connectWallet", (btn) => {
    if (!window.ethereum?.isMetaMask) {
      btn.innerText = "Install MetaMask";
      btn.onclick = () =>
        new MetaMaskOnboarding({ forwarderOrigin: "http://localhost:3000" })
          .startOnboarding();
    } else {
      btn.innerText = "Connect & Pledge";
      btn.onclick   = () => connectAndPledge(btn);
    }
  });
});
