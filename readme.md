# System Design : URL SHORT

## Problem Statement
- Create an api that will take a long url and return a short url
    - The short url should be unique and should not be repeated
    - The short url should be a random string of 6 characters, containing only letters and numbers, so 36^6 possibilities ( arbitrary choice)



- Estimation traffic

Assume we have 100 millions of new urls per month, per seconde it will be 100 millions / (30 * 24 * 3600) = 40 per second (approx)
Si on a un ratio de 200:1 en lecture/ecriture, on aura 200 * 40 = 8000 requetes par seconde en terme de rediction (lecture)

- Estimation storage

Assume the life time of service is 50 years, and we have 100 millions of new urls per month, so we will have 100 millions * 12 * 50 = 60 billions of urls.
Each data (url, short url, long url, date ) will take 100 bytes, so we will need 60 billions * 100 bytes = 6 TB of storage

- Estimation memory (caching)
Pareto principle : 80% of the traffic will be on 20% of the urls
So to store the 20% of the urls data per day we will need 20% * 40 * 24 * 3600 = 7 millions * 100 bytes = 700 MB, almost 1 GB