auto:
	@echo "making directory for static images"
	@mkdir -p sudopodia/static/images
	@echo "preparing database"
	@./manage.py makemigrations
	@./manage.py migrate
	@echo "creating superuser for testing\nPress ctrl-C if not necessary"
	@./manage.py createsuperuser
	@echo "Done!!!"
