# encoding=utf8
__author__ = 'wcong'
import web
import pdbc
import config
import util


urls = (
    '/', 'Index',
    '/write', 'Write'
)


class Index:
    def GET(self):
        ridicule_id = web.input().get('id')
        ridicule = pdbc.Ridicule.select_by_id(ridicule_id)
        like_list = pdbc.Like.select_by_ridicule_id(ridicule_id)
        comment_list = pdbc.Comment.select_by_ridicule_id(ridicule_id)
        data = dict()
        data['ridicule'] = ridicule
        data['like_list'] = like_list
        data['like_num'] = len(like_list)
        data['comment_list'] = comment_list
        data['comment_num'] = len(comment_list)
        return config.render.ridicule(data)


class Write:
    def GET(self):
        return config.render.write_ridicule()

    def POST(self):
        email = util.get_user_email()
        user_id = pdbc.User.select_id_by_email(email)
        ridicule = web.input().get("ridicule")
        pdbc.Ridicule.insert(user_id, ridicule)
        web.seeother('../my/')


app_ridicule = web.application(urls, locals())