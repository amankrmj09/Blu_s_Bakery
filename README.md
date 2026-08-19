# 🧁 Blu'sBakery Microservice Platform

![Java](https://img.shields.io/badge/Java-21%2B-orange.svg)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.x-brightgreen.svg)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)
![React](https://img.shields.io/badge/React-Frontend-61DAFB.svg?logo=react)

Welcome to the **Blu'sBakery Microservice Platform**! This platform provides an integrated, highly scalable, and robust system specifically designed for managing modern bakery operations. The entire infrastructure is deployed using **AWS EC2 instances** and managed via **Dokploy**.

Modern bakeries face numerous challenges: managing perishable inventory, coordinating complex orders, engaging customers with timely notifications, and ensuring smooth payment and delivery workflows. Our domain-driven microservice architecture offers a flexible solution to meet these needs efficiently.

---

## 📑 Table of Contents

- [🏗️ Architecture & Core Microservices](#️-architecture--core-microservices)
- [🛠️ Tech Stack](#️-tech-stack)
- [🌟 Key Features](#-key-features)
- [🚀 Getting Started](#-getting-started)
- [📁 Repository Structure](#-repository-structure)
- [✨ Recent Updates](#-recent-updates)
- [🎯 Next Steps & Roadmap](#-next-steps--roadmap)
- [📸 Platform Screenshots](#-platform-screenshots)
  - [👤 User Site](#-user-site)
  - [🖥️ Admin Site](#️-admin-site)
  - [☁️ AWS & Dokploy Deployment](#️-aws--dokploy-deployment)
- [📄 License](#-license)

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

## 🌟 Key Features

- **Microservice Architecture:** Independent, scalable services communicating via REST APIs and Kafka for resilient, event-driven processes.
- **Robust Authentication & Security:** Role-based access control separating administrative functions from customer operations, featuring JWTs and OTP verification.
- **Comprehensive Admin Portal:** Intuitive dashboard for managing products, organizing categories, monitoring inventory, tracking orders, and curating customer reviews.
- **Multi-Channel Notifications:** Asynchronous, template-driven email and SMS notifications triggered across the customer journey.
- **High-Performance Catalog:** Fast and efficient product discovery powered by Elasticsearch with advanced search and filtering.
- **Modern Responsive UI:** Stunning frontend built with ReactJS, featuring glassmorphism design, smooth animations, and parallax effects.
- **Centralized Configuration & Discovery:** Uses Spring Cloud Config and Eureka for dynamic service registration and environment management.

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

## 📸 Platform Screenshots

### 👤 User Site

<div align="center">
  <img src="screenshots/bakery_site/00_01_Auth_Login.png" width="600px" alt="Auth Login" />
  <img src="screenshots/bakery_site/00_02_Auth_Verify_OTP.png" width="600px" alt="Auth Verify OTP" />
  <img src="screenshots/bakery_site/00_03_User_Registration.png" width="600px" alt="User Registration" />
  <img src="screenshots/bakery_site/01_01_Home_Page.png" width="600px" alt="Home Page" />
  <img src="screenshots/bakery_site/01_02_Home_Page_Fresh_Arrivals.png" width="600px" alt="Home Page Fresh Arrivals" />
  <img src="screenshots/bakery_site/01_03_Home_Page_Featured_Collection.png" width="600px" alt="Home Page Featured Collection" />
  <img src="screenshots/bakery_site/01_04_Home_Page_Top_Rated_Products_01.png" width="600px" alt="Home Page Top Rated Products 01" />
  <img src="screenshots/bakery_site/01_05_Home_Page_Offers.png" width="600px" alt="Home Page Offers" />
  <img src="screenshots/bakery_site/01_06_Home_Page_Testimonials_01.png" width="600px" alt="Home Page Testimonials 01" />
  <img src="screenshots/bakery_site/01_07_Home_Page_Footer.png" width="600px" alt="Home Page Footer" />
  <img src="screenshots/bakery_site/02_01_Menu_Page.png" width="600px" alt="Menu Page" />
  <img src="screenshots/bakery_site/03_01_Products_details_Page.png" width="600px" alt="Products Details Page" />
  <img src="screenshots/bakery_site/03_02_Products_details_Page.png" width="600px" alt="Products Details Page" />
  <img src="screenshots/bakery_site/03_03_Products_details_Page_Users_Review.png" width="600px" alt="Products Details Page Users Review" />
  <img src="screenshots/bakery_site/04_01_Contact_Us_Page.png" width="600px" alt="Contact Us Page" />
  <img src="screenshots/bakery_site/05_01_Cart_Page.png" width="600px" alt="Cart Page" />
  <img src="screenshots/bakery_site/06_01_User_Profile_Page.png" width="600px" alt="User Profile Page" />
  <img src="screenshots/bakery_site/06_02_User_Order_History.png" width="600px" alt="User Order History" />
  <img src="screenshots/bakery_site/06_03_User_Order_Details.png" width="600px" alt="User Order Details" />
  <img src="screenshots/bakery_site/06_04_User_Address.png" width="600px" alt="User Address" />
  <img src="screenshots/bakery_site/06_05_User_Security.png" width="600px" alt="User Security" />
</div>

---

### 🖥️ Admin Site

<div align="center">
  <img src="screenshots/admin_site/01_01_Dashboard.png" width="600px" alt="Dashboard" />
  <img src="screenshots/admin_site/02_01_Orders.png" width="600px" alt="Orders" />
  <img src="screenshots/admin_site/02_02_Orders_Details.png" width="600px" alt="Orders Details" />
  <img src="screenshots/admin_site/03_01_Products_Catlog.png" width="600px" alt="Products Catlog" />
  <img src="screenshots/admin_site/03_02_Add_Product.png" width="600px" alt="Add Product" />
  <img src="screenshots/admin_site/03_03_Add_Product.png" width="600px" alt="Add Product" />
  <img src="screenshots/admin_site/04_01_Categories.png" width="600px" alt="Categories" />
  <img src="screenshots/admin_site/04_02_Add_Category.png" width="600px" alt="Add Category" />
  <img src="screenshots/admin_site/05_01_Stock_Monitor.png" width="600px" alt="Stock Monitor" />
  <img src="screenshots/admin_site/06_01_Storefront.png" width="600px" alt="Storefront" />
  <img src="screenshots/admin_site/06_02_Storefront_Offer.png" width="600px" alt="Storefront Offer" />
  <img src="screenshots/admin_site/07_01_Users_Management.png" width="600px" alt="Users Management" />
  <img src="screenshots/admin_site/08_01_Reviews.png" width="600px" alt="Reviews" />
  <img src="screenshots/admin_site/09_01_Engagements.png" width="600px" alt="Engagements" />
  <img src="screenshots/admin_site/10_01_Settings.png" width="600px" alt="Settings" />
</div>

---

### ☁️ AWS & Dokploy Deployment

<div align="center">
  <img src="screenshots/aws/01_01_EC2_Instances.png" width="600px" alt="EC2 Instances" />
  <img src="screenshots/aws/02_01_EC2_Security_Groups.png" width="600px" alt="EC2 Security Groups" />
  <img src="screenshots/aws/02_02_EC2_Security_Group_Manager.png" width="600px" alt="EC2 Security Group Manager" />
  <img src="screenshots/aws/02_02_EC2_Security_Group_Worker.png" width="600px" alt="EC2 Security Group Worker" />
  <img src="screenshots/aws/03_01_Elastic_ips.png" width="600px" alt="Elastic ips" />
  <img src="screenshots/aws/04_01_Volumes.png" width="600px" alt="Volumes" />
  <img src="screenshots\dokploy\dokploy_bakery_dashboard.jpeg" width="600px" alt="Dokploy" />
</div>

---

## 📄 License

This project is licensed under the MIT License.

---
*Stay tuned as we roll out new features to make Blu'sBakery more responsive and intelligent!*
