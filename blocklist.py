
import blocklist_aggregator

ext_cfg = """
whitelist:
  - amazonaws.com
  - s3.amazonaws.com
  - localhost.localdomain
  - t.co
"""

# create raw blocklist
blocklist_aggregator.save_raw(filename="blocklist.txt",
                              ext_cfg=ext_cfg)

# create blocklist with hosts format
blocklist_aggregator.save_hosts(filename="hosts.txt",
                                ext_cfg=ext_cfg) 