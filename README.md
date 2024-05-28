# Flask Celery Project

This project demonstrates how to integrate Flask with Celery to handle background tasks, schedule periodic tasks, and use Flower for monitoring. 

The project includes Docker configuration to run the application along with Redis, multiple Celery workers, Celery Beat for scheduling, and Flower for monitoring.

## Project Structure

```flask_celery_project/
├── app/
│ ├── init.py
│ ├── celery_utils.py
│ ├── tasks.py
│ └── views.py
├── celery_worker.py
├── Dockerfile
├── requirements.txt
├── docker-compose.yml
└── run.py
```

## Setup and Running the Project

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd flask_celery_project
Build and start the Docker containers:

```shell
docker-compose up --build
```

Access the application and services:

Flask application: http://localhost:5005

Flower monitoring tool: http://localhost:5555
## Usage
### Adding Tasks
To add a task that runs immediately, you can use the /add endpoint.

Example using curl:

```sh
curl -X POST http://localhost:5005/add -H "Content-Type: application/json" -d '{"a": 4, "b": 6}'
```

### Getting Task Results

To get the result of a task, use the /result/<task_id> endpoint.

Example using curl:

```sh
curl http://localhost:5005/result/<task_id>
```
### Scheduling Periodic Tasks
To schedule a periodic task, use the /schedule endpoint.

Example using curl:

```sh
curl -X POST http://localhost:5005/schedule -H "Content-Type: application/json" -d '{"task_name": "task1", "interval": 30.0, "a": 2, "b": 3}'
```

### Removing Scheduled Tasks
To remove a scheduled task, use the /remove_schedule endpoint.

Example using curl:

```sh
curl -X POST http://localhost:5005/remove_schedule -H "Content-Type: application/json" -d '{"task_name": "task1"}'
```

## Project Details
Flask Application (app/__init__.py)
Defines the Flask application and its configuration.

Celery Initialization (app/celery_utils.py)
Initializes the Celery application and integrates it with Flask.

Celery Tasks (app/tasks.py)
Defines the Celery tasks.

Flask Views (app/views.py)
Defines the Flask routes for adding tasks, scheduling tasks, and getting task results.

Celery Worker (celery_worker.py)
Starts the Celery worker.

Docker Configuration
Dockerfile
Defines the Docker image for the Flask application.

docker-compose.yml
Defines the Docker services for the Flask application, Redis, Celery workers, Celery Beat, and Flower.

Monitoring with Flower
Flower provides a real-time web-based monitoring tool for Celery. It is accessible at http://localhost:5555 and shows the status of the Celery workers, tasks, and other metrics.

## Acknowledgements
[Flask]()

[Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)

[Flower](https://flower.readthedocs.io/en/latest/api.html)

[Redis]()
