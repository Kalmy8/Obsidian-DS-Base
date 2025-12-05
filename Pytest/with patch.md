This is where the magic of "hijacking" imports happens.

with patch('buyer_example.agent.BuyerSDK', return_value=mock_buyer_sdk):

    return BuyerExample(mock_settings)

The Problem it solves:

Your BuyerExample class (in src/buyer_example/agent.py) has this line in its __init__:

self.sdk = BuyerSDK(...) 

Normally, this would create a real BuyerSDK that tries to connect to the internet. We don't want that in a unit test.

How patch fixes it:

1. Target: buyer_example.agent.BuyerSDK tells Python: "Go to the file buyer_example/agent.py and find where BuyerSDK is used."

2. Swap: "Temporarily replace that class with a fake object."

3. return_value: "When that fake class is called (instantiated) like BuyerSDK(...), don't return a new class instance. Return this specific object (mock_buyer_sdk) instead."

The Result:

When BuyerExample(mock_settings) runs inside the with block:

1. It calls self.sdk = BuyerSDK(...).

2. Because of the patch, it actually executes self.sdk = mock_buyer_sdk.

3. Now your BuyerExample instance is permanently holding your fake SDK, allowing you to control it completely during the test.