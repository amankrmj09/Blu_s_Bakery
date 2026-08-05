# API Reference: Product Service - Categories

This documentation details the API endpoints for category management within the Product Service.

## Base URL
`/api/categories`

## Endpoints

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/categories` | Get all categories | No |
| `GET` | `/api/categories/active` | Get active categories only | No |
| `GET` | `/api/categories/with-products` | Get categories with products | No |
| `GET` | `/api/categories/with-active-products` | Get categories with active products | No |
| `GET` | `/api/categories/top-with-products` | Get top categories with top products | No |
| `GET` | `/api/categories/{categoryId}` | Get category by ID | No |
| `POST` | `/api/categories` | Create new category | Yes (ADMIN) |
| `PUT` | `/api/categories/{categoryId}` | Update category | Yes (ADMIN) |
| `DELETE` | `/api/categories/{categoryId}` | Delete category | Yes (ADMIN) |
| `GET` | `/api/categories/search` | Search categories | No |
| `GET` | `/api/categories/admin/search` | Search categories (Admin) | Yes (ADMIN) |
| `POST` | `/api/categories/{categoryId}/toggle-status` | Toggle category status | Yes (ADMIN) |
| `POST` | `/api/categories/reorder` | Reorder categories | Yes (ADMIN) |
| `GET` | `/api/categories/statistics` | Get category statistics | Yes (ADMIN) |
