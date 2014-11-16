#!/usr/bin/env python
# coding=utf-8

# from Model import *
from flask import *
# from jinja2 import evalcontextfilter, Markup, escape
# import re
# import mail
# import requests
# from flask.ext.login import LoginManager, login_user , logout_user , current_user , login_required
# from flask.ext.security import login_required
# from datetime import datetime
# import json
# import time

# create a flask application - this ``app`` object will be used to handle
# inbound requests, routing them to the proper 'view' functions, etc
application = app = Flask('wsgi')
app.config.from_object(__name__)

app.debug = True
# app.secret_key = "ZTCNREe68EqhzDY8zUuwZTCNREe68EqhzDY8zUuw"

# token=BAjSyCBUDJaKZXFuWe7N95re
# team_id=T0001
# channel_id=C2147483705
# channel_name=test
# user_id=U2147483697
# user_name=Steve
# command=/weather
# text=94070

@app.route('/go',methods=['GET','POST'])
def go():
    token = request.form['token'] if 'token' in request.form else None
    team_id = request.form['team_id'] if 'team_id' in request.form else None
    channel_id = request.form['channel_id'] if 'channel_id' in request.form else None
    channel_name = request.form['channel_name'] if 'channel_name' in request.form else None
    user_id = request.form['user_id'] if 'user_id' in request.form else None
    user_name = request.form['user_name'] if 'user_name' in request.form else None
    command = request.form['command'] if 'command' in request.form else None
    text = request.form['text'] if 'text' in request.form else None
    return "http://example.com/"+text






# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# _paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')

# mail.MAILGUN_DOMAIN = "bwappmanager.mailgun.org"
# mail.MAILGUN_KEY = "key-2ttnz6zg-caq3mf3w5hevnr4t2weo5v0"


# @app.template_filter()
# @evalcontextfilter
# def nl2br(eval_ctx, value):
#     result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') \
#                           for p in _paragraph_re.split(value))
#     if eval_ctx.autoescape:
#         result = Markup(result)
#     return result

# @app.template_filter()
# @evalcontextfilter
# def icon(eval_ctx, value):
#     return re.sub("-\d+.(apk|ipa)$", ".png", value);

############
#   AUTH
############

# @login_manager.user_loader
# def load_user(id):
#     return User.get(id=int(id))


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'GET':
#         return render_template('register.html')
#     user = User.create(username=request.form['username'],
#                        password=request.form['password'],
#                        email=request.form['email'],
#                        registered_on=datetime.utcnow())
#     flash('User successfully registered')
#     return redirect(url_for('login'))


# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('login.html')
#     username = request.form['username']
#     password = request.form['password']
#     registered_user = User.get(username=username,password=password)
#     if registered_user is None:
#         flash('Username or Password is invalid' , 'error')
#         return redirect(url_for('login'))
#     login_user(registered_user)
#     flash('Logged in successfully')
#     return redirect(request.args.get('next') or url_for('appman'))


# # request handlers -- these two hooks are provided by flask and we will use them
# # to create and tear down a database connection on each request.  peewee will do
# # this for us, but its generally a good idea to be explicit.
# @app.before_request
# def before_request():
#     g.db = database
#     g.db.connect()


# @app.after_request
# def after_request(response):
#     g.db.close()
#     return response


# @app.route('/')
# def welcome():
#     return 'Hello World!'


# @app.route('/api/v1/apps')
# def appApi():
#     return jsonify(**{"apps": [a.toDic() for a in Application.select()]})


# @app.route('/apps/')
# @login_required
# def appwww():
#     Model.hostname = request.host_url
#     return render_template('apps.html', apps=[a.toDic() for a in Application.select()])


# @app.route('/env')
# def env():
#     return os.environ.get("VCAP_SERVICES", "{}")


