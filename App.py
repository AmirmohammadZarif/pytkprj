from view.login_view import *
from view.user_view import *
from view.post_view import *

social_media = LoginView()

from model.da.database_manager import *

db = DatabaseManager()
db.make_engine()
