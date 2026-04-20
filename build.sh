# # set -o errexit
# # pip install -r requirements.txt
# # python manage.py collectstatic --no-input
# # python manage.py migrate

# set -o errexit
# pip install -r requirements.txt
# python manage.py collectstatic --no-input
# python manage.py migrate
# python manage.py shell -c "
# from accounts.models import User
# if not User.objects.filter(username='admin').exists():
#     User.objects.create_superuser('admin', 'admin@lms.com', 'Admin@1234', role='teacher', is_class_teacher=True)
#     print('Admin created!')
# else:
#     print('Admin already exists!')
# "

set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input --clear
python manage.py migrate
python manage.py shell -c "
from accounts.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@lms.com', 'Admin@1234', role='teacher', is_class_teacher=True)
    print('Admin created!')
else:
    print('Admin already exists!')
"