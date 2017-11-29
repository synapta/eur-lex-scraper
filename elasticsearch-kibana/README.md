# Docker ELK stack

Run the latest version of Elasticsearch and Kibana with Docker and Docker Compose.

Based on the official Docker images:

* [elasticsearch](https://github.com/elastic/elasticsearch-docker)
* [kibana](https://github.com/elastic/kibana-docker)

## Requirements

### Host setup

1. Install [Docker](https://www.docker.com/community-edition#/download) version **1.10.0+**
2. Install [Docker Compose](https://docs.docker.com/compose/install/) version **1.6.0+**
3. Clone this folder

## Usage

### Bringing up the stack

Start the ELK stack using `docker-compose`:

```bash
$ docker-compose up
```

You can also choose to run it in background (detached mode):

```bash
$ docker-compose up -d
```

Give Kibana about 2 minutes to initialize, then access the Kibana web UI by hitting
[http://localhost:5601](http://localhost:5601) with a web browser.

By default, the stack exposes the following ports:
* 5000: Logstash TCP input.
* 9200: Elasticsearch HTTP
* 9300: Elasticsearch TCP transport
* 5601: Kibana
