from agents.policies import SLA_POLICY_HOURS

def sla_agent(issue: str, priority: str):
    DEMO_MODE = True

    if DEMO_MODE:
        return {
            "sla_hours": 0.01,  
            "reason": "Demo SLA override"
        }

    issue_policy = SLA_POLICY_HOURS.get(issue)

    if not issue_policy:
        return {
            "sla_hours": 96,
            "reason": "Default SLA applied"
        }

    sla = issue_policy.get(priority, 96)

    return {
        "sla_hours": sla,
        "reason": f"SLA for {issue} at {priority} priority"
    }
