import os

student_login = {
    "login": "student.vpnsmp1_01",
    "school_id": 1469,
    "password": str(os.environ.get("student_dynamic_pwd_732"))
}
student_invalid_login = {
    "login": "student.vpnsmp1_01",
    "school_id": 1469,
    "password": "passwor_invalid_123434343))!)*"
}

admin_login = {
    "login": "admin.x1",
    "school_id": 1802,
    "password": os.environ.get("common_pass")
}