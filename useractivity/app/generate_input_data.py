import random
import string
import uuid
import JsonResponse


def user_data_generation(request):
    res = []
    for i in range(0, 10):
        first_name = ''.join(random.choices(string.ascii_uppercase, k=1) + random.choices(string.ascii_lowercase, k=int(
            random.choices(string.digits, k=1)[0])))
        last_name = ''.join(random.choices(string.ascii_uppercase, k=1) + random.choices(string.ascii_lowercase, k=int(
            random.choices(string.digits, k=1)[0])))
        name = dict({"id": uuid.uuid4().hex[:9].upper(), "first_name": first_name, "last_name": last_name})
        res.append(dict({"model": "app.users", "fields": name}))
    return JsonResponse({'members': res})


f = open("dataset.json", "w")
f.write(str(user_data_generation()))
f.close()
