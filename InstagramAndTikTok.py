class CheckMixin:
    def check(self,username,password):
        if self.username == username and self.password == password:
            print('Successfully created')
            self.count +=1

        else:
            print('Wrong creadentials')



class Instagram(CheckMixin):
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password
        self.count = 0
        


    def post_post(self,title,username,password):
        super().check(username=username, password=password)
        print(f'New post {title}')
        


class TikTok(CheckMixin):
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password
        self.count = 0
    
    def post_video(self,video,username,password):
        super().check(username=username, password=password)
        print(f'New  post {video}')
       

obj = Instagram(username='makers',password='hello1234')
obj.post_post('We are cooking',username='makers',password='hello1234')
obj.post_post('We are cooking cake',username='makers',password='hello1234')

print(obj.count)




obj2 = TikTok(username='makers',password='hello1234')
obj2.post_video('We are cooking',username='makers',password='hello1234')
print(obj2.count)

