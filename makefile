start: app.py
	gunicorn app:app --bind 0.0.0.0:8001 --log-level=DEBUG --reload