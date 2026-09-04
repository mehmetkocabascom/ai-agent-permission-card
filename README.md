# AI Agent Permission Card

Before I connect an AI agent to anything, I open Notes and type this:

`goal | may_read | may_write | ask_before | stop_if | show_me`

That's my whole task card. Six blanks.

It looks almost too plain to be useful. Still, it has saved me from handing a clever system a foggy job and far too many keys.

You can copy the [Markdown card](templates/permission-card.md), or use the [JSON](templates/permission-card.json) and [YAML](templates/permission-card.yaml) files in a structured workflow.

## Why I use it

Take these two requests:

> Draft a reply to this customer.

> Read the request, find the order, write a reply, and send it.

The first can finish as text on your screen. The second needs customer data, order data, and an outbound channel. One extra verb, "send," changes the job.

The card makes me deal with that difference before the run starts.

`goal` says what will be different when the work is over. "Watch my competitors" is foggy. "Compare today's prices on these three pages with yesterday's file" has an edge.

`may_read` names the shelves rather than the whole room. If the job needs three public URLs and one local file, I write those four sources down.

`may_write` is where I slow down. Reading a price is one job. Changing the live price is another. For an early run, this field often contains one local report and nothing else.

`ask_before` gets an actual verb: sending, publishing, paying, refunding, deleting, or overwriting. The pause belongs before the tool runs. A neat explanation afterwards is only a receipt.

`stop_if` covers the ugly page. I use it for a login screen, an unclear match, missing data, or a retry limit. I want the agent to point at the snag, not improvise its way into a wider scope.

`show_me` defines the evidence. It may ask for a URL, saved file, record ID, test result, timestamp, or log. "Done" doesn't count.

## A small example

The [fictional price-check card](examples/price-check.md) reads three `example.com` pages and yesterday's local file. It can write one Markdown report. It cannot sign in, edit a store, send a message, or retry forever.

The same example is available as [validated JSON](examples/price-check.json). No real company, account, or price appears in it.

## Run the checks

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover -s tests -v
python3 scripts/validate_examples.py
```

The [JSON Schema](schema/permission-card.schema.json) rejects a document when one of the six fields is missing or an unknown top-level field appears.

That catches a malformed card. It does not enforce access inside a browser, API, operating system, or agent runtime. Your tools still need real access controls.

Do not commit credentials, tokens, customer records, private URLs, or confidential incident details. [SECURITY.md](SECURITY.md) explains the boundary. The repository contains no agent, telemetry, remote call, account integration, or hosted form.

## Where the idea came from

I first used the card after abandoning an ecommerce automation that wandered into payments and refunds. I went backwards and picked a boring, read-only pilot instead. Much better.

The longer account is in [What Is an AI Agent?](https://www.mehmetkocabas.com/en/blog/what-is-an-ai-agent) on my site. This repository turns the six-field note into files you can copy and test.

The project uses the [MIT License](LICENSE). If you want to add an example, start with [CONTRIBUTING.md](CONTRIBUTING.md).
