import tornado.ioloop
import tornado.web
import sys

def log(str):
    sys.stderr.write(str + "\n")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cs = self.getChannels();
        self.render("./config_channel.html", channels=cs);

    def post(self):
        cs = self.get_argument("data")
        with open("channels", "w") as f:
            f.write(cs);

    def getChannels(self):
        with open("channels") as f:
            return f.read().split();


application = tornado.web.Application([
    (r"/config", MainHandler),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "./css/"}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "./js/"}),
    (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": "./img/"}),
    ]);

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
