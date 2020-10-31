
import blocklist_aggregator

# create raw blocklist
blocklist_aggregator.save_raw(filename="blocklist.txt")

# create blocklist with hosts format
blocklist_aggregator.save_hosts(filename="hosts.txt") 