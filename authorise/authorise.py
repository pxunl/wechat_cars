import hashlib
from config import WX_TOKEN

class Authorise(object):
    
    def __init__(self, request):
        self.request = request

    def check_signature(self):
        try:
            signature = self.request.GET.get('signature')
            timestamp = self.request.GET.get('timestamp')
            nonce = self.request.GET.get('nonce')
            print signature, timestamp, nonce
            combination_list =  [WX_TOKEN, timestamp, nonce]
            combination_list.sort()
            combination_str = ''.join(combination_list)
            combination_str = hashlib.sha1(combination_str).hexdigest()
            return combination_str == signature
        except KeyError as e:
            pass
		except Exception as e:
			print e

        return False
