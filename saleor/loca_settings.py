ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', '209.97.138.32']

DEBUG = Truey

DATABASES = {
    "default": dj_database_url.config(
        default="postgres://saleor:saleor@localhost:5432/saleor", conn_max_age=600
    )
}
