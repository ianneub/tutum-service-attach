# Tutum Service Link Push

This containerized docker app works with services running in the [Tutum cloud](https://www.tutum.co/). It is designed to be used with a stack to allow a stack to link itself into a centralized router.

## Usage

This container assumes that you already have a `tutum/haproxy` service running in another stack or as a stand along service in Tutum.

Given that you have an existing `tutum/haproxy` service running, you will need to get the UUID for that service. Let's assume it is `fbcb2846-a0fb-48bf-89b7-212e601dfdf1`. You could launch a new stack and target the web application to the haproxy router so that it starts routing traffic to this app automatically.

```yaml
web:
  image: tutum/hello-world
  environment:
    - 'VIRTUAL_HOST=http://asdf.yourdoman.com,https://asdf.yourdoman.com'
attach:
  image: ianneub/tutum-service-attach
  links:
    - web
  environment:
    - TARGET_UUID=fbcb2846-a0fb-48bf-89b7-212e601dfdf1
  autodestroy: always
  roles:
    - global
```

## Configuration

This container requires the following variables:

|Name|Description|Example|
|----|-----------|-------|
|`TARGET_UUID`|This is the UUID of the service that you want to add the link to. Normally this would be the UUID of the [tutum/haproxy](https://github.com/tutumcloud/haproxy) service.|`667e2342-e44b-43ab-99f6-369b335d8aad`|
|`TUTUM_AUTH`|This is required to get authentication information from the Tutum API. Normally this will be automatically set by Tutum when you give the service running this app the `global` role.|`ApiKey username:laisugdfilasueytroawe7taooai7t3oaiwuy3o1`|
