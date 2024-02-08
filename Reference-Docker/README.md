---
Title: Docker... Twenty Minutes
Author: Thomas J. Kennedy
TOC: yes
---

This document is (or started as) a brief (and informal) twenty minute Docker
discussion.


# What is Docker?

A container can be thought of as a sandbox. A container allows:

  - A piece of software to run in isolation.
  - Different tool/technologies to be run in parallel (e.g., a two different
    versions of flask).
  - Environment parity... the same Docker image can be reproduced (with fixed
    software tool versions) on multiple machines.

Take a look at the official [Docker "What is a Container" page](https://www.docker.com/resources/what-container).


**Example**

  - [CS 417 Lecture
    Examples](https://git-community.cs.odu.edu/tkennedy/cs417-lecture-examples)

    *Note that you will need to log in with your CS account.*


# What is Docker Compose?

[Docker compose](https://docs.docker.com/compose/) allows multiple docker
containers to:

  - communicate with each other
  - started and stopped simultaneously

**Examples**

  - [Basic LAMP Stack with
    MariaDB](https://mariadb.com/kb/en/setting-up-a-lamp-stack-with-docker-compose/)

