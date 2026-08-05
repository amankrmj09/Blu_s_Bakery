# 🧁 Shah's Bakery - React Frontend Applications

Welcome to the **React JS Workspace** for Shah's Bakery Microservices Platform. This directory houses the modern frontend applications that power both the customer-facing storefront and the administrative dashboard.

---

## Folder Structure

`	ext
reactjs/
├── API_REFERENCE.md
├── API_REFERENCE_NEW.md
├── README.md
├── bakery-admin
│   ├── .env
│   ├── .env.example
│   ├── .gitignore
│   ├── Dockerfile
│   ├── README.md
│   ├── eslint.config.js
│   ├── index.html
│   ├── nginx.conf
│   ├── package-lock.json
│   ├── package.json
│   ├── public
│   │   ├── apple-touch-icon.png
│   │   ├── favicon.ico
│   │   ├── icon-192-maskable.png
│   │   ├── icon-192.png
│   │   ├── icon-512-maskable.png
│   │   ├── icon-512.png
│   │   └── manifest.json
│   ├── rtk-query-migration-plan.md
│   ├── src
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── api
│   │   │   ├── axiosConfig.js
│   │   │   ├── engagementsApi.js
│   │   │   └── reviewsApi.js
│   │   ├── app
│   │   │   └── ThemeContext.jsx
│   │   ├── assets
│   │   ├── components
│   │   │   ├── ProtectedRoute.jsx
│   │   │   ├── layout
│   │   │   │   ├── IslandLayout.jsx
│   │   │   │   └── Sidebar.jsx
│   │   │   ├── settings
│   │   │   │   └── TaxSettings.jsx
│   │   │   ├── shared
│   │   │   │   ├── CategoryDropdown.jsx
│   │   │   │   ├── Pagination.jsx
│   │   │   │   ├── ProductMediaUploader.jsx
│   │   │   │   ├── ProductReviewsTab.jsx
│   │   │   │   ├── SingleImageUploader.jsx
│   │   │   │   └── TopSearchBar.jsx
│   │   │   └── ui
│   │   │       ├── ActionButton.jsx
│   │   │       ├── ActionIconButton.jsx
│   │   │       ├── AuraBackground.jsx
│   │   │       ├── Badge.jsx
│   │   │       ├── Button.jsx
│   │   │       ├── Card.jsx
│   │   │       ├── CustomDatePicker.jsx
│   │   │       ├── Input.jsx
│   │   │       ├── Modal.jsx
│   │   │       ├── SleekDropdown.jsx
│   │   │       ├── SleekSearchDropdown.jsx
│   │   │       ├── Table.jsx
│   │   │       └── Textarea.jsx
│   │   ├── hooks
│   │   │   └── useScrollTop.js
│   │   ├── index.css
│   │   ├── layouts
│   │   ├── lib
│   │   │   └── utils.js
│   │   ├── main.jsx
│   │   ├── pages
│   │   │   ├── Categories.jsx
│   │   │   ├── CategoryDetails.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── EngagementsPage.jsx
│   │   │   ├── Inventory.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── OrderDetails.jsx
│   │   │   ├── Orders.jsx
│   │   │   ├── ProductDetails.jsx
│   │   │   ├── Products.jsx
│   │   │   ├── Reviews.jsx
│   │   │   ├── Settings.jsx
│   │   │   ├── Storefront.jsx
│   │   │   └── Users.jsx
│   │   └── store
│   │       ├── index.js
│   │       └── slices
│   │           ├── authSlice.js
│   │           ├── dashboardSlice.js
│   │           └── taxSlice.js
│   └── vite.config.js
├── bakery-user
│   ├── .env
│   ├── .env.example
│   ├── .gitignore
│   ├── Dockerfile
│   ├── README.md
│   ├── eslint.config.js
│   ├── index.html
│   ├── nginx.conf
│   ├── package-lock.json
│   ├── package.json
│   ├── public
│   │   ├── apple-touch-icon.png
│   │   ├── favicon.ico
│   │   ├── icon-192-maskable.png
│   │   ├── icon-192.png
│   │   ├── icon-512-maskable.png
│   │   ├── icon-512.png
│   │   ├── images
│   │   │   ├── Our_Story_02.jpg
│   │   │   ├── Our_Story_03.jpg
│   │   │   ├── auth_01.jpg
│   │   │   ├── auth_02.jpg
│   │   │   ├── auth_03.jpg
│   │   │   ├── auth_04.jpg
│   │   │   ├── auth_05.jpg
│   │   │   ├── auth_06.jpg
│   │   │   ├── auth_07.jpg
│   │   │   ├── bakery_chef.png
│   │   │   ├── bakery_customers.png
│   │   │   ├── campaign1_small.png
│   │   │   ├── campaign3_small.png
│   │   │   └── placeholder_bakery.png
│   │   └── manifest.json
│   ├── src
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── app
│   │   │   ├── rootReducer.js
│   │   │   └── store.js
│   │   ├── components
│   │   │   ├── animations
│   │   │   │   └── FadeIn.jsx
│   │   │   ├── layout
│   │   │   │   ├── AuthLayout.jsx
│   │   │   │   ├── Footer.jsx
│   │   │   │   ├── MainLayout.jsx
│   │   │   │   └── ScrollToTop.jsx
│   │   │   └── ui
│   │   │       ├── ActionButton.jsx
│   │   │       ├── AnimatedBackground.jsx
│   │   │       ├── CachedImage.jsx
│   │   │       ├── Modal.jsx
│   │   │       ├── SearchAutocomplete.jsx
│   │   │       ├── ShowcaseCard.jsx
│   │   │       ├── Skeleton.jsx
│   │   │       └── SleekDropdown.jsx
│   │   ├── features
│   │   │   ├── auth
│   │   │   │   ├── api
│   │   │   │   │   └── authApi.js
│   │   │   │   ├── components
│   │   │   │   ├── hooks
│   │   │   │   ├── pages
│   │   │   │   │   ├── ForgotPasswordPage.jsx
│   │   │   │   │   ├── LoginPage.jsx
│   │   │   │   │   ├── OtpPage.jsx
│   │   │   │   │   ├── RegisterPage.jsx
│   │   │   │   │   └── ResetPasswordPage.jsx
│   │   │   │   ├── redux
│   │   │   │   │   ├── authSlice.js
│   │   │   │   │   └── authThunk.js
│   │   │   │   └── utils
│   │   │   ├── cart
│   │   │   │   ├── api
│   │   │   │   │   └── cartApi.js
│   │   │   │   ├── components
│   │   │   │   ├── pages
│   │   │   │   │   └── CartPage.jsx
│   │   │   │   └── redux
│   │   │   │       ├── cartSlice.js
│   │   │   │       └── cartThunk.js
│   │   │   ├── checkout
│   │   │   │   ├── api
│   │   │   │   │   └── paymentApi.js
│   │   │   │   ├── components
│   │   │   │   ├── pages
│   │   │   │   │   ├── CheckoutPage.jsx
│   │   │   │   │   └── PaymentPage.jsx
│   │   │   │   └── redux
│   │   │   ├── order
│   │   │   │   ├── api
│   │   │   │   │   └── orderApi.js
│   │   │   │   ├── components
│   │   │   │   │   └── OrderCard.jsx
│   │   │   │   └── slice
│   │   │   │       └── orderSlice.js
│   │   │   ├── shop
│   │   │   │   ├── api
│   │   │   │   │   └── shopApi.js
│   │   │   │   ├── components
│   │   │   │   │   ├── ProductCard.jsx
│   │   │   │   │   ├── ProductSkeleton.jsx
│   │   │   │   │   ├── ReportReviewModal.jsx
│   │   │   │   │   ├── ReviewModal.jsx
│   │   │   │   │   └── home
│   │   │   │   │       ├── AboutUsSection.jsx
│   │   │   │   │       ├── AboutUsSectionSkeleton.jsx
│   │   │   │   │       ├── HeroSection.jsx
│   │   │   │   │       ├── HeroSectionSkeleton.jsx
│   │   │   │   │       ├── HomePageSkeleton.jsx
│   │   │   │   │       ├── NewProductsSection.jsx
│   │   │   │   │       ├── NewProductsSectionSkeleton.jsx
│   │   │   │   │       ├── SpecialOfferSection.jsx
│   │   │   │   │       ├── SpecialOfferSectionSkeleton.jsx
│   │   │   │   │       ├── TestimonialsSection.jsx
│   │   │   │   │       ├── TestimonialsSectionSkeleton.jsx
│   │   │   │   │       ├── TopCategoriesSection.jsx
│   │   │   │   │       └── TopCategoriesSectionSkeleton.jsx
│   │   │   │   ├── pages
│   │   │   │   │   ├── ContactPage.jsx
│   │   │   │   │   ├── HomePage.jsx
│   │   │   │   │   ├── PrivacyPage.jsx
│   │   │   │   │   ├── ProductDetailsPage.jsx
│   │   │   │   │   ├── ShopPage.jsx
│   │   │   │   │   └── TermsPage.jsx
│   │   │   │   └── redux
│   │   │   │       ├── shopSlice.js
│   │   │   │       └── shopThunk.js
│   │   │   └── user
│   │   │       ├── api
│   │   │       │   ├── addressApi.js
│   │   │       │   └── userApi.js
│   │   │       ├── components
│   │   │       │   ├── CancelOrderModal.jsx
│   │   │       │   ├── MyAddresses.jsx
│   │   │       │   ├── MyOrders.jsx
│   │   │       │   ├── ProfileDetails.jsx
│   │   │       │   └── TimeFilterControls.jsx
│   │   │       ├── pages
│   │   │       │   ├── ProfilePage.jsx
│   │   │       │   └── SettingsPage.jsx
│   │   │       └── redux
│   │   │           └── addressSlice.js
│   │   ├── hooks
│   │   ├── lib
│   │   │   └── axios.js
│   │   ├── main.jsx
│   │   ├── routes
│   │   │   └── AppRoutes.jsx
│   │   ├── styles
│   │   │   └── globals.css
│   │   └── utils
│   │       ├── animations.js
│   │       └── imageUtils.js
│   └── vite.config.js
├── script.py
└── tree_output.txt
`

