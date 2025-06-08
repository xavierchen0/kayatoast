// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MockAxlXRP is ERC20 {
    constructor() ERC20("Mock AxlXRP", "axlXRP") {
        // Mint 1 million axlXRP (with 18 decimals) to deployer
        _mint(msg.sender, 1_000_000 * 10 ** decimals());
    }
}
