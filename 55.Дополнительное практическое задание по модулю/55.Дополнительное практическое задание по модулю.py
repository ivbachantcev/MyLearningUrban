import time
import sys
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                return
        print('Пользователь отсутсвует')
    
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'пользователь {nickname} уже существует')
                return
        self.users.append(new_user := User(nickname, password, age))
        self.current_user = new_user
    
    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for new_video in args:
            for old_video in self.videos:
                if new_video.title == old_video.title:
                    break
            else:
                self.videos.append(new_video)
    
    def get_videos(self, word):
        return [video.title for video in self.videos if word.lower() in video.title.lower()]
    
    def watch_video(self, name_video):
        choice_video = None
        for video in self.videos:
            if video.title == name_video:
                choice_video = video
                break
        if choice_video:
            if self.current_user == None:
                print('Войдите в аккаунт, чтобы смотреть видео')
                return
            if choice_video.adult_mode and self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                return
            for sec in range(choice_video.time_now, choice_video.duration):
                print(sec + 1, end=' ')
                sys.stdout.flush()
                time.sleep(1)
            print('Конец видео')
            choice_video.time_now = 0



class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode



class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age = age
        self.password = hash(password)

    def __str__(self):
        return self.nickname


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')