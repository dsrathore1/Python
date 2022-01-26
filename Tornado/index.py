import tornado.web
import tornado.ioloop


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")
class staticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/home",staticRequestHandler),
    ])


app.listen(8888)
print("I am listening Port 8888")
tornado.ioloop.IOLoop.current().start()
