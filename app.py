from bottle import route, run, template, request, post, get, error, static_file, redirect, hook, abort, SimpleTemplate

posts = [
    {
        'id': '1',
        'title': 'Post 1'
    },
    {
        'id': '2',
        'title': 'Post 2'
    }
]


@hook('before_request')
def strip_trailing_slash():
    request.environ['PATH_INFO'] = request.environ['PATH_INFO'].rstrip('/')


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root="./static")


@get('/')
def index():
    context = {
        'active': 'index'
    }
    return template('index.html', **context)

# Read (list)
@get('/blog')
def post_list():
    global posts
    context = {
        'active': 'blog'
    }
    return template('blog.html', posts=posts, **context)

# Read (detail)
@get('/blog/<post_id>')
def post_detail(post_id):
    global posts
    post_by_id = [post for post in posts if post['id'] == post_id]
    if len(post_by_id) > 0:
        return template('post.html', post=post_by_id[0])
    else:
        return abort(404, f'Post {post_id} cannot be found')

# Create
# Update
@get('/blog/post-form')
@get('/blog/post-form/<post_id>')
def post_form(post_id=None):
    global posts
    context = {
        'active': 'post-form'
    }
    if post_id:
        post_by_id = [post for post in posts if post['id'] == post_id]
        if len(post_by_id) > 0:
            return template('post-form.html', post=post_by_id[0], **context)
        else:
            abort(404, f'Post {post_id} cannot be found')
    else:
        return template('post-form.html', post=None, **context)

# Create
# Update
@post('/blog/post-form')
@post('/blog/post-form/<post_id>')
def post_form_submit(post_id=None):
    global posts
    if post_id:
        post_by_id = [post for post in posts if post['id'] == post_id]
        if len(post_by_id) > 0:
            post_index = posts.index(post_by_id[0])
            updated_post = {
                'id': post_id,
                'title': request.forms.postTitle
            }
            posts[post_index] = updated_post
        else:
            abort(404, f'Post {post_id} cannot be found')
    else:
        post_title = request.forms.postTitle
        post_id = str(len(posts) + 1)

        new_post = {
            'id': post_id,
            'title': post_title
        }

        posts.append(new_post)

    return redirect(f'/blog/{post_id}')

# Delete
@post('/blog/post-delete/<post_id>')
def post_delete(post_id):
    global posts
    post_by_id = [post for post in posts if post['id'] == post_id]
    if len(post_by_id) > 0:
        post_index = posts.index(post_by_id[0])
        del posts[post_index]
    else:
        abort(404, f'Post {post_id} cannot be found')
    return redirect('/blog')


run(host='localhost', port=8080, debug=True, reloader=True)