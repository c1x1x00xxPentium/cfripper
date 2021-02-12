from cfripper.config.filter import Filter
from cfripper.config.rule_config import RuleConfig
from cfripper.model.enums import RuleMode

# FILTERS is here a single filter instead of list of filters
FILTERS = Filter(
    rule_mode=RuleMode.WHITELISTED,
    eval={
        "and": [{"eq": [{"ref": "config.stack_name"}, "mockstack"]}, {"eq": [{"ref": "logical_id"}, "RootRoleOne"]},]
    },
    rules={"CrossAccountTrustRule"},
)
