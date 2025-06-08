// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IUniswapV3Pool {
    function swap(
        address recipient,
        bool zeroForOne,            // axlXRP to RLUSD = true
        int256 amountSpecified,     // positive = exact in
        uint160 sqrtPriceLimitX96,  // 0 for no limit
        bytes calldata data         // sent to callback
    ) external returns (int256 amount0, int256 amount1);
}

interface IERC20 {
    function approve(address spender, uint value) external returns (bool);
    function transfer(address to, uint amount) external returns (bool);
    function balanceOf(address user) external view returns (uint);
    function allowance(address owner, address spender) external view returns (uint);
}

interface ISwapCallback {
    function uniswapV3SwapCallback(
        int256 amount0Delta,
        int256 amount1Delta,
        bytes calldata data
    ) external;
}

contract PledgeSwap is ISwapCallback {
    address public immutable axlXRP;
    address public immutable RLUSD;
    IUniswapV3Pool public immutable pool;
    address public campaign;

    event DebugBalance(uint256 axlXRPBalance);
    event DebugAllowance(uint256 allowance);
    event DebugSwapStarted(uint256 amount);
    event DebugSwapCompleted(uint256 rlusdOut);
    event DebugTransferCompleted(uint256 amount);

    constructor(address _axlXRP, address _RLUSD, address _pool, address _campaign) {
        axlXRP = _axlXRP;
        RLUSD = _RLUSD;
        pool = IUniswapV3Pool(_pool);
        campaign = _campaign;
    }

    /// Approve pool to spend axlXRP
    function approvePool() external {
        uint256 balance = IERC20(axlXRP).balanceOf(address(this));
        IERC20(axlXRP).approve(address(pool), balance);
    }

    /// Swap all axlXRP held by this contract into RLUSD and send to campaign
    function swapAndPledge(uint256 minAmountOut) external {
        uint256 balance = IERC20(axlXRP).balanceOf(address(this));
        emit DebugBalance(balance);
        require(balance > 0, "No axlXRP to swap");

        // Check allowance
        uint256 allowance = IERC20(axlXRP).allowance(address(this), address(pool));
        emit DebugAllowance(allowance);
        require(allowance >= balance, "Insufficient allowance");

        // Encode path data for callback
        bytes memory data = abi.encode(msg.sender);
        emit DebugSwapStarted(balance);

        // Perform the swap (0 = no price limit)
        pool.swap(
            address(this),
            true,
            int256(balance), // exact input
            0,
            data
        );

        // Forward resulting RLUSD to campaign
        uint256 rlusdOut = IERC20(RLUSD).balanceOf(address(this));
        require(rlusdOut >= minAmountOut, "Slippage too high");

        IERC20(RLUSD).transfer(campaign, rlusdOut);
        emit DebugTransferCompleted(rlusdOut);
    }

    /// Required by UniswapV3 to pay the pool
    function uniswapV3SwapCallback(
        int256 amount0Delta,
        int256 amount1Delta,
        bytes calldata /*data*/
    ) external override {
        require(msg.sender == address(pool), "Unauthorized pool");

        uint256 payAmount = amount0Delta > 0 ? uint256(amount0Delta) : uint256(amount1Delta);
        IERC20(axlXRP).transfer(msg.sender, payAmount); // pay the pool
    }

    // Function to check contract state
    function getContractState() external view returns (
        uint256 axlXRPBalance,
        uint256 rlusdBalance,
        uint256 axlXRPAllowance
    ) {
        return (
            IERC20(axlXRP).balanceOf(address(this)),
            IERC20(RLUSD).balanceOf(address(this)),
            IERC20(axlXRP).allowance(address(this), address(pool))
        );
    }
}