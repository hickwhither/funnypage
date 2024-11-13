from flask import *

class SegmentTree:
    left: int
    right: int
    value: int
    lazy: int

    left_child: 'SegmentTree'
    right_child: 'SegmentTree'
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.mid = (self.left+self.right)//2
        self.value = 0

        self.left_child = None
        self.right_child = None
    
    def get_value(self, position):
        if position < self.left or self.right < position: return 0
        if self.left == self.right: return self.value

        sum = self.value
        if position <= self.mid and self.left_child:
            sum += self.left_child.get_value(position)
        elif self.right_child:
            sum += self.right_child.get_value(position)
        return sum

    def update_segment(self, start, end, value):
        if start > self.right or end < self.left: return
        if start <= self.left and end >= self.right:
            self.value += value
            return
    
        if not self.left_child:
            self.left_child = SegmentTree(self.left, self.mid)
        if not self.right_child:
            self.right_child = SegmentTree(self.mid + 1, self.right)

        self.left_child.update_segment(start, end, value)
        self.right_child.update_segment(start, end, value)


class segment(Blueprint):
    def __init__(self):
        super().__init__('segment', __name__, url_prefix='/segment')
        self.route('/')(self.home)
        self.route('/update', methods=["POST"])(self.update_api)
        self.route('/get', methods=["POST"])(self.get_api)
        self.LEFT = 1
        self.RIGHT = int(1e9)
        self.segtree = SegmentTree(self.LEFT, self.RIGHT)

    def home(self): return render_template('segment/index.html')
    
    def update_api(self):
        data:dict = request.get_json()
        start = data.get('start')
        end = data.get('end') 
        value = data.get('value')
        
        if not all(isinstance(x, int) for x in [start, end, value]):
            return jsonify({'error': 'Invalid input types'}), 400
            
        if start > end or start < self.LEFT or end > self.RIGHT:
            return jsonify({'error': 'Invalid range'}), 400
            
        self.segtree.update_segment(start, end, value)
        return jsonify({'success': True})

    def get_api(self):
        data:dict = request.get_json()
        position = data.get('position')
        
        if not isinstance(position, int):
            return jsonify({'error': 'Invalid input type'}), 400
            
        if position < self.LEFT or position > self.RIGHT:
            return jsonify({'error': 'Position out of range'}), 400
            
        value = self.segtree.get_value(position)
        return jsonify({'value': value})

bp = segment()