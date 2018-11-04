from pymongo import MongoClient
uri = "mongodb://admin:admin1@ds125914.mlab.com:25914/c4e23-blog"

#1 connect
client = MongoClient(uri)
#2 Get default database
db = client.get_database()
#3 Get collection
posts = db["posts"] #lazy loading
movies = db["movies"]
#4 Create data
new_post = {
    "title":"hom nay troi nang",
    "content" : "toi o van day code",
}
new_movies = {
    "title" : "Nhat ky vang anh",
    "rating": 8.0,
}
#5 insert data
#posts.insert_one(new_post)
#movies.insert_one(new_movies)

#5.1 Read data
post_list = posts.find()
#p = post_list[1]
for p in post_list: 
    print (p["title"])
    print (p["content"])
    print("%%%%%%%%%%%%%%%%%%")


#6 close connection
client.close()