
import blocklist_aggregator

ext_cfg = """
verbose: true
"""

with open("/tmp/whitelist.yml") as f:
    ext_cfg += "\n" + f.read()
    
with open("/tmp/blacklist.yml") as f:
    ext_cfg += "\n" + f.read()

# create raw blocklist
blocklist_aggregator.save_raw(filename="blocklist.txt",
                              ext_cfg=ext_cfg)

# create blocklist with hosts format
blocklist_aggregator.save_hosts(filename="hosts.txt",
                                ext_cfg=ext_cfg) 