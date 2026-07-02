#!/usr/bin/env python3

import asyncio
import time

from na_atlib.ATSHA204 import DEFAULT_I2C_ADDR as ATSHA204_DEFAULT_I2C_ADDR
from na_atlib.ATSHA204.commands import *
from na_atlib.i2cbus import I2CBus


class AsyncATService:

    def __init__(self, bus_num=1):
        self._bus = I2CBus(bus_num, ATSHA204_DEFAULT_I2C_ADDR)
        self._lock = asyncio.Lock()

    def _command(self, cmd):
        self._bus.wake()

        self.bus.write(bytes(cmd))
        time.sleep(0.08)
        reply = self.bus.read(cmd.response_size)

        parsed = cmd.parse_answer(reply)
        
        return parsed.payload

    async def command(self, cmd):
        async with self._lock:
            return await asyncio.to_thread(self._command, cmd)

    def close(self):
        self._bus.close()