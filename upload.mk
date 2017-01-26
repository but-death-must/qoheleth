.PHONY: upload
upload:
	scp -r -i ~/Dropbox/qoheleth-key.pem \
		nodes/html/* \
		ubuntu@qoheleth.post-self.io:/usr/share/nginx/html
