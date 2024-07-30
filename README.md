# Noob
Begineer Codes - applying begnners concept in code for a project.

# Commit Message Format

This document outlines the commit message prefixes to be used for categorizing different types of changes in the project, aligned with the stages of the Software Development Life Cycle (SDLC).

## Commit Message Prefixes

### Design
- **design:** - Design-related changes, including architectural diagrams, mockups, and design documents
  - Example: `design: add system architecture diagram`

### Coding
- **code:** - Writing or updating code, including initial implementations and code refactoring
  - Example: `code: implement user authentication`
- **refactor:** - Refactoring existing code to improve structure without changing functionality
  - Example: `refactor: optimize database query logic`

### Fixing
- **fix:** - Bug fixes and addressing defects in the code
  - Example: `fix: resolve null pointer exception in login service`
- **hotfix:** - Critical fixes that need to be deployed immediately
  - Example: `hotfix: patch security vulnerability in authentication`

### Adding Features
- **feat:** - Adding new features or functionality to the application
  - Example: `feat: add user profile page`
- **enhance:** - Enhancements to existing features
  - Example: `enhance: improve search algorithm performance`

### Documenting
- **docs:** - Adding or updating documentation, including inline code comments, README files, and user guides
  - Example: `docs: update installation instructions`
- **comment:** - Adding or improving comments in the codebase
  - Example: `comment: add comments to user service methods`

### Additional Commit Message Prefixes

#### Testing
- **test:** - Adding or updating tests
  - Example: `test: add unit tests for login component`

#### Build and Deployment
- **build:** - Changes that affect the build system or external dependencies
  - Example: `build: update Maven configuration`
- **ci:** - Changes to CI configuration files and scripts
  - Example: `ci: add Travis CI configuration`

#### Chore
- **chore:** - Miscellaneous tasks that don't modify src or test files
  - Example: `chore: update npm dependencies`

#### Reversions
- **revert:** - Reverts a previous commit
  - Example: `revert: revert "feat: add user profile page"`

#### Dependencies
- **deps:** - Changes related to dependencies
  - Example: `deps: update lodash to v4.17.21`

#### Localization
- **i18n:** - Internationalization and localization changes
  - Example: `i18n: add French translations`

#### Security
- **security:** - Changes that improve security
  - Example: `security: fix XSS vulnerability in user input`

#### Content
- **content:** - Changes related to content
  - Example: `content: update homepage text and images`

## Example Commit Messages
- `design: create wireframes for new dashboard`
- `code: implement initial setup for project`
- `fix: correct issue with user session timeout`
- `feat: integrate payment gateway`
- `docs: add contributing guidelines`
- `test: add integration tests for payment module`
- `build: configure Docker for deployment`
- `ci: update GitHub Actions workflow`
- `chore: clean up deprecated functions`
- `revert: revert "code: implement initial setup for project"`
- `deps: upgrade axios to latest version`
- `i18n: add Spanish translations`
- `security: enhance password encryption`
- `content: refresh about page content`
