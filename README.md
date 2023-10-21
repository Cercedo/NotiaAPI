# 🐦️ NotiaAPI

Backend web application of Notia project for handling simple note features powered by AI.

## Requirements

- [Django v4.2.6](https://docs.djangoproject.com/en/4.2/releases/4.2.6/)
- [Python v3.11.6](https://www.python.org/downloads/release/python-3116/)

## Clean Code

The current repo try to implement good practices during the software
development in order to build a maintainable, scalable and readable
application. In this way, the principles and patterns used are the following:

- Hexagonal Architecture
- Screaming Architecture
- Domain Driven Desing (DDD)
- Dependency Injection (DI)
- Dependency Inversion Principle

Given that those concepts define a kinda workflow, the project structure
defined by Django had to be modified and the framework is only used to manage
external features such as the DB ORM, HTTP handling, deployment setup.
