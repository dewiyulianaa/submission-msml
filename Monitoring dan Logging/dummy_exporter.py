from prometheus_client import start_http_server, Summary
import time
import random

REQUEST_TIME = Summary('python_inference_duration_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def simulate_inference():
    time.sleep(random.uniform(0.1, 0.5))

if __name__ == '__main__':
    start_http_server(8000)
    print("Exporter running on http://localhost:8000/metrics")
    while True:
        simulate_inference()
        time.sleep(1)
