# cython-orderbook
A high-performance order book implementation in Python with Cython acceleration and price-time priority matching. Available as an official PyPI package.

## Installation
````pip install cython-orderbook```

## Features
* Price-time priority matching engine
* Limit and market order support
* Order cancellation
* Trade log with aggressor tracking
* 670k+ matched orders/second throughput (5.4x faster than pure Python)

## Usage
```python
from cython_orderbook import OrderBook, Order, OrderSide
from decimal import Decimal

book = OrderBook()

# Add a limit order
bid = Order(side=OrderSide.BID, price=Decimal("50.00"), original_quantity=100)
book.add_limit_order(bid)

# Add a matching ask
ask = Order(side=OrderSide.ASK, price=Decimal("50.00"), original_quantity=100)
book.add_limit_order(ask)

# Add a market order (no price needed)
market_order = Order(side=OrderSide.BID, original_quantity=50)
book.add_market_order(market_order)

# Cancel an order
book.cancel_order(bid.order_id)

# Display the book
print(book)

# View trade log
book.print_trade_log()
```

## Performance
````
Simple inserts:     ~1.49M orders/second
Matched pairs:      ~670k orders/second
Mixed actions:      ~610k orders/second
