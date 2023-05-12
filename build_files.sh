
echo " BUILD START"
python3.9  -m pip install -r requirements.txt
python3.9 manage.py migrate
python3.9 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'sigprae')"
echo " BUILD END"