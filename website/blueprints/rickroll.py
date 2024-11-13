from flask import *


class rickroll(Blueprint):
    def __init__(self):
        super().__init__('rickroll', __name__, url_prefix='/')
        self.route('/rickroll')(self.home)
        self.route('/info')(self.rickrolled)
        self.route('/info/<path>')(self.rickrolled)

    def home(self): return render_template('rickroll/index.html')    
    def rickrolled(self, path:str=None): return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

bp = rickroll()