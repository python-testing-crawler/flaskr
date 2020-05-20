
from python_testing_crawler import (
    Crawler,
    Rule,
    Request,
    Ignore,
    Allow,
)

GET = "GET"
POST = "POST"

ALL_ELEMENTS_RULE_SET = [
    Rule('.*', '/.*', GET, Request())
]
SUBMIT_GET_FORMS_RULE_SET = [
    Rule("form", '.*', GET, Request())
]
SUBMIT_POST_FORMS_RULE_SET = [
    Rule("form", '.*', POST, Request())
]


def _crawl(client):
    crawler = Crawler(
        client=client,
        initial_paths=['/'],
        rules=(
            ALL_ELEMENTS_RULE_SET
            + SUBMIT_GET_FORMS_RULE_SET
            + SUBMIT_POST_FORMS_RULE_SET
            + [
                # don't logout
                Rule(".*", r"/auth/logout", GET, Ignore()),
                # allow 400 on create and update
                Rule(".*", r"/create", POST, Allow([400])),
                Rule(".*", r"/\d+/update", POST, Allow([400])),
            ]
        ),
    )
    crawler.crawl()
    return crawler


def test_crawl_without_auth(client, auth):
    crawler = _crawl(client)


def test_crawl(client, auth):
    auth.login()
    crawler = _crawl(client)


def test_other_crawl(client, auth):
    auth.login()
    crawler = Crawler(
        client=client,
        initial_paths=['/'],
        rules=(
            ALL_ELEMENTS_RULE_SET
            + SUBMIT_GET_FORMS_RULE_SET
            + SUBMIT_POST_FORMS_RULE_SET
            + [
                # don't logout
                Rule(".*", r"/auth/logout", GET, Ignore()),

                # submit some data to create
                Rule(".*", r"/create", POST, Request(params={"title": "A Title", "body": "body text"})),

                # add the missing body when updating
                Rule(".*", r"/\d+/update", POST, Request(params={"body": "updated body"})),
            ]
        ),
    )
    crawler.crawl()