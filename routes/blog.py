from bottle import get, post, template, abort, request, redirect
from data.database import add_post, get_all_posts, get_post_by_id, update_post, delete_post

# Read (list)
@get('/blog')
def post_list():
    context = {
        'active': 'blog'
    }
    posts = get_all_posts()
    return template('blog.html', posts=posts, **context)

# Read (detail)
@get('/blog/<post_id>')
def post_detail(post_id):
    post_by_id = get_post_by_id(post_id)
    if post_by_id:
        return template('post.html', post=post_by_id)
    else:
        return abort(404, f'Post {post_id} cannot be found')

# Create
# Update
@get('/blog/post-form')
@get('/blog/post-form/<post_id>')
def post_form(post_id=None):
    context = {
        'active': 'post-form'
    }
    if post_id:
        post_by_id = get_post_by_id(post_id)
        if post_by_id:
            return template('post-form.html', post=post_by_id, **context)
        else:
            abort(404, f'Post {post_id} cannot be found')
    else:
        return template('post-form.html', post=None, **context)

# Create
# Update
@post('/blog/post-form')
@post('/blog/post-form/<post_id>')
def post_form_submit(post_id=None):
    if post_id:
        updated_post = (request.forms.postTitle, )
        update_post(post_id, updated_post)
    else:
        new_post = (request.forms.postTitle, )
        post_id = add_post(new_post)

    return redirect(f'/blog/{post_id}')

# Delete
@post('/blog/post-delete/<post_id>')
def post_delete(post_id):
    delete_post(post_id)
    return redirect('/blog')