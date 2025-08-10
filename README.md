# 🧠 vLLM Multi-Concurrent Chatbot with FastAPI UI

This project is a lightweight, production-ready chatbot interface powered by the [vLLM inference engine](https://github.com/vllm-project/vllm). It supports multi-concurrent generation and runs the backend and frontend as separate Docker containers.

---

## 📦 Project Structure

```
.
├── vllm/           # vLLM backend for fast LLM inference
│   └── Dockerfile
├── ui/                # FastAPI-based UI service
│   └── Dockerfile
├── TinyLlama-1.1B-Chat-v1.0/ # HuggingFace model directory
├── docker-compose.yml
├── ui-deployment.yaml # Kubernetes deployment for UI
├── ui-service.yaml # Kubernetes service for UI
├── vllm-deployment.yaml # Kubernetes deployment for vLLM
├── vllm-service.yaml # Kubernetes service for vLLM
└── README.md
```

## 🚀 Features

- 🔁 Multi-concurrency support with vLLM engine  
- ⚡ GPU acceleration (if available)  
- 🔌 Modular: UI and backend run as separate containers  
- 🐳 Dockerized for local or production use
- 🐳 Fully Dockerized (Docker Compose)  
- ☸️ Kubernetes deployment ready  

## 🛠️ Requirements

- Docker + Docker Compose  
- Optional: NVIDIA GPU with drivers (`nvidia-smi` working and watch -n0.1 nvidia-smi for continous usage display)  
- (For GPU use) [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)  
- (For K8s use) A working Kubernetes cluste 

## 🧪 Quickstart with Docker Compose

Clone the repo:

```bash
git clone https://github.com/your-org/Multi_Concurrent_ChatBot_using_vLLM.git
cd Multi_Concurrent_ChatBot_using_vLLM
```

Update the model path (if needed) in `docker-compose.yml`:

```yaml
volumes:
   - ./TinyLlama-1.1B-Chat-v1.0:/app/models
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
1 - Deploy the backend:
```
kubectl apply -f vllm-deployment.yaml
kubectl apply -f vllm-service.yaml
```
2 - Deploy the UI:
```
kubectl apply -f ui-deployment.yaml
kubectl apply -f ui-service.yaml
```
3 - (Optional) Use gpu-operator.yaml for GPU support if needed.

Make sure all Pods are running:

```
kubectl get pods

```


## 🧼 Cleanup

```bash
docker compose down
# or for Kubernetes
kubectl delete -f .
```

---

## 👨‍💻 Author

Chinmay @ Cognisyn Labs  
🔬 https://cognisynlabs.com/
chinmayatcognisynlabs@gmail.com

---

## 🧪 License

MIT License
