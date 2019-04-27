from bottle import route, run, template, request, post, get, error, static_file, redirect, hook, abort

posts = [
    {
        'id': 1,
        'title': 'Post 1'
    },
    {
        'id': 2,
        'title': 'Post 2'
    }
]


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
    global posts
    post_id = int(post_id)
    if post_id <= len(posts):
        return template('post.html', post=posts[post_id - 1])
    else:
        return abort(404, f'Post {post_id} cannot be found')


@get('/blog/post-form')
@get('/blog/post-form/<post_id>')
def post_form(post_id=None):
    global posts
    if post_id:
        post_id = int(post_id)
        if post_id <= len(posts):
            return template('post-form.html', post=posts[post_id - 1])
        else:
            abort(404, f'Post {post_id} cannot be found')
    else:
        return template('post-form.html', post=None)


@post('/blog/post-form')
@post('/blog/post-form/<post_id>')
def post_form_submit(post_id=None):
    global posts
    if post_id:
        post_id = int(post_id)
        if post_id <= len(posts):
            updated_post = {
                'id': post_id,
                'title': request.forms.postTitle
            }
            posts[post_id - 1] = updated_post
        else:
            abort(404, f'Post {post_id} cannot be found')
    else:
        post_title = request.forms.postTitle
        post_id = len(posts) + 1

        new_post = {
            'id': post_id,
            'title': post_title
        }

        posts.append(new_post)

    return redirect(f'/blog/{post_id}')


@post('/blog/post-delete/<post_id>')
def post_delete(post_id):
    global posts
    post_id = int(post_id)
    if post_id <= len(posts):
        del posts[post_id - 1]
    else:
        abort(404, f'Post {post_id} cannot be found')
    return redirect('/blog')


run(host='localhost', port=8080, debug=True, reloader=True)