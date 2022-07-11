import pytest

dc_str = """\
version: '3.4'

services:
  node_1:
    image: ghcr.io/ovrclk/cosmos-omnibus:v0.2.4-cryptoorgchain-v3.3.3
    ports:
      - '26656:26656'
      - '26657:26657'
      - '1317:1317'
    environment:
      - MONIKER=node_1
      - CHAIN_JSON=https://raw.githubusercontent.com/cosmos/chain-registry/master/cryptoorgchain/chain.json
      - SNAPSHOT_QUICKSYNC=https://quicksync.io/crypto.json
    volumes:
      - ./node-data:/root/.chain-maind
"""

akash_str = """\
---
version: "2.0"

services:
  node:
    image: ghcr.io/ovrclk/cosmos-omnibus:v0.2.4-cryptoorgchain-v3.3.3
    env:
      - MONIKER=node_1
      - CHAIN_JSON=https://raw.githubusercontent.com/cosmos/chain-registry/master/cryptoorgchain/chain.json
      - SNAPSHOT_QUICKSYNC=https://quicksync.io/crypto.json
    expose:
      - port: 26657
        as: 80
        to:
          - global: true
      - port: 26656
        to:
          - global: true

profiles:
  compute:
    node:
      resources:
        cpu:
          units: 4
        memory:
          size: 8Gi
        storage:
          size: 100Gi
  placement:
    dcloud:
      attributes:
        host: akash
      signedBy:
        anyOf:
          - akash1365yvmc4s7awdyj3n2sav7xfx76adc6dnmlx63
      pricing:
        node:
          denom: uakt
          amount: 1000

deployment:
  node:
    dcloud:
      profile: node
      count: 1
"""

def test_load():
    assert 1 == 1

def test_load2():
    assert 1 == 3