## 🚀 Projects Overview

| Project | Folder | Description | Tech Stack |
| :--- | :--- | :--- | :--- |
| **Admin Portal** | [`bakery-admin`](./bakery-admin) | Administrative dashboard for inventory management, order fulfillment, sales analytics, user roles, storefront customization, and engagement oversight. | React 19, Vite, Redux Toolkit, Tailwind CSS v4, Recharts, Lucide Icons |
| **User Storefront** | [`bakery-user`](./bakery-user) | Feature-rich customer-facing web application for product browsing, category filtering, cart management, checkout, order tracking, and user profile settings. | React 19, Vite, Redux Toolkit, Tailwind CSS v4, Framer Motion, Lenis Smooth Scroll |

---

## 📁 Workspace Folder Structure

```text
reactjs/
├── README.md                   # ReactJS Workspace documentation & setup guide
├── API_REFERENCE.md            # API Reference documentation for frontend integrations
│
├── bakery-admin/               # Admin Management Dashboard Application
│   ├── public/                 # Static web assets & PWA manifest
│   ├── src/                    # Source code
│   │   ├── api/                # API client modules (axiosConfig, engagementsApi, reviewsApi)
│   │   ├── app/                # Application contexts & providers (ThemeContext)
│   │   ├── assets/             # Static design assets & images
│   │   ├── components/         # Reusable React components
│   │   │   ├── layout/         # IslandLayout, Sidebar
│   │   │   ├── settings/       # TaxSettings
│   │   │   ├── shared/         # CategoryDropdown, Pagination, Media Uploaders
│   │   │   └── ui/             # ActionButtons, Cards, Modals, Tables, Inputs
│   │   ├── hooks/              # Custom React hooks (useScrollTop)
│   │   ├── lib/                # Utility helpers & class merging helpers
│   │   ├── pages/              # Admin pages (Dashboard, Orders, Products, Inventory, Users, Categories, Settings, Storefront, Reviews, Engagements)
│   │   ├── store/              # Global state management (Redux Toolkit slices)
│   │   │   └── slices/         # authSlice, dashboardSlice, taxSlice
│   │   ├── App.jsx             # Main Router setup & layout composition
│   │   ├── index.css           # Global Tailwind CSS styles
│   │   └── main.jsx            # Application entry point
│   ├── Dockerfile              # Production Docker build definition
│   ├── nginx.conf              # Nginx web server config
│   ├── package.json            # Node dependencies & npm scripts
│   └── vite.config.js          # Vite build configuration
│
└── bakery-user/                # Customer Storefront Web Application
    ├── public/                 # Static web assets
    ├── src/                    # Source code
    │   ├── app/                # Redux Store configuration & root reducer
    │   ├── components/         # Generic UI components & layout elements
    │   │   ├── animations/     # Framer Motion animation helpers (FadeIn)
    │   │   ├── layout/         # MainLayout, AuthLayout, Footer, ScrollToTop
    │   │   └── ui/             # ShowcaseCard, CachedImage, SearchAutocomplete, Modals
    │   ├── features/           # Domain-driven feature modules
    │   │   ├── auth/           # Login, Register, OTP Verification, Password Reset
    │   │   ├── cart/           # Shopping Cart drawer, cart sync, checkout trigger
    │   │   ├── checkout/       # Checkout workflow & payment processing
    │   │   ├── order/          # Order history listing, order detail modal, order cancellation
    │   │   ├── shop/           # Catalogue view, category filter, search, reviews, home sections
    │   │   └── user/           # Customer profile management & address book
    │   ├── hooks/              # Custom React hooks
    │   ├── lib/                # Third-party configurations & Axios instance
    │   ├── routes/             # App routing rules & ProtectedRoute setup
    │   ├── styles/             # Global CSS stylesheets
    │   ├── utils/              # Helper utilities (animation presets, image helpers)
    │   ├── App.jsx             # Application root container
    │   └── main.jsx            # Application entry point
    ├── Dockerfile              # Production Docker build definition
    ├── nginx.conf              # Nginx web server config
    ├── package.json            # Node dependencies & npm scripts
    └── vite.config.js          # Vite build configuration
```

