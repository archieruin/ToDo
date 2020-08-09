

def get_user_tasks(user):
    tasks = []
    user_lists = user.lists.all()
    for user_list in user_lists:
        tasks.extend(user_list.tasks.all())
    return tasks
