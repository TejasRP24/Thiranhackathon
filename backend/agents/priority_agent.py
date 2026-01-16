from agents.policies import PRIORITY_POLICY

def priority_agent(issues: list, confidence: float):
    reasoning = []

    if confidence < 0.4 or not issues:
        return {
            "priority": "LOW",
            "reason": ["Low confidence or no clear issue detected"]
        }

    final_priority = "LOW"

    for issue in issues:
        issue_priority = PRIORITY_POLICY.get(issue, "LOW")
        reasoning.append(f"{issue} mapped to {issue_priority}")

        if issue_priority == "HIGH":
            final_priority = "HIGH"
            break
        elif issue_priority == "MEDIUM" and final_priority != "HIGH":
            final_priority = "MEDIUM"

    return {
        "priority": final_priority,
        "reason": reasoning
    }
