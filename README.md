# Fsite
# Secure Notes App - Django Project

## Description
Secure Notes App est une application web simple développée avec Django.  
Elle permet aux utilisateurs de créer, lire, modifier et supprimer des notes personnelles.  
L'objectif principal du projet est d'intégrer des **pratiques de sécurité** dans une application web.

---

## Fonctionnalités

### Fonctionnalités principales
- Inscription et connexion des utilisateurs  
- Création, lecture, modification et suppression de notes  
- Chaque utilisateur peut voir uniquement ses propres notes  
- Redirection automatique vers la page Notes après connexion

### Sécurité intégrée
- **Hashing des mots de passe** avec Argon2 pour protéger les comptes  
- **CSRF Protection** sur tous les formulaires  
- **Rate Limiting** sur la connexion pour prévenir les attaques brute force  
- **Logging** de tous les événements importants (login, CRUD, IP) dans `security.log`  
- **Security Headers** pour prévenir XSS, clickjacking et content injection  
- **Input Validation / Sanitization** avec ORM Django et `bleach` pour empêcher les injections SQL et XSS  
- **Session Security**: cookies sécurisés, expiration à la fermeture du navigateur

---

## Installation

1. Cloner le dépôt :

```bash
git clone https://github.com/votre-utilisateur/secure-notes-app.git
cd secure-notes-app
