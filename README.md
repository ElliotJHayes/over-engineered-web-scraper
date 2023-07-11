# over-engineered-web-scraper
A small project to create an overengineered web scraper. In the process I hope to get a deeper understanding of Kafka streams and the repository/service/controller design pattern.


## Usage
### Kafka topic startup
`docker compose up`

### Local kafka production and consumption (Windows)
`kafka-console-producer.bat --bootstrap-server localhost:9092 --topic my-topic-1`
`kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic my-topic-1`