import tornado.ioloop
import tornado.web
import sys
import file_util

def log(str):
    sys.stderr.write(str + "\n")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cs = file_util.getChannels();
        self.render("./config_channel.html", channels=cs);

    def post(self):
        cs = self.get_argument("data")
        with open("channels", "w") as f:
            f.write(cs);

application = tornado.web.Application([
    (r"/config", MainHandler),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "./css/"}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "./js/"}),
    (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": "./img/"}),
    ]);

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
