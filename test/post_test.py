from controller.post_controller import PostController
from controller.user_controller import UserController

user = UserController.find_by_id(1)
print(user)
post = PostController.save("NEW POST1", user)
print(post)


post = PostController.save("NEW POST2", user)
print(post)
