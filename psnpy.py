#!/usr/bin/env python
# -*- coding: utf-8 -*-
import falcon


class PSNPyResource:
    def on_get(self, req, res):
        res.status = falcon.HTTP_200
        res.body = '{"message": "Hello, world!"}'

app = falcon.API()

psnpy = PSNPyResource()

app.add_route('/', psnpy)
