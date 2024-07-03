# MyBlog Project

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose

### Steps to Run the Project

1. Clone the repository:
    ```bash
    git clone https://github.com/lakxpro/myblog
    cd yourrepository
    ```

2. Build and start the Docker containers:
    ```bash
    docker-compose build
    docker-compose up -d
    ```

3. Create superuser:
    ```bash
    docker-compose exec app /bin/bash
    ```

4. Upload fixtures data:
    ```bash
    python manage.py loaddata blog/fixtures/tag.json
    python manage.py loaddata blog/fixtures/article.json
    python manage.py loaddata blog/fixtures/articletag.json
    ```

5. Access the application:
    Open your web browser and go to `http://127.0.0.1:8000`.

### Troubleshooting

If you encounter any issues, check the logs:
    ```bash
    docker-compose up
    docker-compose logs app
    docker-compose logs db
    ```

pre-commit install

pyenv virtualenv 3.12.1 myblog-env 