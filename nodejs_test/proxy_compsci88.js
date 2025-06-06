const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

// create the proxy
/** @type {import('http-proxy-middleware/dist/types').RequestHandler<express.Request, express.Response>} */
const exampleProxy = createProxyMiddleware({
    target: 'https://temp.compsci88.com/', // target host with the same base path
    changeOrigin: true, // needed for virtual hosted sites
});

// mount `exampleProxy` in web server
app.use('/', exampleProxy);
app.listen(3001);