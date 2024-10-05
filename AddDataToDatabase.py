import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://facerecognition-b74ff-default-rtdb.firebaseio.com/"
})

ref = db.reference("VAA")

data = {
    "321654":
        {
            "name": "Murtaza",
            "MSSV": "0987654321",
            "total_attendance": 10,
            "last_attendace": "2022-9-19 15:27:30"
        },
    # "224466":
    #     {
    #         "name": "Vũ Hoàng Sơn",
    #         "major": "Công nghệ thông tin ",
    #         "starting_year": 2022,
    #         "total_attendance": 10,
    #         "standing": "E",
    #         "year": 2,
    #         "last_attendace": "2022-9-19 15:27:30"
    #     },
    "963852":
        {
            "name": "Elon Musk",
            "MSSV": "0123456789",
            "total_attendance": 10,
            "last_attendace": "2022-9-19 15:27:30"

        },

    "135795":
        {
            "name": "Nguyễn Thị Xuân Mai",
            "MSSV": "2254810240",
            "total_attendance": 10,
            "last_attendace": "2022-9-19 15:27:30"

        },

    "193755":
        {
            "name": "Nguyễn Phạm Thuỳ Dung",
            "MSSV": "2254810131",
            "total_attendance": 10,
            "last_attendace": "2022-9-19 15:27:30"

        },

    "246810":
        {
            "name": "Daughter Anh Thư",
            "MSSV": "2254810261",
            "total_attendance": 10,
            "last_attendace": "2022-9-19 15:27:30"
        },
}

for key,value in data.items():
    ref.child(key).set(value)
