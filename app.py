from bottle import route, run, template, request, post, get, error, static_file, redirect, hook

posts = ['post1', 'post2']


@hook('before_request')
def strip_trailing_slash():
    request.environ['PATH_INFO'] = request.environ['PATH_INFO'].rstrip('/')


@get('/')
def index():
    return template('index.html')


@get('/blog')
def post_list():
    global posts
    return template('blog.html', posts=posts)


@get('/blog/<post_id>')
def post_detail(post_id):
    return f"Details for {post_id}"


@get('/blog/post-form')
@get('/blog/post-form/<post_id>')
def post_form(post_id=None):
    if post_id:
        return template('post-form.html')
    else:
        return template('post-form.html')


@post('/blog/post-form')
@post('/blog/post-form/<post_id>')
def post_form_submit(post_id=None):
    global posts
    if post_id:
        print(f'updated existing post #{post_id}')
    else:
        post_title = request.forms.postTitle
        print(f'created new post: {post_title}')
        posts.append(post_title)
        post_id = 'new_post_id'

    return redirect('/blog/')


@post('/blog/post-delete/<post_id>')
def post_delete(post_id):
    print(f'deleted post using using post id {post_id}')
    return redirect('/blog')


run(host='localhost', port=8080, debug=True, reloader=True)