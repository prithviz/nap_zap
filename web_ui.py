#! /usr/bin/env python

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, Blueprint
from flask_bootstrap import Bootstrap
from flask_paginate import Pagination, get_page_parameter
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from indexer import Searcher
from lang_proc import remove_stopwords
from lang_proc import to_query_terms
import random

# TODO: Put pagination in search results

app = Flask(__name__)
Bootstrap(app)
searcher = Searcher("indexes")

r = random.randint(1, 33)
logo = str(r) + '.png'


# print request.environ['REMOTE_ADDR']


class SearchForm(Form):
    user_query = StringField('Looking for: ', validators=[DataRequired()])
    search_button = SubmitField("Search")


@app.route("/", methods=["GET", "POST"])
def index():
    search_form = SearchForm(csrf_enabled=False)
    if search_form.validate_on_submit():
        return redirect(url_for("search_results", query=search_form.user_query.data))
    return render_template("index.html", form=search_form, logo=logo)


@app.route("/search_results/<query>")
def search_results(query):
    start_time = datetime.now()
    # stopwords needs to be removed from query :D
    query1 = remove_stopwords(query)
    query_terms = to_query_terms(query1)
    # app.logger.info("Requested [{}]".format(" ".join(map(str, query_terms))))
    docids = searcher.find_documents_AND(query_terms)
    total_doc_num = 0
    for docid in docids:
        total_doc_num += 1
    urls = [searcher.get_url(docid) for docid in docids]
    texts = [searcher.generate_snippet(query_terms, docid) for docid in docids]
    finish_time = datetime.now()
    return render_template("search_results.html", processing_time=(finish_time - start_time),
                           total_doc_num=total_doc_num, query=query, titles_texts_and_urls=zip(urls, texts), logo=logo)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
