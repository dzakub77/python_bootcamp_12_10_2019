def print_total_time(user_total_time):
    for user, tt in sorted(user_total_time)


def zlicz_czasy1(file_name):
    sum_login_time = {}


    sum_logout_time = {}
    with open(file_name) as f:
        for line in f:
            name, action, current_time = line.strip().split(";")
            current_time = int(current_time)
            if action == "LOGIN":
                sum_login_time[name] = sum_login_time.get(name, 0) + current_time
            if action == "LOGOUT":
                sum_logout_time[name] = sum_logout_time.get(name, 0) + current_time

    user_total_time = {}

    for user in sum_logout_time:
        user_total_time[user] = sum_logout_time[user] - sum_login_time[user])
    print_total_time(user_total_time)

class User:
        def __init__(self, name):
            self.name = name
            self.last_login_time = 0
            self.total_time = 0

        def set_last_login_time(self, t):
            self.last_login_time = t

        def incr_total_time(self, t):
            self.total_time += t - self.last_login_time

def zlicz_czasy_3(file_name):
    users = {}
    with open(file_name) as f:
        for line in f:
            name, action, current_time = line.strip().split(";")
            if name in users:
                user = users[name]
            else:
                user = User(name)
                users[name] = user
            current_time = int(current_time)
            if action == "LOGIN":
                users[name].set_last_login_time(current_time)
            elif action == "LOGOUT":
                users[name].incr_total_time(current_time)
    user_total_time = {name: users[name].total_time for name in users}
    print_total_time(user_total_time)
