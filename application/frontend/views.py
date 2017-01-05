from application.frontend import frontend_blueprint as bp

@bp.route('/')
def index():
  return 'Hello World!'
