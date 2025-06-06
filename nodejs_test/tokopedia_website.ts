// typescript

import * as express from 'express';
import type { Request, Response, NextFunction } from 'express';

import { createProxyMiddleware } from 'http-proxy-middleware';
import type { Filter, Options, RequestHandler } from 'http-proxy-middleware';

const app = express();

const proxyMiddleware = createProxyMiddleware<Request, Response>({
    target: 'http://www.example.org/api',
    changeOrigin: true,
});

app.use('/api', proxyMiddleware);

app.listen(3000);
