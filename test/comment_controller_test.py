# # from controller.like_controller import LikeController
# from controller.comment_controller import CommentController
# from controller.post_controller import PostController
# from controller.user_controller import UserController
#
# #
# # #uc = UserController()
# c_c= CommentController()
# # print(c_c.find_by_text("lololo good !!!"))
from controller import CommentController

cc = CommentController()
print(cc.get_comments_sorted_by_date_and_post_id)
