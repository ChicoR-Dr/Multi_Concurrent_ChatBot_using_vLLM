# 🧠 vLLM Multi-Concurrent Chatbot with FastAPI UI

This project is a lightweight, production-ready chatbot interface powered by the [vLLM inference engine](https://github.com/vllm-project/vllm). It supports multi-concurrent generation and runs the backend and frontend as separate Docker containers.

---

## 📦 Project Structure

```
.
├── backend/           # vLLM backend for fast LLM inference
│   └── Dockerfile
├── ui/                # FastAPI-based UI service
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🚀 Features

- 🔁 Multi-concurrency support with vLLM engine  
- ⚡ GPU acceleration (if available)  
- 🔌 Modular: UI and backend run as separate containers  
- 🐳 Dockerized for local or production use  

## 🛠️ Requirements

- Docker + Docker Compose  
- Optional: NVIDIA GPU with drivers (`nvidia-smi` working)  
- (For GPU use) NVIDIA Container Toolkit  

## 🧪 Quickstart with Docker Compose

Clone the repo:

```bash
git clone https://github.com/your-org/Simple_LLM_ChatBot_using_vLLM.git
cd Simple_LLM_ChatBot_using_vLLM
```

Update the model path (if needed) in `docker-compose.yml`:

```yaml
volumes:
  - ./models:/app/models
```

Launch both UI and backend:

```bash
docker compose up --build
```

Access the chatbot UI:

Open your browser and go to http://localhost:7860

## 🐳 Docker Compose Overview

```yaml
services:
  vllm-backend:
    image: chinmay555/vllm:latest
    ports:
      - 8000:8000

  fastapi-ui:
    image: chinmay555/chat-ui:latest
    ports:
      - 7860:7860
```

## ⚙️ Environment Variables

You can configure the following via `.env` or hardcode in `docker-compose.yml`:

- `MODEL_PATH`: Path to your HF model (e.g., TinyLlama/TinyLlama-1.1B-Chat)  
- `PORT`: Backend port (default: 8000)  

## 🧑‍💻 API Usage

The FastAPI backend serves standard endpoints like:

```bash
POST /generate
GET  /health
```

To test:

```bash
curl -X POST http://localhost:8000/generate -d '{"prompt": "Tell me a joke"}'
```

## ☸️ (Optional) Kubernetes Deployment

If you'd like to run this stack on Kubernetes instead of Docker Compose, you can use the following files:

- `vllm-deployment.yaml`
- `ui-service.yaml`
- `gpu-operator.yaml` (for GPU support)

Use `kubectl apply -f` to deploy each one.

## 🧼 Cleanup

```bash
docker compose down
```

## 📜 License

MIT License. See `LICENSE`.

## 🙋‍♀️ Questions?

Feel free to open an issue or reach out at [your-email@example.com].
