// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MockRLUSD is ERC20 {
    constructor() ERC20("Mock RLUSD", "RLUSD") {
        _mint(msg.sender, 1e24); // Mint plenty for testing
    }
}
