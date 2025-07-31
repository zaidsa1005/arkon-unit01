# ذاكرة محادثة مؤقتة داخل الجلسة
from collections import defaultdict

class MemoryBuffer:
    def __init__(self):
        self.sessions = defaultdict(list)

    def add(self, user_id, message):
        self.sessions[user_id].append(message)
        if len(self.sessions[user_id]) > 5:
            self.sessions[user_id].pop(0)

    def get(self, user_id):
        return self.sessions[user_id]