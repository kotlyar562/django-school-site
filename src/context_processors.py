from src.accounts.models import User

def get_teachers_photo(request):
    alluser = User.objects.all()
    teachers = []
    for u in alluser:
        if u.photo:
            teachers.append(u)
    return {'teachers_photo': teachers}
