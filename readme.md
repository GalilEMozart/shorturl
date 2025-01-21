# System Design : URL SHORT

Create a complete API that will take a long url and return a short url.
That system take a long url like this one (https://www.quora.com/Can-you-recommend-any-websites-with-unusually-long-URLs-What-is-the-purpose-of-creating-such-long-URLs) and produce a short url (https://short_url.com/ywk2v4) that can be easly remembered or insert into social medial post.\
LinkedIn use a short url system when you insert a url into post. The short url redirect to the original url, the long one.

## Basic requirement

- Get short ulr from a long url
- Redirect to the long url when users tries to acces short short url
- Low latency and high availability

## Design and technicals details

- Estimation traffic

We assume that we have 100 millions of new urls per month, per seconde it will be 100 millions / (30 * 24 * 3600) = 40 per second (approx). If we have a ratio of 200:1 in I/O, we get 200*40 = 8000 requests by secondes, for redirection to the original link (read).

- Estimation storage

Assume the life time of service is 50 years, and we have 100 millions of new urls per month, so we will have 100 * 12 * 50 = 60 billions of urls.
Suppose that each data (url, short url, long url, date ) will take 100 bytes, so we will need 60 billions * 100 bytes = 6 TB of storage

- Estimation memory (caching)

Pareto principle : 80% of the traffic will be on 20% of the urls
So to store the 20% of the urls data per day we will need 20% * 40 * 24 * 3600 = 7 millions * 100 bytes = 700 MB, almost 1 GB for cache.

# How to use
You need docker install and run:
```sh
user@path/to/projetc/shorturl docker compose up --build --scale fastapi=2
```
fastapi=2, fix the number of fastapi instance to 2. You can change it, and modifie the load_balancer/nginx.conf

## TODO
- [ ] Unit and Integration test, complete pipeline (CI/CD)
- [x] Asynchonicite on api call
- [x] Load balancer
- [ ] Documentation
- [x] Logging
- [x] Analytics informations
- [ ] Performance Test (low latency, high availability)
- [ ] BDD failure and Scalability
- [ ] Time expiration
- [x] Cache (Redis ?)
- [ ] Other algorithms to generate short url
- [x] Containerization (Docker)
- [ ] Orchestration (Kubernetes ?)
- [ ] Deploy on AWS
- [ ] Monitoring
- [ ] Add alembic (Pour le changement de schemas de la base des donnees)
- [x] Add pre-commit Flask8 pep8 isort
- [ ] Volume docker

# resources
- [Fist ressource](https://www.codekarle.com/system-design/TinyUrl-system-design.html?source=post_page-----106f30f23a82--------------------------------)
- [Second ressource](https://medium.com/@sandeep4.verma/system-design-scalable-url-shortener-service-like-tinyurl-106f30f23a82)
- [Last one](https://www.hellointerview.com/learn/system-design/problem-breakdowns/bitly)
