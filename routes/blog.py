from bottle import get, post, template, abort, request, redirect
from data.database import add_post, get_all_posts, get_post_by_id

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
        post_by_id = [post for post in posts if post.id == post_id]
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
    new_post = (request.forms.postTitle, )
    return
    if post_id:
        post_by_id = [post for post in posts if post.id == post_id]
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
    post_by_id = [post for post in posts if post.id == post_id]
    if len(post_by_id) > 0:
        post_index = posts.index(post_by_id[0])
        del posts[post_index]
    else:
        abort(404, f'Post {post_id} cannot be found')
    return redirect('/blog')