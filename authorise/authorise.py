import hashlib
from config import WX_TOKEN

class Authorise(object):
    
    def __init__(self, request):
        self.request = request

    def check_signature(self):
        if not self.request.has_key('signatrue') or \
           not self.request.has_key('timestamp') or \
           not self.request.has_key('nonce'):
            return False

        signature = self.request.get('signature')
        timestamp = self.request.get('timestamp')
        nonce = self.request.get('nonce')
        combination_list =  [WX_TOKEN, timestamp, nonce]
        combination_list.sort()
        combination_str = ''.join(combination_list)
        combination_str = hashlib.sha1(combination_str).hexdigest()
        return combination_str == signatrue
