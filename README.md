# Shop API

Simple API for managing products, orders, users using stripe for payments.
Please note that app has some lacks and it's not fully complete. It need's code improvement and few more tests.

## Setup

Firstly please create `.env` file in the root of directory with following data:

```
DB_NAME=shopapi
DB_HOST=db
DB_USER=root
DB_PASSWORD=qwerty

APPLICATION_HOST=0.0.0.0
STRIPE_KEY=<generated-stripe-test-key>

SALT=examplevalue
```

In order to get `STRIPE_KEY` head into https://stripe.com/en-pl and create an account.

Next steps:

1. Click on the Developers tab in right corner
2. On the left sidebar select API keys
3. In standard keys click on reveal test key
4. Copy it and paste into .env file

**Note!**
Api key should start with `sk_test` characters.

Then run `docker-compose up --build` command

After everything is done properly, type in terminal `docker ps` and copy the *CONTAINER ID* of shop-api_web.

In new terminal tab type `docker exec -it <container-id> bash`.

Next run `export PYTHONPATH=./src` and as second command `alembic upgrade head`.

From now api should be accessible at 0.0.0.0:8000/docs

## How to test if it works?

1. Firstly create 2 users at `/create-user` endpoint. First should have group `admin` with strong password (8 characters, 1 letter, 1 number and 1 special character) and valid email and second account with different email and and group `seller`
2. Secondly hit `/login` endpoint with any of users (just for validation).
3. Next step is to create product, as `owner_id` pass user id with group **seller** you just created.
4. Now register order at `/create-order` endpoint, pass currently logged user id (`admin`) id of product you just created. You can leave status unchanged, for now it has no validation.
5. And the last step. Hit `proceed-payment` endpoint with given data:
```
{
  "customer_id": <id-of-admin-group-acc>,
  "order_id": <id-of-created-order>,
  "currency": "pln",
  "card_number": 4242424242424242,
  "exp_month": 12,
  "exp_year": 2025,
  "cvc": 123
}
```

If you lost in that ids numbers, remember you can get them on `get` method endpoints

If there will be any problems with configuration, anything else please let me know
