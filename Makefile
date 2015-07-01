.PHONY: build push

NAME=ianneub/tutum_haproxy_push

build:
	docker build -t $(NAME) .

push:
	docker push $(NAME)

test:
	docker run --env-file=.env $(NAME)
