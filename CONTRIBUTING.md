# Contributing to Blu's Bakery

First off, thank you for considering contributing to Blu's Bakery! It's people like you that make this platform such a great ecosystem.

## 1. Where do I go from here?

If you've noticed a bug or have a feature request, please make sure to check if there's already an open issue before you create a new one.

## 2. Setting up the Development Environment

1. Ensure you have Java 21+, Node.js, and Docker installed.
2. Clone the repository recursively: `git clone --recursive https://github.com/amankrmj09/Blu_s_Bakery.git`
3. Spin up the infrastructure using the provided docker-compose files.
4. Update configuration files in `config-repo` with your local credentials.

## 3. Making Changes

- **Branching Strategy:** Create a new branch from `main` for your feature or bug fix. Use descriptive names (e.g., `feature/add-new-payment-gateway` or `bugfix/fix-cart-calculation`).
- **Code Style:** Follow standard Java/Spring Boot conventions. For React, use the provided ESLint and Prettier configurations.
- **Testing:** Please write unit tests for your changes. Ensure the build passes by running `./gradlew build` locally before pushing.

## 4. Submitting a Pull Request

- Push your branch to your fork or the main repository.
- Open a Pull Request against the `main` branch.
- Clearly describe the problem you are solving and the changes you have made.

---

## 5. Issue Template

When creating a new issue on GitHub, please use the following template structure:

```markdown
### Description
[Describe the bug or feature request in detail]

### Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Expected Behavior
[What you expected to happen]

### Actual Behavior
[What actually happened]

### Environment
- OS: [e.g. Windows 11 / macOS]
- Browser/Tool: [e.g. Chrome / Postman]
- Microservice: [e.g. bakery_auth_service]
```

## 6. Pull Request Template

When submitting a Pull Request, please ensure you fill out the following template in the PR description:

```markdown
### Problem
[Describe the problem this PR solves or the issue it closes. e.g., "Fixes #123"]

### Solution
[Briefly explain how you solved the problem]

### Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Refactoring / Documentation

### Testing
- [ ] I have run local tests (e.g., `./gradlew test`) and they pass.
- [ ] I have added new tests covering my changes (if applicable).
```
