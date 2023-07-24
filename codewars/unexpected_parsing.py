# Expected Behaviour
# Function should return a dictionary/Object/Hash with "status" as a key,
# whose value can : "busy" or "available"
# depending on the truth value of the argument is_busy.

def get_status(is_busy):
    status = {"status": "busy"} if is_busy is True else {"status": "available"}
    return status
