from db.mongo import complaint_collection, task_collection
from bson import ObjectId
from datetime import datetime


def check_and_close_complaint(complaint_id: ObjectId):
    open_tasks = task_collection.count_documents({
        "complaint_id": complaint_id,
        "status": {"$ne": "RESOLVED"}
    })

    if open_tasks == 0:
        complaint_collection.update_one(
            {"_id": complaint_id},
            {
                "$set": {
                    "status": "RESOLVED",
                    "updated_at": datetime.utcnow()
                }
            }
        )
        return True

    return False
