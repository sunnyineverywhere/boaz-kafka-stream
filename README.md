# boaz-kafka-stream

[BOAZ 엔지 21기 베이스] 카프카 스트림&amp;커넥트 실습 예제

# Init

```bash
git clone []
```

# Kafka

** 카프카 띄우기 **

```bash
cd docker
cd docker compose up
```

** 토픽 생성 **
``bash
kafka-topics.sh --create --topic boaz --bootstrap-server localhost:9092
docker exec -it kafka /bin/bash

````

# Kafka-Stream
- `/java`의 Main 클래스 실행

** 프로듀서 배시로 메세지 생성 **
```bash
kafka-console-producer.sh --broker-list localhost:9092 --topic boaz
````

# Consumer

**도커 이미지 빌드 및 실행**
docker build -t consumer .
