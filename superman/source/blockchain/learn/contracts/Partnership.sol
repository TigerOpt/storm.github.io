// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.28;

import "hardhat/console.sol";

contract Partnership {
    string private deploymentMessage = "Contract is deployed";
    uint256 private partnerAmount = 2;
    address[] public addresses;
    uint256[] public splitRatios;

    constructor(address[] memory _addresses) {
        require(_addresses.length == partnerAmount, "You can't have more than 2 partners");
        addresses = _addresses;
        ismatch(splitRatios);
        
        console.log(deploymentMessage);
    }

    function getPartnerAmount() public view returns(uint256) {
        return partnerAmount;
    }

    function ismatch(uint256[] memory _splitRatios) private pure returns(bool) {
        for(uint i = 0; i < _splitRatios.length; i++) {
            if (_splitRatios[i] <= 5) {
                return false;
            }
        }
        return true;
    }
}