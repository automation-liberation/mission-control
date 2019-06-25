from celery import Celery

from config import Config

celery = Celery('missioncontrol', autofinalize=False)


def create_app():
    """
    Creates and returns a Celery applications.

    :return: Celery application.
    """
    configure_celery()
    return celery


def configure_celery():
    """
    Configures Celery application based on configuration.
    """
    celery.config_from_object(Config)
    celery.autodiscover_tasks(['missioncontrol.mission', ])

    celery.finalize()
