 import uuid
 import datetime
 from .models import Post

 class Blog(object):
     def __init__(self, author, title, description, id=None):
         self.autor = author
         self.title = title
         self.description = description
         self.id = uuid.uuid4().hex if id is None else id

     def new_post(self):
         title = input("enter post title")
         content = input('enter post content')
         date = input('enter post date or leave blank(in format(DDMMYY):')
         if date == "":
             date = datetime.datetime.utcnow()
         else:
             date = datetime.datetime.strptime(date, "Xm%y")
         post = Post(blog_id=self.id,
                     title = title,
                     content = content,
                     author = self.autor,
                     date=date)
         post.save_to_mongo()

     def get_posts(self):
         return Post.from_blog(self.id)

     def save_to_mongo(self):
         Database.insert(collection='blogs', data=self.json())

     def json(self):
         return{
             'author': self.author,
             'title': self.title,
             'description': self.description,
             'id': self.id
         }

     @staticmethod
     def from_mongo(cls, id):
         blog_data = Database.find_one(collection='blogs', query{'id': id})
         return cls(author=blog_data['author'],title=blog_data['title'],
                    description=blog_data['description'],id=blog_data['id'])