from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
posts = db["posts"]
new_post = {
    "title":"Thở Hey cho mọi nhà",
    "author":"Dũng 9 Ngón",
    "content" : "-Mình về mình có nhớ ta\n15 năm ấy thiết tha mặn lòng\n-mình về mình có nhớ không\nnhìn Cây nhớ núi -nhìn sông nhớ nguồn \n-Tiếng ai tha thiết bên cồn \n-Bâng khuâng trong dạ, \n-bồn chồn bước đi \n-Áo chàm đưa buổi phân li \n-Cầm tay nhau  biết nói gì hôm nay \n-Sóng bắt đầu từ gió \n-gió bắt đầu từ đâu \n-em cũng không biết nữa \n-từ khi nào ta yêu nhau \n-Sông Mã xa rồi Tây tiến ơi ! \n -Nhớ về rừng núi, nhớ chơi vơi \n-Sài Khao sương lấp đoàn quân mỏi \n -Mường Lát hoa về trong đêm hơi...:))))))",
}


posts.insert_one(new_post)
client.close()