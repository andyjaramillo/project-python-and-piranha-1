#!/bin/env bash
curl --request POST http://andy-website.duckdns.org:5000/api/timeline_post -d 'name=andreas&email=andy.jaramillo022@gmail.com&content=Just added new Info to Database'
curl http://andy-website.duckdns.org:5000/api/timeline_post
