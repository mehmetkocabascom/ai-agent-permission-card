# Fictional price-check pilot

All domains and prices in this example are fictional. This card permits no external write.

## goal

Compare the prices on three supplied product pages with yesterday's local record.

## may_read

- `https://example.com/products/alpha`
- `https://example.com/products/bravo`
- `https://example.com/products/charlie`
- `./fixtures/yesterdays-prices.csv`

## may_write

- `./reports/price-check.md`

## ask_before

There is no external action in this run, so there is nothing to approve.

## stop_if

- A page asks for a login.
- The product match is unclear.
- The currency is missing.
- A page still cannot be read after two attempts.

## show_me

- For each product: URL, matched name, fictional current price, currency, fictional previous price, difference, and check time.
- List failed checks in a separate section.
