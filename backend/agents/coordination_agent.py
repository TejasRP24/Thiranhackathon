from agents.policies import DEPARTMENT_POLICY

def coordination_agent(
    issues,
    priority,
    sla_map,
    confidence,
    original_complaint,
    location
):
    if confidence < 0.4 or not issues:
        return [{
            "status": "NEEDS_CLARIFICATION",
            "message": "Insufficient information to generate department work orders"
        }]

    tasks = []

    for issue in issues:
        department = DEPARTMENT_POLICY.get(issue, "General")

        tasks.append({
            "issue": issue,
            "department": department,
            "work_order_title": generate_title(issue),
            "work_order_description": generate_description(
                issue, original_complaint, location
            ),
            "priority": priority,
            "sla_context": format_sla_context(issue, sla_map),
            "status": "ASSIGNED",
            "source": "AI Coordination Agent"
        })

    return tasks


def generate_title(issue):
    return {
        "electric_hazard": "Potential electrical hazard reported",
        "water_leak": "Water leakage reported",
        "road_damage": "Road damage reported",
        "sanitation_issue": "Sanitation concern reported"
    }.get(issue, "Public issue reported")


def generate_description(issue, complaint, location):
    base = {
        "electric_hazard": "A potential electrical safety risk has been identified.",
        "water_leak": "A water leakage issue has been reported.",
        "road_damage": "Damage to public road infrastructure has been reported.",
        "sanitation_issue": "A sanitation-related concern has been reported."
    }.get(issue, "A public issue has been reported.")

    loc_text = f" Location: {location}." if location else " Location not specified."

    return f"{base} Details: {complaint}.{loc_text}"



def format_sla_context(issue, sla_map):
    hours = sla_map[issue]["sla_hours"]
    return (
        f"As per municipal SLA policy, this issue is classified with an "
        f"expected response time of {hours} hours."
    )