# #
# #{
# #  "client": "Cityrama",
# #  "latest_releases": {
# #    "dev": {
# #      "release_notes": "qtydgbe\\ndjaks",
# #      "url": "http://example.com/4b-4.apk",
# #      "version": "0.1.1 (4)"
# #    },
# #    "prod": {
# #      "release_notes": "qtydgbe\\ndjaks\\n PROD",
# #      "url": "http://example.com/4b-4.apk",
# #      "version": "0.1.1 (4)"
# #    }
# #  },
# #  "name": "4Booking",
# #  "platform": "android"
# #}
# #

# @app.route('/api/v1/<app>', methods=["GET"])
# @app.route('/<app>/', methods=["GET"])
# def getApp(app):
#     try:
#         a = Application.get(machine_name=app)
#         return jsonify(**a.toDic())
#     except Exception, e:
#         raise e, 404


# #
# # POST
# #
# @app.route('/api/v1/<app>/', methods=["POST", "PUT"])
# @app.route('/<app>/', methods=["POST", "PUT"])
# def addApp(app):
#     try:
#         app = Application.get(machine_name=app)
#         return "Already exists.", 403
#     except:
#         n = request.form["name"]
#         c = request.form["client"]
#         p = request.form["platform"]

#         return jsonify(**Application.create(machine_name=app, name=n, client=c, platform=p).toDic())


# @app.route('/api/v1/<app>/carlos.fonseca@beware.pt', methods=["DELETE"])
# def deleteApp(app):
#     try:
#         app = Application.get(machine_name=app)
#     except:
#         return "App doesn't exist", 404

#     delete_query = Release.delete().where(Release.application == app)
#     delrel = delete_query.execute()

#     if app.delete_instance() == 1:
#         return "Ok."
#     return "Error", 500


# #
# # POST
# #
# @app.route('/api/v1/<app>/<channel>', methods=["POST", "PUT"])
# @app.route('/<app>/<channel>', methods=["POST", "PUT"])
# def addRelease(app, channel):
#     app = Application.get(machine_name=app)
#     if not app:
#         return "Not an app", 404
#         #app4B.new_release("0.1.0 (2)", "dev", "http://example.com/4b-2.apk", "New feature X\nBug fixes")

#     v = request.form["version"]
#     u = request.form["url"]
#     n = request.form["release_notes"]

#     try:
#         release = app.new_release(v, channel, u, n)
#         if not release:
#             return "Error occurred", 403
#         return jsonify(**release.toDic())
#     except Exception, e:
#         return str(e), 400


# @app.route('/api/v1/<app>/<channel>/download')
# @app.route('/<app>/<channel>/download')
# def download(app, channel):
#     #try:
#     application = Application.get(machine_name=app)
#     return redirect(application.latest_release(channel).url)
#     #except:
#     #    return "Error"


# #{
# #  "latest_version": "0.1.1 (4)",
# #  "release_notes": "qtydgbe\\ndjaks",
# #  "url": "http://example.com/4b-4.apk"
# #}
# @app.route('/api/v1/<app>/releases/latest/<channel>')
# @app.route('/api/v1/<app>/<channel>')
# @app.route('/<app>/releases/latest/<channel>')
# @app.route('/<app>/<channel>')
# def latest_version(app, channel):
#     app = Application.get(machine_name=app)
#     if not app:
#         return "Not an app", 404

#     return jsonify(**app.latest_release(channel).toDic())


# @app.route('/api/v1/reset/carlos.fonseca.beware.pt')
# def reset():
#     Release.drop_table()
#     Application.drop_table()
#     User.drop_table()
#     create_tables()
#     return "Done."

# @app.route('/api/v1/updatetables/carlos.fonseca.beware.pt')
# def updateDB():
#     create_tables()
#     return "Done."



