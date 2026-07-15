# 🧁 Blu'sBakery Microservice Platform

![Java](https://img.shields.io/badge/Java-21%2B-orange.svg)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.x-brightgreen.svg)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)
![React](https://img.shields.io/badge/React-Frontend-61DAFB.svg?logo=react)

Welcome to the **Blu'sBakery Microservice Platform**! This platform provides an integrated, highly scalable, and robust system specifically designed for managing modern bakery operations.

Modern bakeries face numerous challenges: managing perishable inventory, coordinating complex orders, engaging customers with timely notifications, and ensuring smooth payment and delivery workflows. Our domain-driven microservice architecture offers a flexible solution to meet these needs efficiently.

---

## 🏗️ Architecture & Core Microservices

The platform follows microservice architectural principles. Services communicate over REST APIs and are built using the **Spring Boot** and **Spring Cloud** stack. 

### 🧩 Services Overview

| Service | Purpose |
|---------|---------|
| **API Gateway** | Central routing, authentication, and request filtering. |
| **Auth Service** | User authentication, authorization, Admin Analytics, and Global Store Settings. |
| **Cart Service** | Shopping cart handling, session management, totals calculation, and automated maintenance. |
| **Eureka Server** | Service registry and discovery for dynamic microservice location. |
| **Notification Service** | Multi-channel notifications via Brevo and Kafka event-driven broadcasting. |
| **Order Service** | Order processing, status updates, history management, and Kafka event publishing. |
| **Payment Service** | Payment processing, third-party gateway integration, and internal stats syncing. |
| **Product Service** | Product catalogue, pricing, stock management, R2 storage uploads, and advanced search. |
| **Common Libs** | Shared libraries, DTOs, Kafka event models, and shared security/Feign configurations. |
| **Config Server** | Centralized configuration management for all services. |
| **Config Repo** | Backing Git repository for configuration properties. |
| **ReactJS Frontend** | The customer-facing web application interface (Admin and User portals). |

---

## 🛠️ Tech Stack

- **Backend:** Spring Boot, Spring Cloud (Eureka, OpenFeign, Config)
- **Security:** Spring Security (OAuth2 / JWT)
- **Database & Storage:** PostgreSQL (Spring Data JPA), MongoDB, Elasticsearch, Cloudflare R2 / S3
- **Caching & Session:** Redis
- **Messaging & Eventing:** Apache Kafka (Event-Driven Processing), Brevo (Email & SMS)
- **Observability:** Spring Boot Actuator, Swagger / OpenAPI
- **Testing:** JUnit 5, Testcontainers
- **Infrastructure:** Docker, Docker Compose
- **Frontend:** ReactJS

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:
- [Java 21+](https://adoptium.net/)
- [Docker](https://www.docker.com/) & Docker Compose
- [Node.js](https://nodejs.org/) (for the React frontend)
- [Gradle](https://gradle.org/) (optional, included via wrapper)

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone --recursive https://github.com/amankrmj09/bakery.git
   cd bakery
   ```

2. **Configure Environment:**
   Update the application configurations (e.g., database credentials, third-party API keys) inside the `config-repo` or individual service `application.yml` files.

3. **Start the Infrastructure & Services:**
   We recommend using Docker Compose to spin up the required databases and services.
   ```bash
   docker-compose -f docker-compose.infra.yml up -d
   docker-compose -f docker-compose.services.yml up -d
   ```

4. **Access the Platform:**
   - **API Gateway:** `http://localhost:8080` (Central entry point)
   - **Service Discovery (Eureka):** `http://localhost:8761`
   - **React Frontend:** `http://localhost:3000`
   - **Swagger UI:** Accessible via the API Gateway endpoints.

---

## 📁 Repository Structure

```text
bakery/ 
├── bakery_api_gateway/        # API Gateway routing and security 
├── bakery_auth_service/       # User auth 
├── bakery_cart_service/       # Shopping and session cart 
├── bakery_eureka_server/      # Service discovery server 
├── bakery_notification_service/# Notifications, templates and campaigns 
├── bakery_order_service/      # Order processing & lifecycle 
├── bakery_payment_service/    # Payment gateway integration 
├── bakery_product_service/    # Product catalogue management
├── common-libs/               # Shared code and utilities
├── config-repo/               # Centralized configuration properties
├── config-server/             # Spring Cloud Config server
└── reactjs/                   # Frontend applications
    ├── bakery-admin/          # Admin Portal
    └── bakery-user/           # User Portal
```

---

## 🎯 Next Steps & Roadmap

- **Observability Integration:** Implement comprehensive metrics monitoring and distributed tracing using **Prometheus and Grafana** across all microservices.

---

## 📄 License

This project is licensed under the MIT License.

---
*Stay tuned as we roll out new features to make Blu'sBakery more responsive and intelligent!*
