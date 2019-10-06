FROM mongo

COPY test_nr_data.json /test_nr_data.json
CMD use test;
CMD db.tweet.remove({})
CMD mongoimport --host mongodb:27017 --db test --collection tweet --file /test_nr_data.json