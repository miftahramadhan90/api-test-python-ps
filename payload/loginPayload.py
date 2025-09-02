import os

student_login = {
    "login": "student.vpnsmp1_01",
    "school_id": 1469,
    "password": "portal732"
}
student_invalid_login = {
    "login": "student.vpnsmp1_01",
    "school_id": 1469,
    "password": "password12"
}

admin_login = {
    "login": "admin.x1",
    "school_id": 1802,
    "password": os.environ.get("common_pass")
}