# #
# #{
# #  "dev": [
# #    {
# #      "latest_version": "0.1.1 (4)",
# #      "release_notes": "qtydgbe\\ndjaks",
# #      "url": "http://example.com/4b-4.apk"
# #    },
# #    {
# #      "latest_version": "0.1.1 (3)",
# #      "release_notes": "qtydgbe\\ndjaks",
# #      "url": "http://example.com/4b-3.apk"
# #    }
# #  ],
# #  "prod": [
# #    {
# #      "latest_version": "0.1.1 (4)",
# #      "release_notes": "qtydgbe\\ndjaks\\n PROD",
# #      "url": "http://example.com/4b-4.apk"
# #    }
# #  ]
# #}
# #
# @app.route('/api/v1/<app>/releases/')
# @app.route('/<app>/releases/')
# def list_app_releases(app):
#     app = Application.get(machine_name=app)
#     if not app:
#         return "Not an app", 404

#     return jsonify(**app.sortedReleasesDic(latest=False))


# @app.route('/api/v1/<app>/releases/<channel>')
# def list_app_releases_for_channel(app, channel):
#     app = Application.get(machine_name=app)
#     if not app:
#         return "Not an app", 404

#     return jsonify(**app.sortedReleasesDic(channel=channel, latest=False))


# #{
# #  "dev": {
# #    "latest_version": "0.1.1 (4)",
# #    "release_notes": "qtydgbe\\ndjaks",
# #    "url": "http://example.com/4b-4.apk"
# #  },
# #  "prod": {
# #    "latest_version": "0.1.1 (4)",
# #    "release_notes": "qtydgbe\\ndjaks\\n PROD",
# #    "url": "http://example.com/4b-4.apk"
# #  }
# #}

# @app.route('/api/v1/<app>/releases/latest/')
# @app.route('/<app>/releases/latest/')
# def list_latest_app_releases(app):
#     app = Application.get(machine_name=app)
#     if not app:
#         return "Not an app", 404

#     return jsonify(**app.sortedReleasesDic(True))


# @app.route('/api/v1/mail/<app>/<channel>/', methods=["POST"])
# @app.route('/api/v1/mail/<app>/<channel>/<version>/', methods=["POST"])
# def mail_release(app, channel, version=None):
#     to = request.form["to"]
#     frm = request.form["from"]

#     app = Application.get(machine_name=app)
#     if not app:
#         return "Not an app", 404

#     if version is not None:
#         return "not implemented", 500

#     release = app.latest_release(channel)

#     if release is None:
#         return "Not a channel", 404

#     appname = app.name
#     version = release.version
#     release_notes = release.release_notes
#     url = release.url
#     if channel == "prod": channel = ""

#     subject = "%s %s %s is now available" % (appname, version, channel)

#     plaintext = "%s %s %s\n\n\nWhat's new in this build:\n\n%s\n\nInstall:\n%s\n\n\nPowered by Beware App Manager" % \
#                 (appname, version, channel, release_notes, url)

#     htmltxt = render_template('mail.html', appname=appname, version=version, release_notes=release_notes, url=url)

#     #return plaintext
#     #return htmltxt
#     mail.send_mail(to, frm, subject, plaintext, htmltxt)
#     return "OK"

# @app.route('/api/v1/mailmultiple', methods=["POST"])
# def mail_release_multiple():
#     if "to" not in request.form:
#         return "'to' is missing."
#     if "from" not in request.form:
#         return "'from' is missing."
#     to = request.form["to"]
#     if "apps" not in request.form:
#         return "'apps' is missing."
#     if "channel" not in request.form:
#         return "'channel' is missing."
#     to = request.form["to"]
#     frm = request.form["from"]
#     appNames = re.split("[^a-zA-Z0-9._]+", request.form["apps"])
#     channel = request.form["channel"]

#     apps = []

#     for app in appNames:

#         try:
#             app = Application.get(machine_name=app)
#         except:
#             return "Not an app: "+app, 404

#         release = app.latest_release(channel)

#         if release is None:
#             return "Not a channel", 404

#         appname = app.name
#         version = release.version
#         release_notes = release.release_notes
#         url = release.url
#         if channel == "prod": channel = ""

#         apps.append({"name":appname, "version":version, "url":url, "channel":channel})

#     print(apps)

