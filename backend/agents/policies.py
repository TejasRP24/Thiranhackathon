
PRIORITY_POLICY = {
    "electric_hazard": "HIGH",
    "water_leak": "MEDIUM",
    "road_damage": "MEDIUM",
    "sanitation_issue": "LOW"
}

SLA_POLICY_HOURS = {
    "electric_hazard": {
        "HIGH": 12,
        "MEDIUM": 24,
        "LOW": 48
    },
    "water_leak": {
        "HIGH": 24,
        "MEDIUM": 48,
        "LOW": 72
    },
    "road_damage": {
        "HIGH": 48,
        "MEDIUM": 72,
        "LOW": 96
    },
    "sanitation_issue": {
        "HIGH": 24,
        "MEDIUM": 48,
        "LOW": 72
    }
}

DEPARTMENT_POLICY = {
    "electric_hazard": "Electricity",
    "water_leak": "Water",
    "road_damage": "Roads",
    "sanitation_issue": "Sanitation"
}