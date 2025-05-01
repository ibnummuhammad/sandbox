"use strict";
// typescript
Object.defineProperty(exports, "__esModule", { value: true });
var express = require("express");
var http_proxy_middleware_1 = require("http-proxy-middleware");
var app = express();
var proxyMiddleware = (0, http_proxy_middleware_1.createProxyMiddleware)({
    target: 'https://x.com',
    changeOrigin: true,
});
app.use('/', proxyMiddleware);
app.listen(3000);
