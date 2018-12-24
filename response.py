

class Response():
    def __init__(self, header=False, body=False):
        self.header = {
                'Content-Type': 'text/html'
                }
        if header:
            for k, v in header.iteritems():
                self.header[k] = v
        self.body = body
