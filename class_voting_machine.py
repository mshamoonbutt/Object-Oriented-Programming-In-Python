'''class VotingMachine:
    def  __init__(self,machine_state,tallies):
        self.machine_state = machine_state
        self.tallies = tallies'''

class VotingMachine:
    def __init__(self):
        self.democrat_votes = 0
        self.republican_votes = 0

    def clear(self):
        """Clear the machine state."""
        self.democrat_votes = 0
        self.republican_votes = 0

    def voteDemocrat(self):
        """Vote for the Democrat candidate."""
        self.democrat_votes += 1

    def voteRepublican(self):
        """Vote for the Republican candidate."""
        self.republican_votes += 1

    def getTallies(self):
        """Get the tallies for both parties."""
        return {"Democrat": self.democrat_votes, "Republican": self.republican_votes}

# Example usage:
voting_machine = VotingMachine()

# Voters cast their votes
voting_machine.voteDemocrat()
voting_machine.voteRepublican()
voting_machine.voteDemocrat()

# Display tallies
tallies = voting_machine.getTallies()
print("Democrat Votes:", tallies["Democrat"])
print("Republican Votes:", tallies["Republican"])

# Clear the machine state
voting_machine.clear()

# Display tallies after clearing
tallies_after_clear = voting_machine.getTallies()
print("Democrat Votes after Clearing:", tallies_after_clear["Democrat"])
print("Republican Votes after Clearing:", tallies_after_clear["Republican"])
        