from celery import Celery

from webapp import create_app
from webapp.news.parsers import habr

flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379/0')


@celery_app.task
def habr_snippets():
    with flask_app.app_context():
        habr.get_news_snippets()


@celery_app.task
def habr_content():
    with flask_app.app_context:
        habr.get_news_content()
