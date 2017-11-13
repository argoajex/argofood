from application import app

PORT = 5000

# ------- PRODUCTION CONFIG -------
# http_server = HTTPServer(WSGIContainer(app))
# http_server.bind(PORT)
# http_server.start(0)
# ioloop = tornado.ioloop.IOLoop().instance()
# autoreload.start(ioloop)
# ioloop.start()

# ------- DEVELOPMENT CONFIG -------
app.run(host='0.0.0.0', port=PORT, debug=True)