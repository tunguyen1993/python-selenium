from flask import Flask, request, jsonify
import test
app = Flask(__name__)

@app.route("/")
def hello():

    # TuIg = test.InstagramBot("s2.shining93@gmail.com", "Quynhnga!23", request.GET('url'))
    # data = TuIg.login()
    # TuIg.closeBrower()
    return 'hello'
@app.route(
    "/ig-report/<post>")
def user_detail(post):
    ig = test.InstagramBot("s2.shining93@gmail.com", "Quynhnga!23", "https://www.instagram.com/p/" + post)
    ig_data = ig.login()
    ig.closeBrower()
    ig_data

@app.route(
    "/facebook-report/video/<post>")
def user_detail_fb_video(post):
    fb = test.FacebookBot("s2.shining93", "Quynhnga!2345", "https://www.facebook.com/" + post)
    fb.get_url_not_login()
    return fb.get_data_not_login_video()

@app.route(
    "/facebook-report/post/<post>")
def user_detail_fb_post(post):
    fb = test.FacebookBot("", "", "https://www.facebook.com/" + post)
    fb.get_url_not_login()
    return fb.get_data_not_login_post()

if __name__ == '__main__':
    app.run(debug=True)

