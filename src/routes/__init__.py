from flask import render_template, session, request

def render(file_name : str, **kwargs) -> str:
    """
        Render a Jinja template, given with a few basis variables
        as context to know better how to render the template.
    """
    values = {
        'logged_in'     :   'user' in session and session['user'] is not None,
        'username'      :   None if 'user' not in session else session['user'],
        'path'          :   request.path
    }
    return render_template(file_name, **values, **kwargs)
