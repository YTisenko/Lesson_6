from behave import given, when, then

@then('Verify Sign In Page Opened')
def verify_signin_opened(context):
   context.app.signin_page.verify_signin_opened()
