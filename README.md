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
| [**API Gateway**](https://github.com/amankrmj09/bakery_api_gateway) | Central routing, authentication, and request filtering. |
| [**Auth Service**](https://github.com/amankrmj09/bakery_auth_service) | User authentication, authorization, Admin Analytics, and Global Store Settings. |
| [**Cart Service**](https://github.com/amankrmj09/bakery_cart_service) | Shopping cart handling, session management, totals calculation, and automated maintenance. |
| [**Engagement Service**](https://github.com/amankrmj09/bakery_engagement_service) | Customer testimonials, community feedbacks, curation, and Elasticsearch indexing. |
| [**Eureka Server**](https://github.com/amankrmj09/bakery_eureka_server) | Service registry and discovery for dynamic microservice location. |
| [**Notification Service**](https://github.com/amankrmj09/bakery_notification_service) | Multi-channel notifications via Brevo and Kafka event-driven broadcasting. |
| [**Order Service**](https://github.com/amankrmj09/bakery_order_service) | Order processing, status updates, history management, and Kafka event publishing. |
| [**Payment Service**](https://github.com/amankrmj09/bakery_payment_service) | Payment processing, third-party gateway integration, and internal stats syncing. |
| [**Product Service**](https://github.com/amankrmj09/bakery_product_service) | Product catalogue, pricing, stock management, R2 storage uploads, and advanced search. |
| **Common Modules** | Modularized shared libraries ([`core`](https://github.com/amankrmj09/bakery_common_core), [`messaging`](https://github.com/amankrmj09/bakery_common_messaging), [`security`](https://github.com/amankrmj09/bakery_common_security), [`feign`](https://github.com/amankrmj09/bakery_common_feign)) containing DTOs, Kafka event models, security filters, and clients. |
| [**Config Server**](https://github.com/amankrmj09/bakery-config-servers) | Centralized configuration management for all services. |
| [**Config Repo**](https://github.com/amankrmj09/bakery-config-repo) | Backing Git repository for configuration properties. |
| [**ReactJS Admin Site**](https://github.com/amankrmj09/Blu_s_Bakery) | The admin-facing web application interface. |
| [**ReactJS User Site**](https://github.com/amankrmj09/Blu_s_Bakery) | The customer-facing web application interface. |

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

3. **Start the Infrastructure Components:**
   Spin up the required databases and infrastructure using the provided Docker Compose files.
   ```bash
   docker-compose -f docker-compose-postgresql.yml up -d
   docker-compose -f docker-compose-mongodb.yml up -d
   docker-compose -f docker-compose-redis.yml up -d
   docker-compose -f docker-compose-kafka.yml up -d
   docker-compose -f docker-compose-elasticsearch.yml up -d
   ```
   *(Note: Ensure infrastructure is fully running before starting the microservices via your IDE or wrapper scripts.)*

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
├── bakery_engagement_service/ # Customer testimonials, feedbacks, and admin curation
├── bakery_eureka_server/      # Service discovery server 
├── bakery_notification_service/# Notifications, templates and campaigns 
├── bakery_order_service/      # Order processing & lifecycle 
├── bakery_payment_service/    # Payment gateway integration 
├── bakery_product_service/    # Product catalogue management
├── bakery_common_core/        # Shared core library and DTOs
├── bakery_common_feign/       # Shared Feign clients
├── bakery_common_messaging/   # Shared Kafka event models
├── bakery_common_security/    # Shared security configurations
├── config-repo/               # Centralized configuration properties
├── config-server/             # Spring Cloud Config server
└── reactjs/                   # Frontend applications
    ├── bakery-admin/          # Admin Portal
    └── bakery-user/           # User Portal
```

---

## ✨ Recent Updates

We've been hard at work improving the platform! Recent enhancements include:
- **Security & Access:** Implemented OTP sign-in for the Admin portal and improved admin registration workflows.
- **Frontend Enhancements:** Implemented SEO strategies in React, added product page parallax effects, and improved overall UI/UX components.
- **Microservices Robustness:** Standardized logging using SLF4J, implemented centralized environment variable configurations, and improved error handling.
- **Order & Payments:** Fixed COD payment workflows and updated admin management panel visibility for delivered orders.

---

## 🎯 Next Steps & Roadmap

- **Comprehensive Testing:** Implement extensive unit, integration, and end-to-end (E2E) testing across all microservices and frontend applications to ensure high reliability.
- **Promotions & Engagement:** Develop dynamic features for combo offers and daily deals to boost customer engagement and sales.
- **Observability Integration:** Implement comprehensive metrics monitoring and distributed tracing using **Prometheus and Grafana** across all microservices.

---

## 🎬 Video Showcase

Get a feel for the platform through these walkthrough videos covering the full user and admin experience.

### 👤 User Journey

| # | Title | Description | Watch |
|---|---|---|---|
| 01 | 🏠 Home Page Tour | Overview of the landing page, featured products, and offer banners. | [▶️ Watch](https://github.com/amankrmj09/Blu_s_Bakery/raw/main/.github/assets/01_home_page_tour.mp4) |
| 02 | 📝 Registering a New Account | Step-by-step new user registration flow. | [▶️ Watch](https://github.com/amankrmj09/Blu_s_Bakery/raw/main/.github/assets/02_register_new_account.mp4) |
| 03 | 🔐 Logging In | Logging into the platform with user credentials. | [▶️ Watch](https://github.com/amankrmj09/Blu_s_Bakery/raw/main/.github/assets/03_user_login.mp4) |
| 04 | 🛍️ Shop Page Tour | Browsing the product catalogue, filters, and search. | [▶️ Watch](https://github.com/amankrmj09/Blu_s_Bakery/raw/main/.github/assets/04_shop_page_tour.mp4) |
| 05 | 🧁 Product Details Tour | Exploring an individual product's detail page. | [▶️ Watch](https://github.com/amankrmj09/Blu_s_Bakery/raw/main/.github/assets/05_product_details_tour.mp4) |
| 06 | 🛒 Buying Products | Adding to cart and completing a full purchase. | [▶️ Watch](https://github.com/amankrmj09/Blu_s_Bakery/raw/main/.github/assets/06_buying_products.mp4) |
| 07 | 🏷️ Applying a Coupon & Checkout | Copying a coupon from the home page offer banner and applying it at checkout. | [▶️ Watch](https://github.com/amankrmj09/Blu_s_Bakery/raw/main/.github/assets/07_applying_coupon_and_checkout.mp4) |
| 08 | 📬 Contact Page Tour | Navigating the contact and customer support page. | [▶️ Watch](https://github.com/amankrmj09/Blu_s_Bakery/raw/main/.github/assets/08_contact_page_tour.mp4) |
| 09 | 👤 Managing Profile & Adding Address | Updating profile info and adding a saved delivery address. | [▶️ Watch](https://github.com/amankrmj09/Blu_s_Bakery/raw/main/.github/assets/09_profile_and_adding_address.mp4) |

### 🖥️ Admin Operations

| # | Title | Description | Watch |
|---|---|---|---|
| 10 | 🖥️ Admin Portal Tour | Full walkthrough of the admin dashboard and its management features. | [▶️ Watch](https://github.com/amankrmj09/Blu_s_Bakery/raw/main/.github/assets/10_admin_site_tour.mp4) |
| 11 | 📂 Adding a Category | How an admin creates and publishes a new product category. | [▶️ Watch](https://github.com/amankrmj09/Blu_s_Bakery/raw/main/.github/assets/11_admin_add_category.mp4) |
| 12 | 📦 Adding a Product | How an admin creates, configures, and publishes a new product listing. | [▶️ Watch](https://github.com/amankrmj09/Blu_s_Bakery/raw/main/.github/assets/12_admin_add_product.mp4) |

---

## 🎬 Video Showcase

Get a feel for the platform through these walkthrough demos covering the full user and admin experience.

### 👤 User Journey

| 🏠 Home Page Tour | 📝 Registering a New Account |
|---|---|
| ![Home Page Tour](.github/assets/01_home_page_tour.gif) | ![Registering a New Account](.github/assets/02_register_new_account.gif) |

| 🔐 Logging In | 🛍️ Shop Page Tour |
|---|---|
| ![Logging In](.github/assets/03_user_login.gif) | ![Shop Page Tour](.github/assets/04_shop_page_tour.gif) |

| 🧁 Product Details Tour | 🛒 Buying Products |
|---|---|
| ![Product Details Tour](.github/assets/05_product_details_tour.gif) | ![Buying Products](.github/assets/06_buying_products.gif) |

| 🏷️ Applying a Coupon & Checkout | 📬 Contact Page Tour |
|---|---|
| ![Applying a Coupon & Checkout](.github/assets/07_applying_coupon_and_checkout.gif) | ![Contact Page Tour](.github/assets/08_contact_page_tour.gif) |

| 👤 Managing Profile & Adding Address |
|---|
| ![Managing Profile & Adding Address](.github/assets/09_profile_and_adding_address.gif) |

---

### 🖥️ Admin Operations

| 🖥️ Admin Portal Tour |
|---|
| ![Admin Portal Tour](.github/assets/10_admin_site_tour.gif) |

| 📂 Adding a Category | 📦 Adding a Product |
|---|---|
| ![Adding a Category](.github/assets/11_admin_add_category.gif) | ![Adding a Product](.github/assets/12_admin_add_product.gif) |

---

## 📄 License

This project is licensed under the MIT License.

---
*Stay tuned as we roll out new features to make Blu'sBakery more responsive and intelligent!*
