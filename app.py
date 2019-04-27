from bottle import route, run, template, request, post, get, error, static_file, redirect, hook


@hook('before_request')
def strip_trailing_slash():
    request.environ['PATH_INFO'] = request.environ['PATH_INFO'].rstrip('/')


@get('/')
def index():
    return "Hello World"


@get('/blog')
def post_list():
    return "All Posts"


@get('/blog/<post_id>')
def post_detail(post_id):
    return f"Details for {post_id}"


@get('/blog/post-form')
@get('/blog/post-form/<post_id>')
def post_form(post_id=None):
    if post_id:
        return f"Form to update post {post_id}"
    else:
        return "Form to create new post"


@post('/blog/post-form')
@post('/blog/post-form/<post_id>')
def post_form_submit(post_id=None):
    if post_id:
        print(f'updated existing post #{post_id}')
        pass
    else:
        print('created new post')
        post_id = 'new_post_id'
        pass

    return redirect(f'/blog/{post_id}')


@post('/blog/post-delete/<post_id>')
def post_delete(post_id):
    print(f'deleted post using using post id {post_id}')
    return redirect('/blog')


run(host='localhost', port=8080, debug=True, reloader=True)