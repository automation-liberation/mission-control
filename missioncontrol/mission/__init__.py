import time

import requests

from missioncontrol import celery
from missioncontrol.mission.models import Mission, MissionStep


@celery.task
def start(mission_id):
    mission = Mission.objects(id=mission_id).first()
    steps = MissionStep.objects.filter(mission=mission).order_by("order")
    for step in steps:
        requests.get(f"http://localhost:5000/tellocontrol/control/{step.command}")
        if step.sleep:
            time.sleep(step.sleep)


@celery.task
def create(mission_data):
    mission_info = mission_data.get('mission')
    if not mission_info:
        return {"msg": f"Something went wrong"}
    mission = Mission.objects(**mission_info).first()
    if mission:
        return {"msg": f"Mission {mission.name} for drone {mission.drone} already exists"}
    mission = Mission(**mission_data.get('mission'))
    mission.save()

    for idx, step in enumerate(mission_data.get('steps')):
        step = MissionStep(mission=mission, order=idx+1, command=step.get('command'), sleep=step.get('sleep'))
        step.save()

    return {"msg": f"Mission {mission.name} created"}


@celery.task
def get_all_missions():
    missions = Mission.objects
    return {"missions": [{"name": mission.name, "id": str(mission.id)} for mission in missions]}
