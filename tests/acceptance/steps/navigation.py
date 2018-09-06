from behave import *
from selenium import webdriver

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')  # Regular expression


@given('I am on the homepage')  # Decorator given will be executed
# every time string inside the () will be called
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = HomePage(context.driver)
    context.driver.get(page.url)


@step('I am on the Blog page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@given('I am on the new Post Page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = NewPostPage(context.driver)
    context.driver.get(page.url)


@then('I am navigated to the Blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am navigated to the Home page')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url



