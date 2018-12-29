# Table of Content

1.  How to install
2.  How to deploy
3.  References

# How to install

1.  Run `pip install -r requirements.txt`

# How to run
1. Go to `scrapy_comment` path
2. Run `scrapy crawl rotten` or `scrapy crawl rotten -o rotten.json`

# How to deploy

1.  Change directory to `scrapy_stores`
2.  Run `scrapyd` from your machine
3.  Run `scrapyd-deploy`
4.  Run spider eg: `curl http://localhost:6800/schedule.json -d project=default -d spider=rotten`

# References

https://scrapyd.readthedocs.io/en/latest/index.html
https://github.com/scrapy/scrapyd-client
