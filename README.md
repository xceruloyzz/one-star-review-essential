# One-Star Review of Something Essential

[![make.fun](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/xceruloyzz/one-star-review-essential/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/xceruloyzz/one-star-review-essential/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)

Entry for the [make.fun bounty "One-Star Review of Something Essential"](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629):
write the funniest deadpan one-star review, 160 characters or fewer, of an
everyday essential.

`main.py` is the harness driver (program/v1): it writes one single-line
review to `/output/entry.txt` — the same text on every run, no input, no
network, no randomness.

> Gravity never takes a day off, never apologises, and still drops my toast
> butter-side down every single morning.

112 characters. One essential (gravity), one true grievance everyone
recognises (toast landing butter-side down), deadpan throughout, and the
sting lands in the last few words.

## Local check

```
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # 112 chars, byte-identical on every run
```

## License

MIT — see [LICENSE](LICENSE).
