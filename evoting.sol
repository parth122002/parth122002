pragma solidity ^0.6.6;

contract voting{
    
    struct Candidate{
        uint id;
        string name;
        uint voteCount;
    }
    
    mapping (uint => Candidate) public candidates;
    uint public candidatecount;
    mapping (address => bool) public citizen;
    
    constructor() public{
        addCandidate("Parth");
        addCandidate("Meet");
    }
    
    function addCandidate(string memory _name) private{
        candidatecount++;
        candidates[candidatecount] = Candidate(candidatecount, _name, 0);
    }
    
    function vote(uint _candidateid) public{
        require(!citizen[msg.sender]);
        
        citizen[msg.sender] = true;
        candidates[_candidateid].voteCount ++;
        
    }
}










pragma solidity ^0.5.16;

contract Election {

    struct Candidate {
        uint id;
        string name;
        uint voteCount;
        string details;
        string election_id;
    }

    mapping(uint => Candidate) public candidates;
    mapping(address => bool) public voters;

    uint public candidatesCount;

    string public candidate;

    constructor() public {}

    event votedEvent(
        uint indexed _candidateId
    );

    function addCandidate(string memory _name, string memory _details, string memory _election_id) public {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0, _details, _election_id);
    }

    function vote(uint _candidateId) public {
        require(!voters[msg.sender]);

        require(_candidateId > 0 && _candidateId <= candidatesCount);
        
        voters[msg.sender] = true;
        
        candidates[_candidateId].voteCount++;
    
        emit votedEvent(_candidateId);
    }

}

contract Migrations {
  address public owner;
  uint public last_completed_migration;

  modifier restricted() {
    if (msg.sender == owner) _;
  }

  constructor() public {
    owner = msg.sender;
  }

  function setCompleted(uint completed) public restricted {
    last_completed_migration = completed;
  }
}



pragma solidity>=0.7.0 <0.9.0;

contract Auction{
    address payable public beneficiary;
    uint public auctionEndTime;
    
    // current state of the auction 
    address public highestBidder;
    uint public highestbid; 
    bool ended;
    
    mapping(address => uint) pendingReturns;
    
    event highestBidIncreased(address bidder, uint amount);
    event auctionEnded(address winner, uint amount);
    
    constructor(uint _biddingTime, address payable _beneficiary) {
        beneficiary = _beneficiary;
        auctionEndTime = block.timestamp + _biddingTime; 
    }
    function bid() public payable {
        require(block.timestamp < auctionEndTime,'The Auction Time Is Over');
        if(msg.value > highestbid) {
            
            if(pendingReturns[msg.sender]>0)
            {
                uint amount = pendingReturns[msg.sender];
                payable(msg.sender).transfer(amount);
            }

            pendingReturns[msg.sender] = msg.value; 
            highestBidder = msg.sender;
            highestbid = msg.value;
            emit highestBidIncreased(msg.sender, msg.value);
        }
        else {
            revert('sorry, the bid is not high enough!');
        }
     }
     function withdraw() public payable returns(bool) {
        require(ended,"You Cannot Withdraw Until The Auction Has Ended");
        uint amount = pendingReturns[msg.sender];
        if(amount > 0) {
            pendingReturns[msg.sender] = 0;
        }
        
        if(!payable(msg.sender).send(amount)) {
            pendingReturns[msg.sender] = amount;
        }
        return true;
    }
    function auctionEnd() public {
        require(block.timestamp > auctionEndTime,'The Auction Cannot End Before The Specified Time');
        if(ended) revert('the auction is already over!');
        ended = true;
        emit auctionEnded(highestBidder, highestbid);
        beneficiary.transfer(highestbid);
    }
}
