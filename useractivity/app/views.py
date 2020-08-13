from django.shortcuts import render
from .models import Users, UserActivity
from django.http import HttpResponse
import json
from collections import OrderedDict


def index(request):
    useractivity = UserActivity.objects.all()
    user = {}
    for i in useractivity:
        user[i.user_id] = Users.objects.filter(id=i.user_id)

    result = OrderedDict()
    members = []
    for i in user:
        t = OrderedDict()
        t["id"] = i.id
        t["real name"] = i.first_name + " " + i.last_name
        ua = UserActivity.objects.filter(user_id=i.id)
        l = []
        for j in ua:
            d = OrderedDict()
            t["time zone"] = str(j.start_time.tzinfo)
            d["start_time"] = str(j.start_time.strftime("%b %d %Y %I:%M %p"))
            d["end_time"] = str(j.end_time.strftime("%b %d %Y %I:%M %p"))
            l.append(d)
        t["activity_periods"] = l
        members.append(t)
    result["ok"] = "true"
    result["members"] = members
    result = OrderedDict(result)

    json_pretty = json.dumps(result, sort_keys=True, indent=4)
    return HttpResponse(json_pretty, content_type="application/json")