#     appsStr = ", ".join([app["name"]+" "+app["version"] for app in apps])
#     subject = "%s %s now available." % (appsStr, "is" if len(apps) == 1 else "are")
#     # subject = "%s %s %s is now available" % (appname, version, channel)

#     plaintext = "\n\n".join(["%s %s\n  %s" % (app["name"],app["version"],app["url"]) for app in apps])

#     plaintext += "\n\n\nRelease Notes:\n\n%ss\n\n\nPowered by Beware App Manager\nhttp://beware.pt" % release_notes

#     htmltxt = render_template('mailm.html', apps=apps, release_notes=release_notes)

#     #return plaintext
#     #return htmltxt
#     mail.send_mail(to, frm, subject, plaintext, htmltxt)
#     return "OK"


# @app.route('/api/v1/slackbot/<app>/<channel>/<slackchannel>') # ?releasenotes
# def slackbot(app, channel, slackchannel, version=None):
#     app = Application.get(machine_name=app)
#     if not app:
#         return "Not an app", 404

#     if version is not None:
#         return "not implemented", 500

#     release = app.latest_release(channel)

#     if release is None:
#         return "Not a channel", 404

#     appname = app.name
#     version = release.version
#     release_notes = release.release_notes
#     url = release.url  # "%sd/%s" % (request.url_root, release.url.rsplit('/',1)[1])

#     if channel == "prod":
#         channel = ""
#     else:
#         channel = " on the _" + channel + "_ channel"

#     #slackurl = 'https://beware.slack.com/services/hooks/slackbot?token=ReAe4bznlc2GPREyVtHFZUK0&channel=%23' + slackchannel
#     #x = requests.post(slackurl, data=">\n:triangular_flag_on_post: %s *%s* %s%s: %s" % (
#         #":android:" if app.platform == "android" else "", appname, version, "", url)).status_code

#     slackurl = 'https://card4b.slack.com/services/hooks/incoming-webhook?token=UyiGLqMlF78r0k475PXgoe8m'

#     payload = {
#         "channel":"#"+slackchannel,
#         "username":u"%s   %s - New Release" % (appname, "Android" if app.platform == "android" else u""),
#         "icon_url":"https://cld.pt/dl/download/2d92e7f4-c1a4-449e-bb38-69d86511442b/APKs/"+app.machine_name+".png?"+time.strftime("%Y%m%d"),
#         "text": "%s %s" % (version, url)
#     }

#     if "releasenotes" in request.args:
#         payload["attachments"]= [{
#                                     "fallback": "",
#                                     "color": "good",
#                                     "fields": [{
#                                         "value": release_notes,
#                                         "short": False
#                                     }]
#                                 }];


#     data = {"payload":json.dumps(payload)}

#     print(json.dumps(data, indent=2))

#     x = requests.post(slackurl, data=data).status_code

#     if x >= 400:
#         return str(x)+": Post to Slack Failed"
#     else:
#         return redirect("/apps")


# @app.route("/api/v1/plist/<app>-<channel>.plist")
# def plist(app, channel):
#     application = Application.get(machine_name=app)
#     if application:
#         release = application.latest_release(channel)
#         if release:
#             return render_template("ios.plist", name=application.name, url=release.url, version=release.version,
#                                    identifier=app)
#     return "Error", 400


# @app.route('/d/<filename>')
# def directdownload(filename):
#     url = Release.expand_url("%/" + filename)
#     if url:
#         return redirect(url)
#     else:
#         return "Not found", 404


# @app.route('/m/')
# def mobile():
#     return render_template('mobile.html', apps=[a.toDic() for a in Application.select()])

# @app.route('/appman/')
# def appman():
#     return render_template('appman.html', apps=[a.toDic() for a in Application.select()])

# @app.route('/appman/<app>')
# def singleappman(app):
#     return render_template('app.html', app=Application.get(machine_name = app).toDic())


# @app.route('/robots.txt')
# def robots():
#     return Response(render_template("robots.txt"), mimetype='text/txt')


# allow running from the command line
if __name__ == '__main__':
    app.run()
