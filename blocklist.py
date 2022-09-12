
import blocklist_aggregator

ext_cfg = """
verbose: true
"""

with open("whitelist.yml") as f:
    ext_cfg += "\n" + f.read()
    
with open("blacklist.yml") as f:
    ext_cfg += "\n" + f.read()

# create raw blocklist
blocklist_aggregator.save_raw(filename="blocklist.txt",
                              cfg_update=ext_cfg)

# create blocklist with hosts format
blocklist_aggregator.save_hosts(filename="hosts.txt",
                                cfg_update=ext_cfg) 

# create blocklist to CDB format
blocklist_aggregator.save_cdb(filename="blocklist.cdb",
                              cfg_update=ext_cfg)
