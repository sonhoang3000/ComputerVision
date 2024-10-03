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
            "major": "Teaching Computer Vision",
            "starting_year": 2022,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendace": "2024-9-19 15:27:30"
        },
    "224466":
        {
            "name": "Vũ Hoàng Sơn",
            "major": "Công nghệ thông tin ",
            "starting_year": 2022,
            "total_attendance": 10,
            "standing": "E",
            "year": 2,
            "last_attendace": "2022-9-19 15:27:30"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "billionaire",
            "starting_year": 2000,
            "total_attendance": 20,
            "standing": "CEO",
            "year": 10,
            "last_attendace": "2010-9-19 15:27:30"
        },

    "135795":
        {
            "name": "Nguyễn Thị Xuân Mai",
            "major": "Culi trăm họ, nô lệ tư bản ",
            "starting_year": 2000,
            "total_attendance": 20,
            "standing": "CEO",
            "year": 10,
            "last_attendace": "2010-9-19 15:27:30"
        },

    "193755":
        {
            "name": "Nguyễn Phạm Thuỳ Dung",
            "major": "bán bánh mì ",
            "starting_year": 2000,
            "total_attendance": 20,
            "standing": "CEO",
            "year": 10,
            "last_attendace": "2010-9-19 15:27:30"
        },

    "246810":
        {
            "name": "Daughter Anh Thư",
            "major": "Ăn bám cha mẹ ",
            "starting_year": 2000,
            "total_attendance": 20,
            "standing": "CEO",
            "year": 10,
            "last_attendace": "2010-9-19 15:27:30"
        },
}

for key,value in data.items():
    ref.child(key).set(value)
