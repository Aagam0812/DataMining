import pytest
from app import create_app
from unittest.mock import patch
from unittest.mock import Mock


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_index_page(client, mocker):
    # Mock the get_trivia_question function to return a sample question and answer
    mocker.patch('app.get_trivia_question', return_value=("Sample Question", "Sample Answer"))
    
    #Test GET request
    response = client.get('/')
    print("response: ", response.data)
    assert b'Art & Literature' in response.data

    # Test POST request with a selected topicpytest
    response = client.post('/', data={'topic': 'artliterature'})
    assert b'Sample Question' in response.data
    assert b'Sample Answer' in response.data

    # Test POST request without a selected topic (this should never happen due to the HTML 'required' attribute, but it's good to test)
    response = client.post('/', data={'topic': ''})
    assert b'Art & Literature' in response.data



def test_get_trivia_question(mocker): 
    # Mock the get_trivia_question function
    mocker.patch('app.get_trivia_question', return_value=("Sample Question", "Sample Answer"))

    # Test if the function returns the correct output
    from app import get_trivia_question
    assert get_trivia_question("artliterature") == ("Sample Question", "Sample Answer")

# Path: Assignment2/projects/Travia/workspace/app.py    
# Compare this snippet from Assignment2/projects/Travia/workspace/app.py:
# from flask import Flask, render_template, request
# import requests
# import os
