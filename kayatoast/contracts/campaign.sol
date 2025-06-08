// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract DummyCampaign {
    address public immutable RLUSD;

    event PledgeReceived(address indexed from, uint256 amount);

    constructor(address _RLUSD) {
        RLUSD = _RLUSD;
    }

    // Call this function from PledgeSwap after swap
    function receivePledge(uint256 amount) external {
        require(IERC20(RLUSD).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        emit PledgeReceived(msg.sender, amount);
    }

    // View balance of RLUSD held by this contract
    function balance() external view returns (uint256) {
        return IERC20(RLUSD).balanceOf(address(this));
    }
}