---

## 🛠️ Tech Stack & Key Libraries

- **Framework & Build Tool:** [React 19](https://react.dev/) with [Vite 8](https://vitejs.dev/)
- **State Management:** [@reduxjs/toolkit](https://redux-toolkit.js.org/) for async thunks & global state
- **Styling & UI:** [Tailwind CSS v4](https://tailwindcss.com/), [Framer Motion](https://www.framer.com/motion/), [Lucide React Icons](https://lucide.dev/), [Sonner](https://sonner.emilkowal.ski/) toast notifications
- **HTTP Client:** [Axios](https://axios-http.com/) with request/response interceptors & Bearer Auth injection
- **Data Visualization:** [Recharts](https://recharts.org/) for sales and order analytics in `bakery-admin`

---

## 💻 Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v18.0.0 or higher recommended)
- NPM or Yarn package manager

### 1. Admin Portal Setup (`bakery-admin`)

```bash
# Navigate to the bakery-admin directory
cd reactjs/bakery-admin

# Install dependencies
npm install

# Configure environment variables
cp .env.example .env

# Run development server
npm run dev
```

The application will be accessible at `http://localhost:5173`.

### 2. User Storefront Setup (`bakery-user`)

```bash
# Navigate to the bakery-user directory
cd reactjs/bakery-user

# Install dependencies
npm install

# Configure environment variables
cp .env.example .env

# Run development server
npm run dev
```

The application will be accessible at `http://localhost:5174` (or next available port).

---

## 📜 NPM Scripts Reference

Each subproject includes the following standard scripts:

| Script | Command | Purpose |
| :--- | :--- | :--- |
| `npm run dev` | `vite` | Starts the Vite hot-reloading development server |
| `npm run build` | `vite build` | Compiles production-ready bundle into `/dist` |
| `npm run preview` | `vite preview` | Previews the production build locally |
| `npm run lint` | `eslint .` | Runs ESLint to check for code quality issues |

---

## 🐳 Docker Deployment

Both applications include optimized multi-stage Docker builds using Nginx:

```bash
# Build and run Admin Portal container
cd bakery-admin
docker build -t bakery-admin:latest .
docker run -d -p 8080:80 bakery-admin:latest

# Build and run User Portal container
cd bakery-user
docker build -t bakery-user:latest .
docker run -d -p 8081:80 bakery-user:latest
```

---

## 🔗 Related Links
- [Parent Repository](https://github.com/amankrmj09/Blu_s_Bakery)
- [API Reference](./API_REFERENCE.md)

---

## 📖 API Documentation

For complete API endpoint specifications and integration details, see the [`API_REFERENCE.md`](./API_REFERENCE.md) document.


