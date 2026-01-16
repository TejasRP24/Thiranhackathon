from db.mongo import task_collection, task_history_collection, complaint_collection
from datetime import datetime, timedelta,timezone
from db.mongo import sla_breach_collection

def monitoring_agent():
    now = datetime.utcnow()

    tasks = task_collection.find({
        "status": {"$in": ["ASSIGNED", "IN_PROGRESS"]},
        "escalated": False
    })

    for task in tasks:
        elapsed = now - task["created_at"]
        sla_limit = timedelta(hours=task["sla_hours"])

        if elapsed > sla_limit:
            task_collection.update_one(
                {"_id": task["_id"]},
                {
                    "$set": {
                        "escalated": True,
                        "priority": "HIGH",
                        "updated_at": now
                    }
                }
            )

            task_history_collection.insert_one({
                "task_id": task["_id"],
                "old_status": task["status"],
                "new_status": task["status"],
                "changed_by": "Monitoring Agent",
                "remark": "SLA breached – auto escalated",
                "timestamp": now
            })

            complaint_collection.update_one(
                {"_id": task["complaint_id"]},
                {
                    "$set": {
                        "status": "AT_RISK",
                        "updated_at": now
                    }
                }
            )

            sla_breach_collection.insert_one({
                "task_id": task["_id"],
                "complaint_id": task.get("complaint_id"),
                "department": task["department"],
                "issue": task["issue"],
                "priority": task["priority"],
                "sla_hours": task["sla_hours"],
                "elapsed_hours": elapsed.total_seconds() / 3600,
                "breach_type": "MISS",
                "severity": "CRITICAL",
                "detected_at": datetime.now(timezone.utc),
                "action_taken": "AUTO_ESCALATED"
            })