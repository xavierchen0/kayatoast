//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import {AxelarExecutableWithToken} from "./axelar-gmp-sdk-solidity/contracts/executable/AxelarExecutableWithToken.sol";
import {IERC20} from "./axelar-gmp-sdk-solidity/contracts/interfaces/IERC20.sol";
import {IAxelarGasService} from "./axelar-gmp-sdk-solidity/contracts/interfaces/IAxelarGasService.sol";

/**
 * @title Call Contract With Token Contract
 * @notice Send a token along with an Axelar GMP message between two blockchains
 */
contract CallContractWithToken is AxelarExecutableWithToken {
    IAxelarGasService public immutable gasService;

    event Executed();
    event ReceivedWXRPTotal(uint256 totalAmount);

    uint256 public constant MAX_AMOUNT = 100 * 10**18; // 100 wXRP (adjust precision as needed)
    uint256 public totalWXRPHeld;

    /**
     *
     * @param _gateway address of axl gateway on deployed chain
     * @param _gasReceiver address of axl gas service on deployed chain
     */
    constructor(
        address _gateway,
        address _gasReceiver
    ) AxelarExecutableWithToken(_gateway) {
        gasService = IAxelarGasService(_gasReceiver);
    }

    /*
     * @notice trigger interchain tx from src chain
     * @dev destinationAddresses will be passed in as gmp message in this tx
     * @param destinationChain name of the dest chain (ex. "Fantom")
     * @param destinationAddress address on dest chain this tx is going to
     * @param destinationAddresses recipient addresses receiving sent funds
     * @param symbol symbol of token being sent
     * @param amount amount of tokens being sent
     */
    // function sendToMany(
    //     string memory destinationChain,
    //     string memory destinationAddress,
    //     address[] calldata destinationAddresses,
    //     string memory symbol,
    //     uint256 amount
    // ) external payable {
    //     require(msg.value > 0, "Gas payment is required");

    //     address tokenAddress = gatewayWithToken().tokenAddresses(symbol);
    //     IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount);
    //     IERC20(tokenAddress).approve(address(gatewayWithToken()), amount);
    //     bytes memory payload = abi.encode(destinationAddresses);
    //     gasService.payNativeGasForContractCallWithToken{value: msg.value}(
    //         address(this),
    //         destinationChain,
    //         destinationAddress,
    //         payload,
    //         symbol,
    //         amount,
    //         msg.sender
    //     );
    //     gatewayWithToken().callContractWithToken(
    //         destinationChain,
    //         destinationAddress,
    //         payload,
    //         symbol,
    //         amount
    //     );
    // }

    /*
     * @notice logic to be executed on dest chain
     * @dev this is triggered automatically by relayer
     * @param
     * @param
     * @param
     * @param payload encoded gmp message sent from src chain
     * @param tokenSymbol symbol of token sent from src chain
     * @param amount amount of tokens sent from src chain
     */
    function _executeWithToken(
        bytes32 /*commandId*/,
        string calldata /*sourceChain*/,
        string calldata /*sourceAddress*/,
        bytes calldata /*payload*/,
        string calldata /*tokenSymbol*/,
        uint256 amount
    ) internal override {
        totalWXRPHeld += amount;
        emit ReceivedWXRPTotal(totalWXRPHeld);

        // If the maximum amount is reached, you can add logic here to
        // distribute the tokens or perform other actions.
        if (totalWXRPHeld >= MAX_AMOUNT) {
            // Example: Distribute to a single owner
            // IERC20(gatewayWithToken().tokenAddresses(tokenSymbol)).transfer(ownerAddress, totalWXRPHeld);
            // totalWXRPHeld = 0; // Reset the balance
        }
    }

    function _execute(
        bytes32 commandId,
        string calldata sourceChain,
        string calldata sourceAddress,
        bytes calldata payload
    ) internal virtual override {}
}