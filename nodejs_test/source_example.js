"use strict";
// typescript
Object.defineProperty(exports, "__esModule", { value: true });
var express = require("express");
var http_proxy_middleware_1 = require("http-proxy-middleware");
var app = express();
var proxyMiddleware = (0, http_proxy_middleware_1.createProxyMiddleware)({
    target: 'http://www.example.org/api',
    changeOrigin: true,
});
app.use('/api', proxyMiddleware);
app.listen(3009);
// proxy and keep the same base path "/api"
// http://127.0.0.1:3000/api/foo/bar -> http://www.example.org/api/foo/bar
